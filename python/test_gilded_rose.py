# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_normal_item_quality_decreases_by_1_before_sell_in(self):
        items = [Item("Normal Item", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_normal_item_quality_decreases_by_2_after_sell_in(self):
        items = [Item("Normal Item", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(18, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_normal_item_quality_never_negative(self):
        items = [Item("Normal Item", 0, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_quality_increases_by_1_before_sell_in(self):
        items = [Item("Aged Brie", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_aged_brie_quality_increases_by_2_after_sell_in(self):
        items = [Item("Aged Brie", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_aged_brie_quality_never_above_50(self):
        items = [Item("Aged Brie", 0, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_quality_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_sell_in_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_backstage_quality_increases_by_1_when_sell_in_above_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(14, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
