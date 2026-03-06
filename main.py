import speech_recognition as sr
import pyttsx3
import webbrowser
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize recognizer
r = sr.Recognizer()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("ERROR: GEMINI_API_KEY not found. Create a .env file with your API key.")
    exit(1)

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    'gemini-2.5-flash',
    system_instruction="You are Coco, a helpful voice assistant. Give short, crisp responses in 1-2 sentences. Be conversational and concise."
)

def speak(text):
    """Make Coco speak"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def ask_gemini(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return "Sorry, I couldn't process that request."

def process_command(command):
    if "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open google" in command.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "exit" in command.lower() or "goodbye" in command.lower() or "quit" in command.lower() or "stop" in command.lower() or "bye" in command.lower() or "see you later" in command.lower() or "good bye" in command.lower():
        speak("Goodbye!")
        return False
    else:
        # Use Gemini for other questions
        answer = ask_gemini(command)
        print(f"Gemini: {answer}")
        speak(answer)
    return True

if __name__ == "__main__":
    speak("Hello, I am Coco. How may I help you today?")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3)

            command = r.recognize_google(audio)
            print(f"You said: {command}")

            if "coco" in command.lower():
                speak("Yes, how can I help you?")
                
                # Listen for the actual command
                with sr.Microphone() as source:
                    print("Waiting for command...")
                    audio = r.listen(source, timeout=5)
                    command = r.recognize_google(audio)
                    print(f"You said: {command}")
                    
                if not process_command(command):
                    break
            
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.WaitTimeoutError:
            continue