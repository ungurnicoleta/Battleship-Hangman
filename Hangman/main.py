from controller.controller import Controller
from entities.sentance import Hangman
from repository.FileRepository import TextFile
from repository.PickleFile import PickleRepository

#controller = Controller(TextFile("entities/Hangman.txt"))
controller = Controller(PickleRepository("entities/Hangman.pickle"))

def run():
    while True:
        print("Choose a command: 1.Add sentance'\n'2.Play'\n'3.Exit'\n'")
        cmd = int(input("Insert command: "))
        if cmd == 1:
            sentance = input("Insereaza noua propozitie: ")
            controller.addSentance(sentance)
        elif cmd == 2:
            controller.play()
            while controller.get_dead():
                print(controller.get_hangman())
                letter = input("Alege litera: ")
                controller.guess(letter)
        elif cmd == 0:
            break


run()
