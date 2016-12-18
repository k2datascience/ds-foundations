import itertools
from random import shuffle

class Deck:
    """Create a deck to initialize cards and deal cards"""

    def __init__(self):
        suits = ['H', 'D', 'S', 'C']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        # Note - you could try to create a separate Card class, however, it does encapsulate any additional information or need specific methods aside from maybe mapping the full Suit name, so we left it simpler
        self.cards = list(itertools.product(suits, values))
        shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()

class Hand:
    """Create a hand to store cards and calculate the total"""

    def __init__(self):
        self.cards = []

    def total(self):
        total_value = 0
        for (suit, value) in self.cards:
            if value == 'A':
                total_value += 11
            elif value in ['J', 'Q', 'K']:
                total_value += 10
            else:
                total_value += int(value)

        # Aces
        aces = sum(card.count("A") for card in self.cards)

        while total_value > 21 and aces:
            total_value -= 10
            aces -= 1

        return total_value

    def add_card(self, new_card):
        self.cards.append(new_card)


class Player(Hand):
    """Create a player that inherits from the Hand. It has a custom show method."""

    def __init__(self, name):
        Hand.__init__(self)
        self.name = name

    def show_hand(self):
        print("--- {0}'s Hand ---".format(self.name))
        for card in self.cards:
            print("=> {0}".format(card))
        total = self.total()
        print("Your total is now: {0}".format(total))


class Dealer(Hand):
    """Create a dealer that inherits from the Hand. It has a custom show method."""

    def __init__(self, name = "Dealer"):
        Hand.__init__(self)
        self.name = name

    def show_flop(self):
        print("--- Dealer's Hand ---")
        print("=> First card is hidden")
        print("=> Second card is {0}".format(self.cards[1]))


class BlackJack:
    """Create a Blackjack clas to store all the gameplay methods"""

    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player 1")
        self.dealer = Dealer()
        self.blackjack_amount = 21
        self.dealer_hit_min = 17

    def set_player_name(self):
        self.player.name = input("Enter your name: ")

    def deal_cards(self):
        self.player.add_card(self.deck.deal_one())
        self.dealer.add_card(self.deck.deal_one())
        self.player.add_card(self.deck.deal_one())
        self.dealer.add_card(self.deck.deal_one())

    def show_flop(self):
        self.player.show_hand()
        self.dealer.show_flop()

    def is_busted(self, hand):
        return hand.total() > self.blackjack_amount

    def blackjack_or_bust(self, player_or_dealer):
        if player_or_dealer.total() == self.blackjack_amount:
            if isinstance(player_or_dealer, Dealer):
                print("Sorry, dealer hit Blackjack. You lose.")
                self.play_again()
            else:
                print("Congrats. {0} hit Blacjack. {0} wins!".format(self.player.name))
                self.play_again()

        elif self.is_busted(player_or_dealer):
            if isinstance(player_or_dealer, Player):
                print("Sorry, you busted. You lose.")
                self.play_again()
            else:
                print("Congrats, dealer busted. You win!")
                self.play_again()

    def play_again(self):
        choice = input("Would you like to play again? 1) Yes 2) No ")
        if choice == "1":
            print("Starting new game")
            self.deck = Deck()
            self.player.cards = []
            self.dealer.cards = []
            self.start()
        elif choice == "2":
            quit()

    def player_turn(self):
        print("It's {0}'s turn'".format(self.player.name))

        self.blackjack_or_bust(self.player)

        while not self.is_busted(self.player):
            hit_or_stay = input("What would you like to do? 1) hit 2) stay  ")

            if hit_or_stay not in ['1','2']:
                print("Error: you must enter 1 or 2")
                continue

            if hit_or_stay == "2":
                print("You chose to stay")
                break

            new_card = self.deck.deal_one()
            print("Dealing card to {0}: {1}".format(self.player.name, new_card))
            self.player.add_card(new_card)
            print("{0}'s total is now: {1}".format(self.player.name, self.player.total()))

            self.blackjack_or_bust(self.player)

    def dealer_turn(self):
        print("Dealer's Turn.")
        print("Dealer has: {0} and {1}".format(self.dealer.cards[0], self.dealer.cards[1]))

        self.blackjack_or_bust(self.dealer)

        while self.dealer.total() < self.dealer_hit_min:
            new_card = self.deck.deal_one()
            print("Dealing card to dealer: {0}".format(new_card))
            self.dealer.add_card(new_card)
            print("Dealer's total is now: {0}".format(self.dealer.total()))

        self.blackjack_or_bust(self.dealer)
        print("Dealer stays with: {0}".format(self.dealer.total()))
        self.who_won()

    def who_won(self):
        if self.dealer.total() > self.player.total():
            print("Sorry, dealer wins.")
        elif self.dealer.total() < self.player.total():
            print("Congratulations, you win!")
        else:
            print("It's a push. House wins. Sorry.")

        self.play_again()

    def start(self):
        self.set_player_name()
        self.deal_cards()
        self.show_flop()
        self.player_turn()
        self.dealer_turn()


game = BlackJack()
game.start()
