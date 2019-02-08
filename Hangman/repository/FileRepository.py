from entities.sentance import Hangman
from repository.Repository import Repository
from validation.Validator import HangmanException


class TextFile(Repository):
    def __init__(self, fileName):
        self.__fileName = fileName
        super().__init__(self.__read_from_file())

    def __writeToFile(self, sentance):
        try:
            file = open(self.__fileName, "a")
            file.write(str(sentance) + "\n")
            file.close()
        except Exception as ex:
            print(str(ex))

    #
    # def __writeAllToFile(self):
    #     try:
    #         file = open(self.__fileName, "w")
    #         for sentance in super().getAll():
    #             file.write("{}\n".format(sentance.id))
    #         file.close()
    #     except IOError:
    #         raise HangmanException("Imposibil de deschis fisierul!")

    def __read_from_file(self):
        try:
            file = open(self.__fileName, "r")
            results = []
            for line in file:
                line = line.strip("\n")
                results.append(Hangman(line))
            file.close()
            return results[:]
        except Exception as ex:
            print("Something occured: " + str(ex))

    def addSentance(self, sentance):
        if sentance not in super().getAll():
            super().addSentance(sentance)
            self.__writeToFile(sentance)
        else:
            raise HangmanException("blablabla")
