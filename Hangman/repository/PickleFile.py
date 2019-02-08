from entities.sentance import Hangman
from repository.Repository import Repository
import pickle
from validation.Validator import HangmanException

class PickleRepository(Repository):
    def __init__(self, fileName):
        self.__fileName = fileName
        super().__init__(self.__readFromFile())


    def __readFromFile(self):
        try:
            file = open(self.__fileName, "rb")
            return pickle.load(file)
        except EOFError:
            return []
        except IOError as ex:
            print("An error occured - " + str(ex))

    def __writeToFile(self, sentances):
        try:
            file = open(self.__fileName, "wb")
            return pickle.dump(sentances, file)
        except EOFError:
            return []
        except IOError as ex:
            print("An error occured - " + str(ex))


    def addSentance(self, sentance):
        if sentance not in super().getAll():
            super().addSentance(sentance)
            self.__writeToFile(super().getAll())
        else:
            raise HangmanException("Propozitia a mai fost introdusa!")
