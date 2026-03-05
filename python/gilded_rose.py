# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def _is_aged_brie(self, item):
        return item.name == "Aged Brie"

    def _is_backstage_pass(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def _degrade_normal(self, item):
        decrement = 2 if "Conjured" in item.name else 1
        item.quality = max(0, item.quality - decrement)

    def _update_sulfuras(self, item):
        pass

    def _update_aged_brie(self, item):
        item.quality = min(50, item.quality + 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = min(50, item.quality + 1)

    def _update_backstage_pass(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        else:
            increment = 1
            if item.sell_in <= 5:
                increment = 3
            elif item.sell_in <= 10:
                increment = 2
            item.quality = min(50, item.quality + increment)
        item.sell_in -= 1

    def _update_normal_item(self, item):
        self._degrade_normal(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._degrade_normal(item)

    def update_quality(self):
        for item in self.items:
            if self._is_sulfuras(item):
                self._update_sulfuras(item)
            elif self._is_aged_brie(item):
                self._update_aged_brie(item)
            elif self._is_backstage_pass(item):
                self._update_backstage_pass(item)
            else:
                self._update_normal_item(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
