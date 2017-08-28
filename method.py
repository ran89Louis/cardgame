def get_new_suit():
    global active_suit
    got_suit = False
    while not got_suit:
        suit = raw_input("Pick a suit: ")
        if suit.lower() == 'd':
            active_suit = "Diamonds"
            got_suit = True
        elif suit.lower() == 's':
            active_suit = "Spades"
            got_suit = True
        elif suit.lower() == 'h':
            active_suit = "Hearts"
            got_suit = True
        elif suit.lower() == 'c':
            active_suit = "Clubs"
            got_suit = True
        else:
            print "Not a valid suit.  Try again."
    print "You picked ", active_suit

def  computer_turn():
    global c_hand, deck, up_card, active_suit, blocked
    options = []
    for card in c_hand:
        if card.rank == '8':
            c_hand.remove(card)
            up_card = card
            print "  Computer played ", card.short_name
            #suit totals: [diamonds, hearts, spades, clubs]

            suit_totals = [0, 0, 0, 0]
            for suit in range(1, 5):
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit-1] += 1
            long_suit = 0
            for i in range(4):
                if suit_totals[i] > long_suit:
                    long_suit = i
            if long_suit == 0:  active_suit = "Diamonds"
            if long_suit == 1:  active_suit = "Hearts"
            if long_suit == 2:  active_suit = "Spades"
            if long_suit == 3:  active_suit = "Clubs"
            return
        else:
            if card.suit == active_suit:
                options.append(card)
            elif card.rank == up_card.rank:
                options.append(card)

    if len(options) > 0:
        best_play = options[0]
        for card in options:
            if card.value > best_play.value:
                best_play = card

        c_hand.remove(best_play)
        up_card = best_play
        active_suit = up_card.suit
        print "  Computer played ", best_play.short_name

    else:
        if len(deck)> 0:
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print "   Computer drew a card"
        else:
            print "Computer is blocked"
            blocked += 1
    print "Computer has %i cards left"  %(len(c_hand))


def player_turn():
    global deck, p_hand, blocked, up_card, active_suit
    print "What would you like to do? ",
    response = raw_input("Type a card name to play or 'Draw' to take a card: ")
    valid_play = False
    is_eight = False
    while not valid_play:
        selected_card = None
        while selected_card == None:
            if response.lower() == 'draw':
                valid_play = True
                if len(deck) > 0:
                    card = random.choice(deck)
                    p_hand.append(card)
                    deck.remove(card)
                    print "You drew", card.short_name
                else:
                    print "There are no cards left in the deck"
                    blocked += 1
                    break
            else:
                for card in p_hand:
                    if response.upper() == card.short_name:
                        selected_card = card
                    if selected_card == None:
                        response = raw_input("You don't have that card. Try again:")
                    print"\nYour hand: ",
                    for card in p_hand:
                        print card.short_name,
                    print "    Up card: ", up_card.short_name
                    
                    if up_card.rank == '8':
                        print"   Suit is", active_suit
                    print "What would you like to do? ",
                    response = raw_input("Type a card name to play or 'Draw' to take a card: ")
