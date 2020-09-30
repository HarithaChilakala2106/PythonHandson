from random import randint, random

from Assignment6.Spaceship import Spaceship
from Assignment6.Upgradeship import upgradeship


def initiatecombat(spaceship1, spaceship2):
    turn = randint(1, 2)
    # lists = [spaceship1, spaceship2]
    # source = random.choice(lists)
    # opponent = 1 if list.index(random.choice(lists)) == 0 else 0
    # random.choice(list of spaceship) listofspaceships.pop(choosen attacker)
    skipattack = {1: "n", 2: "n"}
    while True:
        if turn == 1:
            source = spaceship1
            opponent = spaceship2
        else:
            source = spaceship2
            opponent = spaceship1
        print(source.name + " turn : ")
        if source.damage > 0:
            source.attack(opponent)
        else:
            print(f"{source.name} can't attack because it has no damage")
            skipattack[turn] = "y"
        turn = 2 if (turn == 1) else 1
        if len(list(val for val in skipattack.values() if val == "y")) == 2:
            print("Both spaceships skipped their attack since their damage is 0. So Game is Tie")
            break
        if spaceship1.hp == 0 or spaceship2.hp == 0:
            print("One of the space ship is destroyed. So, Game Over")
            break


if __name__ == '__main__':
    battlecruiser = Spaceship("Battlecruiser", 9, 2, 1)
    corsair = Spaceship("Corsair", 5, 3, 1)
    shipsincombat = {1: battlecruiser, 2: corsair}
    print(battlecruiser.__str__())
    print(corsair.__str__())
    upgradesavailable = {1: [x for x in Spaceship.upgrades.keys()], 2: [x for x in Spaceship.upgrades.keys()]}
    while True:
        for key, value in shipsincombat.items():
            print(str(key) + "." + value.name)
        print("3.No need of upgradation (for both ships) ")
        whoneedupgradation = int(input("Who want to upgrade their ships choose your key from the above : "))
        if not 1 <= whoneedupgradation <= 2:
            print("Both ships doesn't need upgradation")
            break
        elif len(upgradesavailable[whoneedupgradation]) == 0:
            print(f"No upgrade options availble for {shipsincombat[whoneedupgradation]}")
        else:
            upgradeship(shipsincombat[whoneedupgradation], upgradesavailable[whoneedupgradation])
    initiatecombat(battlecruiser, corsair)
