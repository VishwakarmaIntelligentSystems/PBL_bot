from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
from PIL import Image
import sys

recognizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)

contents = ["Children in the world", "Child labour in the world", "Child labour in India", "Contribution of India",
            "Child labor in Uttar Pradesh", "Laws on child labour", "A talk about Kailash Satyarthi",
            "Our action plan", "My logo", "A short poem on peace"]


def create_handouts():
    global recognizer
    speaker.say("Yes, I am noting it.")
    speaker.runAndWait()
    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Please choose a file name.")
                speaker.runAndWait()
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

                with open(filename, 'w') as f:
                    f.write(note)
                    done = True
                    speaker.say("Done")
                    speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Please repeat")
            speaker.runAndWait()


def add_query():
    global recognizer
    speaker.say("What is the query?")

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                item = recognizer.recognize_google(audio)
                item = item.lower()

                contents.append(item)
                done = True
                speaker.say("We need to take a query later on.")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Please try again")
            speaker.runAndWait()


def show_con():
    speaker.say("Here are the contents to be covered.")
    for item in contents:
        speaker.say(item)
    speaker.runAndWait()


def q():
    speaker.say("Bye, it was nice to interact with you all.")
    speaker.runAndWait()
    sys.exit(0)


def composition_of_cl():
    img = Image.open('./composition of labour.png')
    img.show()


def coicl():
    img = Image.open('./contribution of india in child labour.png')
    img.show()


def int_and_inter_cl():
    img = Image.open('./international and interstate child labour.png')
    img.show()


def rural_and_urban():
    img = Image.open('./RURAL and URBAN.png')
    img.show()


def up():
    img = Image.open('./up.png')
    img.show()


def poem():
    img = Image.open('./WhatsApp Image 2021-06-13 at 5.00.27 PM.jpeg')
    img.show()


def logo():
    img = Image.open('./WhatsApp Image 2021-06-13 at 5.25.32 PM.jpeg')
    img.show()


def action_plan():
    img = Image.open('./action plan.png')
    img.show()


def bio_sketch():
    img = Image.open('./2021-06-13 (2).png')
    img.show()


def greetings():
    speaker.say("Hello, my name is PBL bot, nice to meet you all.")
    speaker.runAndWait()


def q1():
    speaker.say(
        "Out of the 2.2 billion children in the world, around 217 million are prone to child labour in the whole world")
    speaker.runAndWait()


def q2():
    speaker.say(
        "The indian law has the following guidelines for the child labor in India- 1,The minimum age for employment "
        "is 14 years,2,Shift of 6 hours including 1 hour rest.3,No night shifts")
    speaker.runAndWait()


def q3():
    speaker.say(
        "Child exploitation refers to the use of children for someone else's advantage, gratification or profit often "
        "resulting in unjust, cruel and harmful treatment of the child.")
    speaker.runAndWait()


def q4():
    speaker.say("Uttar Pradesh in India is the most prone to child labour in India.")
    speaker.runAndWait()


def q5():
    speaker.say("Around 127 million children are prone to child labor in the whole world.")
    speaker.runAndWait()


def q6():
    speaker.say("10.1 million children are prone to child labor in India")
    speaker.runAndWait()


def q7():
    speaker.say("According to UNICEF, 12.6 million children are engaged in hazardous occupations.Only 10% of human "
                "trafficking in India is international, while 90% is interstate.There are an estimated 300,"
                "000 child beggars in India.Every year, 44,000 children fall into the clutches of gangs")
    speaker.runAndWait()


def q8():
    speaker.say("According to a report by the National Human Rights Commission of India, 40,000 children are abducted "
                "each year, leaving 11,000 untraced")
    speaker.runAndWait()


def affects_cl():
    img = Image.open('./affects.png')
    img.show()


mappings = {
    "Greetings": greetings,
    "Composition_of_child_labour": composition_of_cl,
    "contribution_of_india_in_child_labor": coicl,
    "international_and_interstate_child_labor": int_and_inter_cl,
    "rural_and_urban": rural_and_urban,
    "up": up,
    "exit": q,
    "action_plan": action_plan,
    "handouts": create_handouts,
    "query": add_query,
    "show_contents": show_con,
    "Kailash_Satyarthi": bio_sketch,
    "logo_slogan": logo,
    "poem": poem,
    "q1": q1,
    "q2": q2,
    "q3": q3,
    "q4": q4,
    "q5": q5,
    "q6": q6,
    "q7": q7,
    "q8": q8,
    "affects": affects_cl
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, 0.2)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio)
            message = message.lower()

            assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
