class Entity(object):
    def __init__(self, name):
        self._name = name
        self._inventory = set()
        self._equipped = set()
        self.hp, self.max_hp = 10, 10
        self.level, self.exp = 1, 0
        self.attack, self.dexterity = 0, 0
        self.defense, self.agility = 0, 0

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
        successful = item not in self._equipped
        self._equipped.add(item)

        if successful:
            item.trigger_equip(self)

        return successful


class Weapon(object):
    def __init__(self, name, attack, dexterity):
        self.name = name
        self.attack = attack
        self.dexterity = dexterity

    def trigger_equip(self, character):
        character.attack += self.attack
        character.dexterity += self.dexterity
