from random import randint

from entities.sentance import Hangman


class RepoException(Exception):
    pass


class Repository(object):
    def __init__(self, elements):
        self.__repo = elements

    def addSentance(self, sentance):
        if sentance not in self.__repo:
            self.__repo.append(Hangman(sentance))
        else:
            raise RepoException("Element adaugat anterior")

    def __getitem__(self, item):
        for sentance in self.__repo:
            if sentance.id == item:
                return sentance
        raise RepoException("Inexistent")

    def randomGenerateSentance(self):
        return self.__repo[randint(0, len(self.__repo) - 1)]

    def getAll(self):
        return self.__repo
