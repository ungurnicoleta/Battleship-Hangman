import random
from Domain.Computer import Computer


class BattleShipInterface:

    def __init__(self, harta, hartaoponent):
        self.__harta = harta
        self.__hartaoponent = hartaoponent
        self.__semiintelligentplayer = Computer()

    def run(self):
        print("Opponent ship generation initialized...")
        self.__hartaoponent.generateRandomShips()
        print("Opponent ship generation completed successfully!")
        print("Player ship generation initialized...")
        for i in range(2, 5):
            while True:
                try:
                    print("Please insert coordinates for the ship of length " + str(i))
                    x = int(input("x:"))
                    y = int(input("y:"))
                    vert = bool(input("vertical[True/False]:"))
                    self.__harta.addShip(x, y, i, vert)
                    break
                except Exception:
                    print("Choose different position and orientation:")
        print("Player ship generation completed successfully!")

        print("Oponent's map")
        print(self.__hartaoponent)
        print("Player's map")
        print(self.__harta)

        while not self.__harta.defeated() and not self.__hartaoponent.defeated():
            print("Player has the floor!")
            while True:
                try:
                    print("Choose target coordinates:")
                    x = int(input("x:"))
                    y = int(input("y:"))
                    if self.__hartaoponent.hit(x, y):
                        print("Bullseye!")
                    else:
                        print("hmmm...")
                    break
                except Exception:
                    print("Invalid coordinates!")
            print("Oponent has the floor!")

            x, y = self.__semiintelligentplayer.chooseCoordinates()
            if self.__harta.hit(x, y):
                print("Bullseye!")
            else:
                print("yeeeey!!!")

            print("Oponent's map")
            print(self.__hartaoponent)
            print("Player's map")
            print(self.__harta)

        if self.__harta.defeated():
            print("You have lost!")
        else:
            print("You have won!")








