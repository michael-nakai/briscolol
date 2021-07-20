import card_class, random

### A COUPLE OF GUIDELINES
#
# For all AI, they should have the following methods: 
#   AI_name should return a string of the name of the AI
#   set_turn sets the turn to either "first" or "second"
#   set_revealed_card sets revealed_card to the card played by the opponent
#   starting_hand should take a list of card objects, and should create the AI's hand
#   set_trump should take a suit string, and should overwrite trump_suit
#   add_card should take a card object and add a card to the AI's hand
#   play_card should return the card to be played, and the AI's hand should now lack the played card


### AI

# AI = big_spender
# Plays the highest value card each turn. 
# If there's a tie, it plays the trump suit. If it doesn't have the trump suit, then it plays the one leftmost in the hand.

class big_spender:
    def __init__(self, hand = [], trump_suit = "", turn = None, revealed_card = None):
        self.hand = hand
        self.trump_suit = trump_suit
        self.turn = turn
        self.revealed_card = revealed_card

    def AI_name(self):
        return "big_spender"

    def set_turn(self, t):
        self.turn = t
    
    def set_revealed_card(self, revealed):
        self.revealed_card = revealed

    def starting_hand(self, h):
        self.hand = h

    def set_trump(self, trump):
        self.trump_suit = trump

    def add_card(self, x):
        self.hand.append(x)
    
    def play_card(self):
        value_list = []
        for c in self.hand:
            value_list.append(c.card_value())
        max_value = max(value_list)

        # If more than 1 card shares the max_value
        if value_list.count(max_value) > 1:
            index=0
            foundcard = False
            for c in self.hand:
                if c.suit != self.trump_suit:
                    index += 1
                else:
                    foundcard = True
            if foundcard:
                a = self.hand[index]
                del self.hand[index]
                return a
            else:
                i = value_list.index(max_value)
                a = self.hand[i]
                del self.hand[i]
                return a

        # If only one card has the max_value
        else:
            index = value_list.index(max_value)
            a = self.hand[index]
            del self.hand[index]
            return a



# AI = little_coward
# Plays the lowest value card each turn. 
# If there's a tie, it plays the trump suit. If it doesn't have the trump suit, then it plays the one leftmost in the hand.

class little_coward:
    def __init__(self, hand = [], trump_suit = "", turn = None, revealed_card = None):
        self.hand = hand
        self.trump_suit = trump_suit
        self.turn = turn
        self.revealed_card = revealed_card

    def AI_name(self):
        return "little_coward"

    def set_turn(self, t):
        self.turn = t
    
    def set_revealed_card(self, revealed):
        self.revealed_card = revealed

    def starting_hand(self, h):
        self.hand = h

    def set_trump(self, trump):
        self.trump_suit = trump

    def add_card(self, x):
        self.hand.append(x)
    
    def play_card(self):
        value_list = []
        for c in self.hand:
            value_list.append(c.card_value())
        min_value = min(value_list)

        # If more than 1 card shares the min_value
        if value_list.count(min_value) > 1:
            index=0
            foundcard = False
            for c in self.hand:
                if c.suit != self.trump_suit:
                    index += 1
                else:
                    foundcard = True
            if foundcard:
                a = self.hand[index]
                del self.hand[index]
                return a
            else:
                i = value_list.index(min_value)
                a = self.hand[i]
                del self.hand[i]
                return a

        # If only one card has the max_value
        else:
            index = value_list.index(min_value)
            a = self.hand[index]
            del self.hand[index]
            return a



# AI = randy_random
# Plays a random card each turn. Our control group.

class randy_random:
    def __init__(self, hand = [], trump_suit = "", turn = None, revealed_card = None):
        self.hand = hand
        self.trump_suit = trump_suit
        self.turn = turn
        self.revealed_card = revealed_card

    def AI_name(self):
        return "randy_random"
    
    def set_turn(self, t):
        self.turn = t
    
    def set_revealed_card(self, revealed):
        self.revealed_card = revealed

    def starting_hand(self, h):
        self.hand = h

    def set_trump(self, trump):
        self.trump_suit = trump

    def add_card(self, x):
        self.hand.append(x)
    
    def play_card(self):
        index = random.randrange(0, len(self.hand))
        a = self.hand[index]
        del self.hand[index]
        return a



# AI = little_opportunist
# Plays the lowest value card each turn, except when it is going second, in which case it tries to beat the card
# that the opponent played, first by suit, then by value.
# If there's a tie within its hand, it plays the trump suit. 
# If it doesn't have the trump suit, then it plays the one leftmost in the hand.

class little_opportunist:
    def __init__(self, hand = [], trump_suit = "", turn = None, revealed_card = None):
        self.hand = hand
        self.trump_suit = trump_suit
        self.turn = turn
        self.revealed_card = revealed_card

    def AI_name(self):
        return "little_opportunist"

    def set_turn(self, t):
        self.turn = t
    
    def set_revealed_card(self, revealed):
        self.revealed_card = revealed

    def starting_hand(self, h):
        self.hand = h

    def set_trump(self, trump):
        self.trump_suit = trump

    def add_card(self, x):
        self.hand.append(x)
    
    def play_card(self):
        value_list = []

        # Check if we have a card that beats theirs. If so, play it
        if self.turn == "second":
            if self.revealed_card.suit != self.trump_suit:
                value_list = []
                trump_suit_cardlist = []
                for c in self.hand:
                    value_list.append(c.card_value())
                    if c.suit == self.trump_suit:
                        trump_suit_cardlist.append(True)
                    else:
                        trump_suit_cardlist.append(False)
                true_count = trump_suit_cardlist.count(True)
                if true_count == 1: # If we have a trump suite and they don't, then we play it
                    index = trump_suit_cardlist.index(True)
                    a = self.hand[index]
                    del self.hand[index]
                    return a
                elif true_count > 1: # Find the lowest value within the Trues and play it
                    index = 0        # If there's a tie, then take the leftmost
                    min_card = min(value_list)
                    for bo in trump_suit_cardlist:
                        if bo and self.hand[index].card_value() == min_card:
                            a = self.hand[index]
                            del self.hand[index]
                            return a
                        else:
                            index += 1
                else: # Try and find any higher value card, otherwise play the lowest value card
                    max_card = max(value_list)
                    if max_card > self.revealed_card.card_value():
                        index = value_list.index(max_card)
                        a = self.hand[index]
                        del self.hand[index]
                        return a

            else: # Try and find a higher value card of the trump suit
                value_list = []
                card_list = []
                trump_suit_cardlist = []
                trump_cards = []
                for c in self.hand:
                    value_list.append(c.card_value())
                    card_list.append(c.card_combination())
                    if c.suit == self.trump_suit:
                        trump_suit_cardlist.append(True)
                        trump_cards.append(c)
                    else:
                        trump_suit_cardlist.append(False)
                if len(trump_cards) == 1 and trump_cards[0].card_value() > self.revealed_card.card_value(): # If we have one trump card that has a higher value, then we play it
                    index = self.hand.index(trump_cards[0])
                    a = self.hand[index]
                    del self.hand[index]
                    return a
                elif len(trump_cards) > 1: # If there's more than one card in the trump suit
                    trump_values = []
                    for z in trump_cards:
                        trump_values.append(z.card_value())
                    val_over_min = []
                    for z in trump_values:
                        if z > self.revealed_card.card_value():
                            val_over_min.append(z)
                    if len(val_over_min) > 0:
                        combo = self.trump_suit + str(min(val_over_min))
                        index = 0
                        for c in self.hand:
                            if c.card_combination() == combo:
                                a = self.hand[index]
                                del self.hand[index]
                                return a
                            else:
                                index += 1
                # Else we just default to the normal choice, and play the lowest value card as if we didn't see theirs
        for c in self.hand:
            value_list.append(c.card_value())
        min_value = min(value_list)

        # If more than 1 card shares the min_value
        if value_list.count(min_value) > 1:
            index=0
            foundcard = False
            for c in self.hand:
                if c.suit != self.trump_suit:
                    index += 1
                else:
                    foundcard = True
            if foundcard:
                a = self.hand[index]
                del self.hand[index]
                return a
            else:
                i = value_list.index(min_value)
                a = self.hand[i]
                del self.hand[i]
                return a

        # If only one card has the max_value
        else:
            index = value_list.index(min_value)
            a = self.hand[index]
            del self.hand[index]
            return a