# -*- coding: utf-8 -*-

class GildedRose(object):
    """Gestion de la mise à jour quotidienne de l'inventaire."""

    def __init__(self, items):
        self.items = items

    def _is_sulfuras(self, item):
        """Retourne True si l'article est Sulfuras (article légendaire)."""
        return item.name == "Sulfuras, Hand of Ragnaros"

    def _is_aged_brie(self, item):
        """Retourne True si l'article est Aged Brie."""
        return item.name == "Aged Brie"

    def _is_backstage_pass(self, item):
        """Retourne True si l'article est un Backstage pass."""
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def _degrade_normal(self, item):
        """Dégrade la qualité d'un article normal (ou Conjured x2). Ne va jamais sous 0."""
        decrement = 2 if "Conjured" in item.name else 1
        item.quality = max(0, item.quality - decrement)

    def _update_sulfuras(self, item):
        """Sulfuras ne change jamais : ni qualité, ni sell_in."""
        pass

    def _update_aged_brie(self, item):
        """Aged Brie augmente en qualité avec le temps. Max 50."""
        item.quality = min(50, item.quality + 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = min(50, item.quality + 1)

    def _update_backstage_pass(self, item):
        """
        Backstage pass : qualité +1 si sell_in > 10, +2 si <= 10, +3 si <= 5.
        Tombe à 0 après le concert. Max 50.
        """
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
        """Item normal (et Conjured) : qualité diminue de 1 (ou 2), double après péremption."""
        self._degrade_normal(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._degrade_normal(item)

    def update_quality(self):
        """Met à jour la qualité de tous les articles pour une journée."""
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
