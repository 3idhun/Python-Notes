import speechrecognition as sr
import webbrowser  # inbuilt module
import pyttsx3  # inbuilt module, text to speech purpose

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say("I will speak this text")
    engine.runAndWait()


if __name__ == "__main__":
    speak("hey sir how may i help you")

