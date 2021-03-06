from autorepr import autorepr


class Entity(object):
    __repr__ = autorepr(
        [
            "name",
            "level",
            "exp",
            "inventory",
            "equipped",
            "hp",
            "max_hp",
            "attack",
            "dexterity",
            "defense",
            "agility",
            "aura",
        ]
    )

    def __init__(self, name):
        self._name = name
        self._inventory = set()
        self._equipped = set()
        self.hp, self.max_hp = 10, 10
        self.level, self.exp = 1, 0
        self.attack, self.dexterity = 0, 0
        self.defense, self.agility = 0, 0
        self.aura = 0

    @property
    def name(self):
        return self._name

    @property
    def inventory(self):
        return self._inventory

    @property
    def equipped(self):
        return self._equipped

    def pick(self, item):
        successful = item not in self._inventory
        self._inventory.add(item)
        return successful

    def equip(self, item):
        successful = item in self._inventory and item not in self._equipped

        if successful:
            self._equipped.add(item)
            item.trigger_equip(self)

        return successful

    def unequip(self, item):
        try:
            self._equipped.remove(item)
            item.trigger_unequip(self)
            return True
        except KeyError:
            return False


class Weapon(object):
    __repr__ = autorepr(["name", "attack", "dexterity"])

    def __init__(self, name, attack, dexterity):
        self.name = name
        self.attack = attack
        self.dexterity = dexterity

    def trigger_equip(self, character):
        character.attack += self.attack
        character.dexterity += self.dexterity

    def trigger_unequip(self, character):
        character.attack -= self.attack
        character.dexterity -= self.dexterity


class Armour(object):
    __repr__ = autorepr(["name", "defense", "agility"])

    def __init__(self, name, defense, agility):
        self.name = name
        self.defense = defense
        self.agility = agility

    def trigger_equip(self, character):
        character.defense += self.defense
        character.agility += self.agility

    def trigger_unequip(self, character):
        character.defense -= self.defense
        character.agility -= self.agility


class Wings(object):
    __repr__ = autorepr(["name", "aura"])

    def __init__(self, name, aura):
        self.name = name
        self.aura = aura

    def trigger_equip(self, character):
        character.aura += self.aura

    def trigger_unequip(self, character):
        character.aura -= self.aura
