from main import Entity, Weapon, Armour

import unittest


class EntityTestCase(unittest.TestCase):
    def setUp(self):
        self.e = Entity(name="John")
        self.sword = Weapon(name="Sword", attack=5, dexterity=1)
        self.chainmail = Armour(name="Chainmail", defense=7, agility=-2)

    def test_init(self):
        self.assertEqual(self.e.name, "John")
        self.assertEqual(len(self.e.inventory), 0)
        self.assertEqual(len(self.e.equipped), 0)
        self.assertEqual(self.e.level, 1)
        self.assertEqual(self.e.exp, 0)
        self.assertEqual(self.e.hp, 10)
        self.assertEqual(self.e.max_hp, 10)
        self.assertEqual(self.e.attack, 0)
        self.assertEqual(self.e.dexterity, 0)
        self.assertEqual(self.e.defense, 0)
        self.assertEqual(self.e.agility, 0)

    def test_name_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.e.name = "Robert"

    def test_inventory_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.e.inventory = []

    def test_equipped_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.e.equipped = []

    def test_pick_simple(self):
        self.assertTrue(self.e.pick("sword"))
        self.assertIn("sword", self.e.inventory)

    def test_pick_only_considers_unique_objects(self):
        self.assertTrue(self.e.pick("sword"))
        self.assertFalse(self.e.pick("sword"))

        self.assertEqual(list(self.e.inventory).count("sword"), 1)

    def test_equip_simple(self):
        self.assertTrue(self.e.pick(self.sword))
        self.assertTrue(self.e.equip(self.sword))
        self.assertIn(self.sword, self.e.inventory)
        self.assertIn(self.sword, self.e.equipped)

    def test_equip_only_considers_unique_objects(self):
        self.assertTrue(self.e.pick(self.chainmail))
        self.assertTrue(self.e.equip(self.chainmail))
        self.assertFalse(self.e.equip(self.chainmail))

        self.assertEqual(self.e.defense, 7)
        self.assertEqual(self.e.agility, -2)

    def test_equip_calls_use_method(self):
        self.assertEqual(self.e.attack, 0)
        self.assertEqual(self.e.dexterity, 0)

        self.assertTrue(self.e.pick(self.sword))
        self.assertTrue(self.e.equip(self.sword))

        self.assertEqual(self.e.attack, 5)
        self.assertEqual(self.e.dexterity, 1)

    def test_equip_only_considers_picked_items(self):
        self.assertFalse(self.e.equip(self.sword))

        self.assertEqual(self.e.attack, 0)
        self.assertEqual(self.e.dexterity, 0)

    def test_unequip_simple(self):
        self.assertTrue(self.e.pick(self.sword))
        self.assertTrue(self.e.pick(self.chainmail))
        self.assertTrue(self.e.equip(self.sword))
        self.assertTrue(self.e.equip(self.chainmail))

        self.assertTrue(self.e.unequip(self.sword))
        self.assertFalse(self.e.unequip(self.sword))
        self.assertTrue(self.e.unequip(self.chainmail))
        self.assertFalse(self.e.unequip(self.chainmail))

        self.assertIn(self.sword, self.e.inventory)
        self.assertNotIn(self.sword, self.e.equipped)
        self.assertIn(self.chainmail, self.e.inventory)
        self.assertNotIn(self.chainmail, self.e.equipped)

        self.assertEqual(self.e.attack, 0)
        self.assertEqual(self.e.dexterity, 0)
        self.assertEqual(self.e.defense, 0)
        self.assertEqual(self.e.agility, 0)

    def test_unequip_only_considers_equipped_items(self):
        self.assertFalse(self.e.unequip(self.sword))
        self.assertFalse(self.e.unequip(self.chainmail))

        self.assertEqual(self.e.attack, 0)
        self.assertEqual(self.e.dexterity, 0)
        self.assertEqual(self.e.defense, 0)
        self.assertEqual(self.e.agility, 0)
