import card_class, random, AI

### Helper functions
def create_deck():
    suits = ["Cl", "Cu", "Co", "Sw"]
    number = range(1, 11)
    deck = []
    for suit in suits:
        for num in number:
            deck.append(card_class.Bcard(suit, num))  
    return deck

def compare_cards(card1, card2, trump_suit):
    card_suits = [card1.suit, card2.suit]
    trump_match = [card_suits[0] == trump_suit, card_suits[1] == trump_suit]
    trues = trump_match.count(True)

    if trues == 1: # Trump card wins
        if trump_match.index(True) == 0:
            return "player1"
        else:
            return "player2"

    else: # Higher value card wins
        values = [card1.card_value(), card2.card_value()]
        if values[0] > values[1]:
            return "player1"
        elif values[0] < values[1]:
            return "player2"
        else:
            return "player1"
        


### Main game
def briscola_auto(player1_AI, player2_AI, debug = False):
    deck = create_deck()
    random.shuffle(deck)

    # Draw and determine the trump
    trump_card = deck.pop()
    trump_suit = trump_card.suit

    # Each player draws their initial 3
    p1_hand = [deck.pop(), deck.pop(), deck.pop()]
    p2_hand = [deck.pop(), deck.pop(), deck.pop()]

    # Setup player 1 and 2
    player1 = player1_AI
    player2 = player2_AI
    player1.set_trump(trump_suit)
    player2.set_trump(trump_suit)
    player1.starting_hand(p1_hand)
    player2.starting_hand(p2_hand)

    # Setup player 1 and 2's cards taken
    player1_stack = []
    player2_stack = []

    # Debug stuff
    current_round = 1

    while True:

        # P1 goes first
        player1.set_turn("first")
        player2.set_turn("second")

        p1_played_card = player1.play_card()
        player2.set_revealed_card(p1_played_card)
        p2_played_card = player2.play_card()

        winner = compare_cards(p1_played_card, p2_played_card, trump_suit)
        if winner == "player1":
            player1_stack.extend([p1_played_card, p2_played_card])
        else:
            player2_stack.extend([p1_played_card, p2_played_card])

        # Draw cards if possible
        if len(deck) > 1: # Normal
            card1 = deck.pop()
            card2 = deck.pop()
            player1.add_card(card1)
            player2.add_card(card2)
        elif len(deck) == 1: # If we're down to 1 card
            if winner == "player1":
                player1.add_card(deck.pop())
                player2.add_card(trump_card)
            else:
                player1.add_card(trump_card)
                player2.add_card(deck.pop())
        
        # If neither player has any cards in hand, break out of the loop
        if len(player1.hand) == 0:
            break
        
        if debug:
            print("Current round: " + str(current_round) + ", Winner = " + winner)
            current_round += 1

        # P2 goes first
        player2.set_turn("first")
        player1.set_turn("second")

        p2_played_card = player2.play_card()
        player1.set_revealed_card(p2_played_card)
        p1_played_card = player1.play_card()

        winner = compare_cards(p1_played_card, p2_played_card, trump_suit)
        if winner == "player1":
            player1_stack.extend([p1_played_card, p2_played_card])
        else:
            player2_stack.extend([p1_played_card, p2_played_card])

        # Draw cards if possible
        if len(deck) > 1: # Normal
            player1.add_card(deck.pop())
            player2.add_card(deck.pop())
        elif len(deck) == 1: # If we're down to 1 card
            if winner == "player1":
                player1.add_card(deck.pop())
                player2.add_card(trump_card)
            else:
                player1.add_card(trump_card)
                player2.add_card(deck.pop())

        # If neither player has any cards in hand, break out of the loop
        if len(player1.hand) == 0:
            break

        if debug:
            print("Current round: " + str(current_round) + ", Winner = " + winner)
            current_round += 1

    player1_values = []
    player2_values = []

    for c in player1_stack:
        player1_values.append(c.card_value())
    for c in player2_stack:
        player2_values.append(c.card_value())
    
    player1_score = sum(player1_values)
    player2_score = sum(player2_values)

    if player1_score > player2_score:
        if debug:
            print("Player 1 wins, " + str(player1_score) + " vs " + str(player2_score))
        return ["player1", player1_score, player2_score]
    elif player2_score > player1_score:
        if debug:
            print("Player 2 wins " + str(player1_score) + " vs " + str(player2_score))
        return ["player2", player1_score, player2_score]
    else:
        if debug:
            print("Tie game")
        return ["tie", player1_score, player2_score]


if __name__ == "__main__":
    a = AI.big_spender()
    b = AI.big_spender()
    result = briscola_auto(a, b, True)
    print(result)