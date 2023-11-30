import speech_recognition
import pyttsx3 as tts

recognizer=speech_recognition.Recognizer()
speaker=tts.init()

speaker.say("ça te dit")