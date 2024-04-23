import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    print("Processing...")
    user_input = recognizer.recognize_google(audio).lower()
    print("You (Voice):", user_input)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError:
    print("Sorry, there was an error processing your request.")
