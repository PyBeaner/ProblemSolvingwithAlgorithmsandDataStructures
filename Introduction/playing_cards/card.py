# coding=utf-8
from collections import defaultdict

__author__ = 'PyBeaner'

CardSuits = ("Spades", "Diamonds", "Clubs", "Hearts")
CardValues = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
GhostValues = ("Black Ghost", "Red Ghost")


class Card:
    def __init__(self, value, suit=None):
        """
        spades(黑桃), diamonds(方片), clubs(梅花), hearts(红桃)
        """
        self.suit = suit
        self.value = value

    def __str__(self):
        if self.suit:
            return "the {} of {}".format(self.value, self.suit)
        return self.value


class Deck:
    def __init__(self):
        self.cards = defaultdict(list)
        for suit in CardSuits:
            for value in CardValues:
                c = Card(value, suit)
                self.cards[suit].append(c)
        for ghost in GhostValues:
            c = Card(ghost)
            self.cards["Ghost"].append(c)

    def show(self):
        print("Normal cards:")
        for suit in CardSuits:
            print("Suit " + suit)
            for card in self.cards[suit]:
                print(card)
            print("=" * 80)
        print("Ghost Cards:")
        for card in self.cards["Ghost"]:
            print(card)


if __name__ == '__main__':
    # c = Card("A", "Spades")
    # print(c)
    dect = Deck()
    dect.show()
