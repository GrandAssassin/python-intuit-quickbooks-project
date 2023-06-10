import pyttsx3
def speak(text):
    pyttsx3.speak(text)
    print(text)
speak("Hello")