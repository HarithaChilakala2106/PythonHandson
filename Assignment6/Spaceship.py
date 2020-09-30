class Spaceship:
    upgrades = {1: {"name": "TitaniumArmor", "armor": 3, "hp": 250, "desc": "Ship gets an extra +3 armor, and +250 HP"},
                2: {"name": "AbsorptionShield", "armor": +0.5, "desc": "Ship gets an extra +50% armor"},
                3: {"name": "ProtonTorpedos", "damage": 25, "desc": "Ship gets an extra 25 damage"},
                4: {"name": "FlareEngine", "armor": 3, "hp": +0.2, "damage": +0.5, "desc": "Ship gets +50% damage, +3 armor and +20% HP"}}

    def __init__(self, name: str, hp: int, armor: int, damage: int):
        self.name = name
        if hp > 0:
            self.hp = hp
        else:
            self.hp = 1
        self.armor = armor
        self.damage = damage

    def __str__(self):
        return f"{self.name} hp = {self.hp} armor = {self.armor} damage ={self.damage}"

    def attack(self, opponent):
        print(self.name + " attacks " + opponent.name)
        opponent.damage = self.damage - opponent.armor
        '''Incoming armor can’t reduce damage to less than 1.'''
        if opponent.damage < 1:
            opponent.damage = 1
        opponent.hp = opponent.hp - opponent.damage
        opponent.hp = 0 if opponent.hp < 0 else opponent.hp
        print(" " + self.__str__())
        print(" " + opponent.__str__())
