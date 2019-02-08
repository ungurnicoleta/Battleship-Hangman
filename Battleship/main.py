from Domain.Harta import Harta
from UI.BattleShipInterface import BattleShipInterface

if __name__ == '__main__':
    harta = Harta(True)
    hartaoponent = Harta(True)
    cons = BattleShipInterface(harta, hartaoponent)
    cons.run()
