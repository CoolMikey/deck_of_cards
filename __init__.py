'''
This module is used to create a deck of cards and allows the basic modification
of it.
'''
try:
    import random
except ImportError:
    print("Can't import random, shuffle won't work.")


class deck_of_cards:
    # "clubs (♣), diamonds (♦), hearts (♥) and spades (♠)" - if you
    # are like me and can't remember the names

    def __init__(self, **kwargs):

        self.deck_type = str(kwargs.get('type', "poker"))
        self.show_cards_after_each_step = int(kwargs.get('show_cards', "0"))
        self.deck = []
        self.no_of_shuffles = "1"
        self.card_types = []
        self.card_numbers = []
        if self.deck_type == "poker":
            self.card_types = ['C', 'D', 'H', 'S']
            self.card_numbers = ['a', '1', '2', '3', '4', '5', '6', '7', '8',
                                 '9', '10', 'j', 'q', 'k']
            self.make_deck()
        else:
            print("Warning - NO card types and numbers were assigned")
            return None

        if self.show_cards_after_each_step == 1:
            print(self.deck)

    def return_deck(self):
        return self.deck

    def make_deck(self):
        for type in self.card_types:
            for card_number in self.card_numbers:
                self.deck.append(type+card_number)
        if self.show_cards_after_each_step == 1:
            print("New deck created:", self.deck)

    def shuffle_deck(self, **kwargs):
        if len(self.deck) > 0:
            self.no_of_shuffles = int(kwargs.get('no_of_shuffles', "1"))
            for shuffle in range(self.no_of_shuffles):
                new_deck = []
                for i in range(len(self.deck)):
                    chosen_number = random.randrange(len(self.deck))
                    new_deck.append(self.deck[chosen_number])
                    self.deck.pop(chosen_number)
                self.deck = new_deck
        else:
            print("Deck empty.")
        if self.show_cards_after_each_step == 1:
            print(self.deck)
