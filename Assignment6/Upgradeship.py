from math import floor

from Assignment6.Spaceship import Spaceship


def upgradeship(shiptoupgrade: Spaceship, availableoptions):
    while True:
        print(f"Below are the upgrades available for {shiptoupgrade.name} ship")
        for option in availableoptions:
            print(" " + str(option) + "." + Spaceship.upgrades[option]["name"] + " - " + Spaceship.upgrades[option][
                'desc'])
        choosedupdradation = int(input("Choose the upgrade option only from the above available options : "))
        while choosedupdradation not in availableoptions:
            choosedupdradation = int(input("Choose the upgrade option only from the above available options : "))
        availableoptions.remove(choosedupdradation)
        if choosedupdradation == 1:
            shiptoupgrade.armor = shiptoupgrade.armor + Spaceship.upgrades[choosedupdradation]["armor"]
            shiptoupgrade.hp = shiptoupgrade.hp + Spaceship.upgrades[choosedupdradation]["hp"]
        elif choosedupdradation == 2:
            shiptoupgrade.armor = shiptoupgrade.armor + (
                    shiptoupgrade.armor * Spaceship.upgrades[choosedupdradation]["armor"])
        elif choosedupdradation == 3:
            shiptoupgrade.damage = shiptoupgrade.damage + Spaceship.upgrades[choosedupdradation]["damage"]
        elif choosedupdradation == 4:
            shiptoupgrade.armor = shiptoupgrade.armor + Spaceship.upgrades[choosedupdradation]["armor"]
            shiptoupgrade.hp = shiptoupgrade.hp + (shiptoupgrade.hp * Spaceship.upgrades[choosedupdradation]["hp"])
            shiptoupgrade.damage = shiptoupgrade.damage + (
                    shiptoupgrade.damage * Spaceship.upgrades[choosedupdradation]["damage"])
        # after upgradation the damage should not be less than 0 ? TODO: do we need to handle this?
        # if shiptoupgrade.damage < 0:
        #    shiptoupgrade.damage = 1
        '''
        Round-down all values resulting from calculations
        '''
        shiptoupgrade.armor = floor(shiptoupgrade.armor)
        shiptoupgrade.hp = floor(shiptoupgrade.hp)
        shiptoupgrade.damage = floor(shiptoupgrade.damage)
        print(" " + shiptoupgrade.__str__())
        if input("Do you want to continue upgradation (y/n) : ") == "n":
            break
        if len(availableoptions) == 0:
            print("No more options available for upgradation(All are utilized)")
            break
