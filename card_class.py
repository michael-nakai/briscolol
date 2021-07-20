### Helper functions
def short_to_long_suit(short_suit):
    if short_suit == "Cl":
        return "Clubs"
    elif short_suit == "Cu":
        return "Cups"
    elif short_suit == "Co":
        return "Coins"
    else:
        return "Swords"

def find_value(number):
    if number == 2:
        return 0
    elif number == 1:
        return 11
    elif number == 3:
        return 10
    elif number == 8:
        return 2
    elif number == 9:
        return 3
    elif number == 10:
        return 4
    else:
        return 0


### Classes
class Bcard:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def suit_full(self):
        return short_to_long_suit(self.suit)
    
    def card_value(self):
        return find_value(self.number)

    def card_combination(self):
        return self.suit + str(self.number)
    
    # Might be bugged, dunno
    def print_card_short(self):
        print(self.suit + str(self.number))