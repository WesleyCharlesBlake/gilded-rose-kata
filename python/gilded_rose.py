# -*- coding: utf-8 -*-
class DefaultUpdater(object):
    max_quality = 50

    def __init__(self, item):
        self.item = item

    def increase_quality(self):
        if self.item.quality < self.max_quality:
            self.item.quality = self.item.quality + 1

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1

    def decrease_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def update_quality(self):
        self.decrease_quality()
        self.decrease_sell_in()

        if self.item.sell_in < 0:
            self.decrease_quality()


class AgedBrieUpdater(DefaultUpdater):
    def update_quality(self):
        self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.increase_quality()


class BackStageUpdater(DefaultUpdater):
    days_threshold_min = 10
    days_threshold_max = 5

    def reset_quality(self):
        self.item.quality = 0

    def update_quality(self):
        self.increase_quality()
        if self.item.sell_in <= self.days_threshold_min:
            self.increase_quality()
        if self.item.sell_in <= self.days_threshold_max:
            self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.reset_quality()


class SulfurasUpdater(DefaultUpdater):

    def update_quality(self):
        pass


class ConjuredUpdater(DefaultUpdater):
    def decrease_quality(self):
        DefaultUpdater.decrease_quality(self)
        DefaultUpdater.decrease_quality(self)


class ItemUpdater(object):

    class_mapping = {
        "Aged Brie": AgedBrieUpdater,
        "Sulfuras, Hand of Ragnaros": SulfurasUpdater,
        "Backstage passes to a TAFKAL80ETC concert": BackStageUpdater,
        "Conjured Mana Cake": ConjuredUpdater
    }

    @classmethod
    def create(cls, item):
        if item.name in cls.class_mapping:
            return cls.class_mapping[item.name](item)
        return DefaultUpdater(item)


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            itemUpdater = ItemUpdater.create(item)
            itemUpdater.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
