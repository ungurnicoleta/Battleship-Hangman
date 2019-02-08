from repository.Repository import Repository
class Controller(object):
    def __init__(self, repo):
        self.__repository = repo
        self.__hangman = None
        self.__dead = ""
        self.__poz = 0

    def guess(self, letter):
        if self.__hangman.check_letter(letter):
            self.__hangman.replace_letter(letter)
        else:
            t = list("hangman")
            self.__dead += t[self.__poz]
            self.__poz += 1

    def get_hangman(self):
        to_print = ""
        for letter in self.__hangman.hangman:
            to_print += str(letter)
        return to_print + "   " + self.__dead

    def get_dead(self):
        if str(self.__hangman.sentance) == str(self.__hangman.hangman):
            return False
        return True if len(self.__dead) != 7 else False

    def play(self):
        self.__hangman = self.__repository.randomGenerateSentance()

    def addSentance(self, sentance):
        self.__repository.addSentance(sentance)