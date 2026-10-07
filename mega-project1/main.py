import re
import speech_recognition as sr
import pyttsx3
import webbrowser
recognizer = sr.Recognizer()


def processCommand(c):
    search = c.lower()

    webbrowser.open(f"https://{search}.com")

def speak(text):
    engine = pyttsx3.init("sapi5")
    engine.say(text)
    engine.runAndWait()
    engine.stop()


if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:
        print("Listening...")

        try:
            # Microphone is opened ONLY here
            with sr.Microphone() as source:
                audio = recognizer.listen(
                    source,
                    timeout=2,
                    phrase_time_limit=3
                )

            # Microphone is now CLOSED
            print("recognizing...")

            word = recognizer.recognize_google(audio).strip().lower()

            print(f"Heard: {word}")

            if word == "jarvis":

                print("JARVIS DETECTED")

                # TTS happens AFTER microphone is released
                speak("Ya")

                print("Jarvis Active..")

                # Open microphone again
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)

                # Microphone released again
                command = recognizer.recognize_google(audio).strip().lower()


                if command in {"stop", "stop it", "exit", "quit"}:
                    speak("Stopping")
                    break
                processCommand(command)
            if word in {"stop", "stop it", "exit", "quit"}:
                speak("Stopping")
                break
        except sr.WaitTimeoutError:
            print("No speech detected")

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print(f"Error: {e}")