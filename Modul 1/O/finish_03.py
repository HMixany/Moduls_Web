from abc import ABC, abstractmethod


class Discount:
    @abstractmethod
    def apply(self, price):
        pass


class BlackFridayDiscount(Discount):
    def apply(self, price):
        return price * 0.7


class SummerDiscount(Discount):
    def apply(self, price):
        return price * 0.9
