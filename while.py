import random
card_pack = [
    "Ace Of Spades",
    "2 Of Spades",
    "3 Of Spades",
    "4 Of Spades",
    "5 Of Spades",
    "6 Of Spades",
    "7 Of Spades",
    "8 Of Spades",
    "9 Of Spades",
    "10 Of Spades",
    "Jack Of Spades",
    "Queen Of Spades",
    "King Of Spades",
    "Ace Of Hearts",
    "2 Of Hearts",
    "3 Of Hearts",
    "4 Of Hearts",
    "5 Of Hearts",
    "6 Of Hearts",
    "7 Of Hearts",
    "8 Of Hearts",
    "9 Of Hearts",
    "10 Of Hearts",
    "Jack Of Hearts",
    "Queen Of Hearts",
    "King Of Hearts",
    "Ace Of Clubs",
    "2 Of Clubs",
    "3 Of Clubs",
    "4 Of Clubs",
    "5 Of Clubs",
    "6 Of Clubs",
    "7 Of Clubs",
    "8 Of Clubs",
    "9 Of Clubs",
    "10 Of Clubs",
    "Jack Of Clubs",
    "Queen Of Clubs",
    "King Of Clubs",
    "Ace Of Diamonds",
    "2 Of Diamonds",
    "3 Of Diamonds",
    "4 Of Diamonds",
    "5 Of Diamonds",
    "6 Of Diamonds",
    "7 Of Diamonds",
    "8 Of Diamonds",
    "9 Of Diamonds",
    "10 Of Diamonds",
    "Jack Of Diamonds",
    "Queen Of Diamonds",
    "King Of Diamonds",
    "Joker"
]
rand_card = random.choice(card_pack)
my_card = "King Of Spades"
while rand_card != my_card:
    print(rand_card)
    rand_card = random.choice(card_pack)
print("you've found the {}".format(my_card))
