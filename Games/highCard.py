# high card
# Feb. 13, 2019

import games, random, cards

deck = cards.Deck()
deck.populate()
deck.shuffle()
deck.shuffle()

print("Welcome to High Card!\n")

again = "y"
while again != "n":
    players = []
    num = games.ask_number("How many players?(2-10)", 2, 11)
    for i in range(num):
        name = input("Player name:")
        player = games.Player(name)
        players.append(player)
    hands = []
    for player in players:
        hand = player.hand
        hands.append(hand)
    deck.deal(hands,1)
    print("Results:")
    for player in players:
        print(player)
    again = games.ask_yes_no("\nPlay again? (y/n)")
input("Press enter to exit")
