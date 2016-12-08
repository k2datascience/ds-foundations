# Blackjack Game

# Create deck and deal cards
# Check hand total
# Decide to hit or stay
# Dealer logic
# Compare hands and decide winner

# Imports
import itertools
from random import shuffle

# Helper Functions
def calculate_total(cards):
    total = 0
    for (suit, value) in cards:
        if value == 'A':
            total += 11
        elif value in ['J', 'Q', 'K']:
            total += 10
        else:
            total += int(value)

    # Aces Logic
    aces = sum(card.count("A") for card in cards)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

# Start Game
print("Welcome to Blackjack!")

suits = ['H', 'D', 'S', 'C']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = list(itertools.product(suits, cards))
shuffle(deck)
# print(deck)

# Deal Cards
player_hand = []
dealer_hand = []

player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

dealer_total = calculate_total(dealer_hand)
player_total = calculate_total(player_hand)

# Show Cards
print("Dealer has: Hidden and {0}.".format(dealer_hand[1]))
print("You have: {0} and {1}, for a total of {2}. \n".format(player_hand[0], player_hand[1], player_total))

# Check if there is a winner
if player_total == 21 and dealer_total == 21:
    print("It's a push. House wins. Sorry.")
    quit()
elif player_total == 21:
    print("Congratulations, you hit Blackjack! You win!")
    quit()
elif dealer_total == 21:
    print("Sorry, dealer hit Blackjack. You lose.")
    quit()
else:
    pass

# Player Turn
while player_total < 21:
    hit_or_stay = input("What would you like to do? 1) Hit 2) Stay    ")

    if hit_or_stay not in ['1', '2']:
        print("Error: You must enter 1 or 2.")
        continue
    elif hit_or_stay == "2":
        print("You chose to stay.")
        break
    else:
        new_card = deck.pop()
        print("Dealing card to player: {0}".format(new_card))
        player_hand.append(new_card)
        player_total = calculate_total(player_hand)
        print("Your total is now: {0}".format(player_total))

        if player_total == 21:
            print("Congratulations, you hit Blackjack! You win!")
            quit()
        elif player_total > 21:
            print("Sorry, you busted!")
            quit()
        else:
            continue

# Dealer Turn
while dealer_total < 17:
    new_card = deck.pop()
    print("Dealing card to dealer: {0}".format(new_card))
    dealer_hand.append(new_card)
    dealer_total = calculate_total(dealer_hand)
    print("Dealer's total is now: {0}".format(dealer_total))

    if dealer_total == 21:
        print("Sorry, dealer hit Blackjack. You lose.")
        quit()
    elif dealer_total > 21:
        print("Congratulations, dealer busted! You win!")
        quit()
    else:
        continue

# Compare Hands
print("Dealer's cards: ")
for card in dealer_hand:
    print(card)
print("")

print("Your cards: ")
for card in player_hand:
    print(card)
print("")

if dealer_total > player_total:
    print("Sorry, dealer wins.")
elif dealer_total < player_total:
    print("Congratulations, you win!")
else:
    print("It's a tie")

quit()



# Additional features
# - Betting
# - Smarter Dealer
# - Total counting via cards
# - Splits, etc.
