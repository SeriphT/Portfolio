import random

class Card(object):
    """  A PLAYING CARD
    This class builds a single card
    to build a card, call Card() and pass in a rank and suit
                    card1 = Card("A","s")
    """
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["♠","♥","♦","♣"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank +self.suit
        return rep

class Hand(object):
    """ A HAND OF CARDS
    creates a hand from cards generated by the Card class
    create a hand by calling Hand()
            hand = Hand()
    add a card to the hand using the .add() method
            hand.add()
    give a card by using the .give() method
            hand.give()
    clear the hand to empty using .clear() method
            hand.clear()
    """

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """ DECK OF CARDS
    to create a deck, call the Deck() class
    then use the populate method
            deck = Deck()
            deck.populate()
    shuffle using the .shuffle() method
            deck.shuffle()
    add a card to the deck using the .add() method from the Hand class
            deck.add()
    give a card by using the .give() method from the Hand class
            deck.give()
    clear the deck to empty using .clear() method from the Hand class
            deck.clear()
    deal cards to players using the .deal() method
            deck.deal()
    """


    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Positional_Card(rank,suit,False))

    def shuffle(self):
        import random
        print("Shuffling...")
        random.shuffle(self.cards)


    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("No cards left to deal from the deck!")

class Unprintable_Card(Card):
    """A CARD THAT WON'T REVEAL THE SUIT OR RANK WHEN PRINTED"""
    def __str__(self):
        return "XX"

class Positional_Card(Card):
    """ A SINGLE CARD
    Builds a card that when given a true or false
    parameter, shows the rank and suit of a card.
    Create a deck of cards you can see by using the deck.populate() method
            deck.populate()
        ** change the parameter to true to show the cards or false to hide the cards values **
    A deck of hidden cards will show as XX
    A deck of shown cards will show Rank + Suit
    """
    def __init__(self, rank, suit, face_up = True):
        super(Positional_Card, self).__init__(rank,suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super(Positional_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up