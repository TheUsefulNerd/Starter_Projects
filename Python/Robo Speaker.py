#My Second project :).
#I am Advait.
#This project is inspired from @CodewithHarry(YT). This is the first step in text to speech recognition projects.
#This is the baby step to learn and create a AI Assistant one day. Looking forward to it!!
# ------------------------------------------------------------------------------------------------------------------------

import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robo Speaker")
# The statement engine = pyttsx3.init() initializes the speech synthesis engine provided by the pyttsx3 library.
#init() is a function provided by pyttsx3 that initializes the speech synthesis engine.
#It creates an instance of the Engine class, which is responsible for converting text into speech.
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak (or 'q' to quit): ")
        if x == "q":
            break
        engine.say(x)
        engine.runAndWait()
