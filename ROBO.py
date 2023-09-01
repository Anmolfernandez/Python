import pyttsx3
import time
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Anmol Fernandis")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want me to speak: ")
        if x =="q":
            engine.setProperty('rate',100)
            engine.say("bye bye friend")
            engine.runAndWait()
            break
        engine = pyttsx3.init()
        engine.setProperty('rate',100)
        engine.say(x)
        engine.runAndWait()
