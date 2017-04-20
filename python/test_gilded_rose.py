# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 1, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_conjured(self):
        items = [Item("Conjured Mana Cake", 2, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[0].sell_in)
        # one more day
        gilded_rose.update_quality()
        self.assertEqual(3, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        # one more day again
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(-1, gilded_rose.items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
