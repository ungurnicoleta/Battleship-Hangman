import random


class Computer:

    def __init__(self):
        self._goodCandidates = []
        self._index = 0
        self._neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def includeHit(self, hit):
        if hit.ishit():
            self._goodCandidates.append(hit)

    def chooseCoordinates(self):
        if len(self._goodCandidates) == 0:
            x = random.randint(0, 7)
            y = random.randint(0, 7)

        else:
            x, y = self._goodCandidates[0].x + self._neighbors[self._index][0], self._goodCandidates[0].y + \
                   self._neighbors[self._index][1]
            self._index += 1
            if self._index == 3:
                self._goodCandidates.pop()
                self._index = 0
        return x, y




