﻿# -*- coding：utf-8 -*-
import random
from cards import Card
#其实更好的方法是，import method ，然后通过method.XXX()去调用函数呢

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
            print "\nComputer played ", card.short_name
            print "Up card: ", up_card.short_name
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
            print "Suit is", active_suit
            
        
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
            options.remove(best_play)
            best_play = up_card
            active_suit = up_card.suit
        print "\nComputer played ", best_play.short_name
                        

    else:
        if len(deck) > 0:
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print "\nComputer drew a card"
            
        else:
            print "Computer is blocked"
            blocked += 1
    print "Computer has %i cards left"  %(len(c_hand))
    #print("Suit is ",active_suit)
    print "Up card:",up_card.short_name


def player_turn():
    global deck, p_hand, blocked, up_card, active_suit
    print "What would you like to do? ",
    response = raw_input("\nType a card name to play or 'Draw' to take a card: ")
    is_eight = False
    ## play or draw a card
    valid_play = False
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
                    print "\nYour hand: "
                    for card in p_hand:
                        print card.short_name,
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
                        
                if selected_card.rank == '8':
                    valid_play = True
                    is_eight = True
                    get_new_suit()
                    p_hand.remove(selected_card)
                    up_card = selected_card
  
 
                    print "You played:",selected_card.short_name
                    print "\nYour hand："
                    for card in p_hand:
                        print card.short_name,
                    
                
                elif selected_card.suit == active_suit:
                    valid_play = True
                    p_hand.remove(selected_card)
                    up_card = selected_card
                    up_card.suit = active_suit
 
                    print "You played:",selected_card.short_name

                    print "\nYour hand："
                    for card in p_hand:
                        print card.short_name, 
                    #print "\nSuit is ",up_card.suit


                elif selected_card.rank == up_card.rank:
                    valid_play = True
                    p_hand.remove(selected_card )
                    up_card = selected_card
                    up_card.suit = active_suit
                    print "You played:",selected_card.short_name
                    print"\nYour hand："
                    for card in p_hand:
                        print card.short_name, 
                    print "\nSuit is",up_card.suit
                else:
                    if not valid_play:
                        response = raw_input("That's not a legal play. Try again: ")
 

                

def init_cards():
    global deck, up_card, active_suit, p_hand, c_hand
    for suit_id in range(1, 5):
        for rank_id in range(1, 14):
            new_card = Card(suit_id, rank_id)
            if new_card.rank_id == 8:
                new_card.value = 50
            deck.append(new_card)
 
    if up_card == []:
       up_card = random.choice(deck)
       deck.remove(up_card)
       active_suit = up_card.suit
    else:
        up_card = up_card[-1]
  
 
    if p_hand == []: 
        for i in range(1,6):       
            a = random.choice(deck)
            p_hand.append(a)
            deck.remove(a)
        
    if c_hand == []:
        for i in range(1,6): 
            b = random.choice(deck)
            c_hand.append(b)
            deck.remove(b)

    print "\nYour hand:"
    for card in p_hand:
        print card.short_name, 
    print "  Up card: ", up_card.short_name
    print "active_suit: ",active_suit
    #print"\nComputer hand:"
    #for card in c_hand:
        #print card.short_name,
deck = []
p_hand = []
c_hand = []
up_card = []
blocked = 0
done = False
p_total = c_total = 0
while not done:
    game_done = False
    while not game_done:
        init_cards()
        player_turn()
        if len(p_hand) == 0:
            game_done = True
            print "You won !"
        if not game_done:
            computer_turn()
        if len(c_hand) == 0:
            game_done = True
            print "Computer won! "
            #display the game score here
        if blocked >= 2:
                game_done = True
                print "Both player blocked, GAME OVER."
    player_points = 0
    for card in c_hand:
        p_points += card.value
    p_total += p_points
    c_points = 0
    for card in p_hand:
        c_point += card.value
    c_total += c_points
    print "You got %i points for computer's hand" % p_points
    print "Computer got %i points for your hand" % c_points


    play_again = raw_input("play again (Y/N)? ")
    if play_again.lower().startswith('y'):
        done = False
        print"\nSo far,you have %i points" % p_total
        print"\nand the computer has %i points." % c_total
    else:
        done = True
print "\nFinal Score:"
print "You: %i Computer: %i" %(p_total, c_total)



