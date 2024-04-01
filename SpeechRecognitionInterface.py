import speech_recognition as sr

class SpeechRecognitionInterface:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_audio(self, audio_input, language='zh-CN'):
        try:
            with audio_input as source:
                print("Please Speak...")
                audio = self.recognizer.listen(source)

            print("Recognizing...")
            text = self.recognizer.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return "Sorry, your speech is unrecognized."
        except sr.RequestError as e:
            return f"Unable to connect to the internet: {e}"
        except Exception as e:
            return f"An error occurred: {e}"

def main():
    speech_recognition_interface = SpeechRecognitionInterface()
    mic = sr.Microphone()
    text = speech_recognition_interface.recognize_audio(mic)
    print("Result:", text)

if __name__ == "__main__":
    main()
