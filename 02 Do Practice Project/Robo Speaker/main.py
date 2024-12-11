import pyttsx3

engine = pyttsx3.init()

if __name__ == "__main__":
    print("Welcome to Robo Speaker v1.1")
    while True:
        text_to_speak = input("Enter what you want me to speak: ")
        if text_to_speak.lower() == "exit":
            engine.say("Ok! I am signing off. Have a nice day.")
            engine.runAndWait()
            break
        engine.say(text_to_speak)
        engine.runAndWait()
