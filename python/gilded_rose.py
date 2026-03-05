# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def _is_aged_brie(self, item):
        return item.name == "Aged Brie"

    def update_quality(self):
        for item in self.items:
            if not self._is_aged_brie(item) and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if not self._is_sulfuras(item):
                        decrement = 2 if "Conjured" in item.name else 1
                        item.quality = max(0, item.quality - decrement)
            else:
                if item.quality < 50:
                    item.quality += 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality += 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality += 1
            if not self._is_sulfuras(item):
                item.sell_in -= 1
            if item.sell_in < 0:
                if not self._is_aged_brie(item):
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if not self._is_sulfuras(item):
                                decrement = 2 if "Conjured" in item.name else 1
                                item.quality = max(0, item.quality - decrement)
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality += 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
