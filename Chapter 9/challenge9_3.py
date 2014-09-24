"""
Program......: challenge9_3.py
Author.......: Michael Rouse
Date.........: 2/24/14
Description..: Add betting into the blackjack program
"""

import cards, games     

class BJ_Card(cards.Card):
    """ A Blackjack Card. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """ A Blackjack Deck. """
    def populate(self):
        for suit in BJ_Card.SUITS: 
            for rank in BJ_Card.RANKS: 
                self.cards.append(BJ_Card(rank, suit))
    

class BJ_Hand(cards.Hand):
    """ A Blackjack Hand. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
        self.funds = 50 # Amount of dollars the player has to start

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()  
        if self.total:
            rep += "(" + str(self.total) + ")"        
        return rep

    @property     
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None
        
        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
              t += card.value

        # determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
                
        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10   
                
        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    """ A Blackjack Player. """
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", you have " + str(self.total) + " do you want a hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self, winningPot):
        print(self.name, "wins.")
        self.funds += winningPot

    def push(self):
        print(self.name, "pushes.")

    def bet(self):
        notValid = True
        while notValid:
            bet = input(self.name + "'s bet (You have $" + str(self.funds) + "): $")
            try:
                bet = int(bet)

                if self.funds == 0 and bet != 0:
                    notValid = False
                elif bet <= self.funds and bet!= 0:
                    notValid = False
            except:
                notValid = True
        
        self.funds -= bet
        
        return bet
        
class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """ A Blackjack Game. """
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.winningPot = 0

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            # Check if there are enough cards
            self.checkCardCount(cardsNeeded=1)
            
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    # Get player's bets
    def place_bets(self):
        for player in self.players:
            self.winningPot += player.bet()

        print("\nThe global pot is: $" + str(self.winningPot) + "\n")
        
    # Check if there are enough cards
    def checkCardCount(self, cardsNeeded):
        if len(self.deck.cards) < (cardsNeeded):
            # Not enough cards, reshuffle them
            print("Not enough cards, repopulating deck")
            self.deck.populate()
            self.deck.shuffle()
        
    def play(self):
        self.place_bets()
            
        # Check if there are enough cards
        cardsNeeded = ((len(self.players) + 1) * 2)
        self.checkCardCount(cardsNeeded)
            
        # deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()    # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    # reveal dealer's first 

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win(self.winningPot)                    
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win(self.winningPot)
                        self.winningPot = 0
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()

def ask_number(question, low=1, high=7):
    notValid = True
    while notValid:
        number = input(question)

        try:
            number = int(number)
            if number in range(low, high+1):
                notValid = False # Input is valid
        except:
            notValid = True

    return int(number)
            

def main():
    print("\t\tWelcome to Blackjack!\n")
    
    names = []
    number = ask_number("How many players? (1 - 7): ", low=1, high=7)
            
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()
        
    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nPress the enter key to exit.")



