from gilded_rose import Item, GildedRose

if __name__ == '__main__':
    items = [Item("Aged Brie", quality=10, sell_in=10)]
    gilded_rose = GildedRose(items)
    for _ in range(5):
        gilded_rose.update_quality()
        print(items[0])