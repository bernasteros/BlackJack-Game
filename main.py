from os import name, system
from random import choice
from cards import card_value, deck
from art import logo

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def deal(deck):
    return choice(deck)

def check_score(hand):
    score = 0
    for card in hand:
        score += card_value[card]

    if "A" in hand and score > 21:
        score -= 10
    return score

def show_result():
    print(f"Player Hand: {' - '.join(p_deck)}\nPlayer Score: {p_score}")
    print((f"\nDealer Hand: {' - '.join(c_deck)}\nActual Score: {c_score}"))

print(logo)
while input("Play a new round of Blackjack? (y/n) > ").lower() == "y":
    clear()
    print(logo)
    p_deck = []
    c_deck = []
    p_score = 0
    c_score = 0
    
    for i in range(2):
        p_deck.append(deal(deck))
    p_score = check_score(p_deck)
    c_deck.append(deal(deck))
    c_score = check_score(c_deck)

    show_result()

    c_deck.append(deal(deck))
    c_score = check_score(c_deck)

    while p_score < 21 and input("Take another card? (y/n) > ").lower() == "y":
        p_deck.append(deal(deck))
        p_score = check_score(p_deck)
        if c_score < 17:
            c_deck.append(deal(deck))
            c_score = check_score(c_deck)
        clear()
        print(logo)
        show_result()
    
    while c_score < 17:
        c_deck.append(deal(deck))
        c_score = check_score(c_deck)

    if p_score > c_score and p_score < 21:
        clear()
        print(logo)
        print("PLAYER WINS!\n")
        show_result()

    elif p_score == 21:
        clear()
        print(logo)
        print("BLACKJACK!\n")
        show_result()

    elif p_score > 21:
        clear()
        print(logo)
        print("BUSTED! - DEALER WINS\n")
        show_result()

    elif p_score < c_score and c_score > 21:
        clear()
        print(logo)
        print("PLAYER WINS\n")
        show_result()  
    elif p_score == c_score:
        clear()
        print(logo)
        print("IT'S A DRAW\n")
        show_result()
    else:
        clear()
        print(logo)
        print("DEALER WINS\n")
        show_result()  

print("\nThank you for playing :)")