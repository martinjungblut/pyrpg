from main import Entity, Weapon

import unittest


class EntityTestCase(unittest.TestCase):
    def setUp(self):
        self.sword = Weapon(name="Sword", attack=5, dexterity=1)

    def test_init(self):
        e = Entity(name="John")
        self.assertEqual(e.name, "John")
        self.assertEqual(len(e.inventory), 0)
        self.assertEqual(len(e.equipped), 0)
        self.assertEqual(e.level, 1)
        self.assertEqual(e.exp, 0)
        self.assertEqual(e.hp, 10)
        self.assertEqual(e.max_hp, 10)
        self.assertEqual(e.attack, 0)
        self.assertEqual(e.dexterity, 0)
        self.assertEqual(e.defense, 0)
        self.assertEqual(e.agility, 0)

    def test_name_is_read_only(self):
        e = Entity(name="John")

        with self.assertRaises(AttributeError):
            e.name = "Robert"

    def test_inventory_is_read_only(self):
        e = Entity(name="John")

        with self.assertRaises(AttributeError):
            e.inventory = []

    def test_equipped_is_read_only(self):
        e = Entity(name="John")

        with self.assertRaises(AttributeError):
            e.equipped = []

    def test_pick_simple(self):
        e = Entity(name="John")
        self.assertTrue(e.pick("sword"))
        self.assertIn("sword", e.inventory)

    def test_pick_only_considers_unique_objects(self):
        e = Entity(name="John")

        self.assertTrue(e.pick("sword"))
        self.assertFalse(e.pick("sword"))

        self.assertEqual(list(e.inventory).count("sword"), 1)

    def test_equip_simple(self):
        e = Entity(name="John")
        self.assertTrue(e.pick(self.sword))
        self.assertTrue(e.equip(self.sword))
        self.assertIn(self.sword, e.inventory)
        self.assertIn(self.sword, e.equipped)

    def test_equip_only_considers_unique_objects(self):
        e = Entity(name="John")

        self.assertTrue(e.pick(self.sword))
        self.assertTrue(e.equip(self.sword))
        self.assertFalse(e.equip(self.sword))

        self.assertIn(self.sword, e.inventory)
        self.assertIn(self.sword, e.equipped)

        self.assertEqual(e.attack, 5)
        self.assertEqual(e.dexterity, 1)

    def test_equip_calls_use_method(self):
        e = Entity(name="John")
        self.assertEqual(e.attack, 0)
        self.assertEqual(e.dexterity, 0)

        self.assertTrue(e.pick(self.sword))
        self.assertTrue(e.equip(self.sword))

        self.assertEqual(e.attack, 5)
        self.assertEqual(e.dexterity, 1)
