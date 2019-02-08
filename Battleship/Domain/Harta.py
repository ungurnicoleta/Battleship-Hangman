from Domain.Ship import Ship
from Domain.Hit import Hit
import random


class HartaEx(Exception):
    pass


class Harta:

    def __init__(self, shipsvisible):
        self._visible = shipsvisible
        self._ships = []
        self._hits = []
        self._totalhitsleft = 9
        self._matrice = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

    def defeated(self):
        return self._totalhitsleft == 0

    def generateRandomShips(self):
        for ship in [Ship(2, True), Ship(3, False), Ship(4, True)]:
            shipx = random.randint(0, 7 - ship.length)
            shipy = random.randint(0, 7 - ship.length)
            ship.x = shipx
            ship.y = shipy
            while ship in self._ships:
                shipx = (shipx + 1) % (7 - ship.length)
                shipy = (shipy + 1) % (7 - ship.length)
                ship.x = shipx
                ship.y = shipy
            self._ships.append(ship)
        print(len(self._ships))

    def __str__(self):
        if self._visible:
            for ship in self._ships:
                if ship.horizontal:
                    for x in range(ship.x, ship.x + ship.length):
                        self._matrice[x][ship.y] = 1
                else:
                    for y in range(ship.y, ship.y + ship.length):
                        self._matrice[ship.x][y] = 1

        for hit in self._hits:
            if hit.ishit:
                self._matrice[hit.x][hit.y] = 2
            else:
                self._matrice[hit.x][hit.y] = 3

        s = ""
        for i in range(8):
            for j in range(8):
                if (self._matrice[i][j] == 0):
                    s += '*'
                if (self._matrice[i][j] == 1):
                    s += 'X'
                if (self._matrice[i][j] == 2):
                    s += '1'
                if (self._matrice[i][j] == 3):
                    s += '0'
            s += '\n'
        return s

    def hit(self, x, y):
        for ship in self._ships:
            if ship.inside(x, y):
                if ship.checkHit(x, y):
                    self._totalhitsleft -= 1
                    self._hits.append(Hit(x, y, True))
                    return True
        self._hits.append(Hit(x, y, False))
        return False

    def addShip(self, x, y, length, horizontal):
        ship = Ship(length, horizontal)
        ship.x = x
        ship.y = y
        if ship in self._ships:
            raise HartaEx("Invalid ship position! Recalibrate!")
        self._ships.append(ship)














