class Hangman(object):
    def __init__(self, sentance):
        self.__id = sentance
        self.__sentance = self.__convert_sentance(sentance)
        self.__hangman = self.__convert_to_hangman(sentance)

    def __convert_sentance(self, sentance):
        sentance = sentance.split()
        hangman = []
        for word in sentance:
            t = list(word)
            for i in t:
                hangman.append(i)
            hangman.append(" ")
        return hangman

    def __convert_to_hangman(self, sentance):
        sentance = sentance.split()  # transform to array of words
        hangman = []
        for word in sentance:
            if len(list(word)) > 3:
                t = list(word)  # transform word to array of letters
                hangman.append(t[0])
                for i in range(1, len(t) - 1):
                    hangman.append("_")
                hangman.append(t[-1])
            else:
                t = list(word)
                for i in t:
                    hangman.append(i)
            hangman.append(" ")
        return hangman

    @property
    def sentance(self):
        return self.__sentance[:]

    @property
    def hangman(self):
        return self.__hangman[:]

    @property
    def id(self):
        return self.__id

    def check_letter(self, letter):
        return letter in self.__sentance

    def replace_letter(self, letter):
        for i in range(0, len(self.__sentance)):
            if self.__sentance[i] == letter:
                self.__hangman[i] = letter

    def __eq__(self, other):
        return self.__id == other

    def __str__(self):
        return str(self.__hangman) + "\n" + str(self.__sentance)
