# deck_of_cards
This is a simple python module that allows you to make a deck of cards.
Please keep in mind that this is still in development and feel free to suggest any changes and/or improvements.

To create a deck of poker cards:
sample_deck = deck_of_cards()

To create a special/unique deck use:
sample_deck.card_numbers = ['a','1', '2', '3', '4', '5', '6', '7', '8', '9',
                            '10', 'j', 'q', 'k']  #for the card values
sample_deck.card_types = ['C', 'D', 'H', 'S']          #for the card colors

If you make a custom deck use the make_deck() method after to create a deck of these cards:
sample_deck.make_deck()

To shuffle a deck use shuffle_deck() - for example:
sample_deck.shuffle_deck()

You can also specify the amount a deck should be shuffled by adding a kwarg - no_of_shuffles:
sample_deck.shuffle_deck(no_of_shuffles=9)

