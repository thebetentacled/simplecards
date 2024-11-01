# little card game by thebetentacled
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.

# imports

import pygame
import random

# pygame setup

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # RENDER YOUR GAME HERE

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# global variables

playercash = 20

dealercash = 20


# functions

def printrules():
    print("welcome to my simple card game")
    print("there's seven cards, don\'t pull a four!")
    print("rule 1: if you bet on a card and it isn't pulled, you lose your bet to the dealer.")
    print("rule 2: if you bet on a card and it's pulled, you take your bet from the dealer.")
    print("rule 3: if the dealer takes all your cash, you lose.")
    print("rule 4: if you take all the dealer's cash, you win.")
    print("rule 5: if you pull a seven, you take $5 from the dealer.")
    print("rule 6: if you pull a four, the dealer takes $5 from you, but not your bet.")
    
def betandpull():
    global playercash
    global dealercash
    cardguess = 0
    print("you have $", playercash)
    print("dealer has $", dealercash)
    cardguess = int(input("what card will be pulled (1-7)? \n  --> "))
    playerbet = int(input("how much will you bet on that? (exclude dollar sign) \n  --> "))
    cardpull = random.randint(1, 7)
    print(cardpull, "was pulled")
    if cardpull == 7:
        dealercash = dealercash - 5
        playercash = playercash + 5
    elif cardpull == 4:
        playercash = playercash - 5
        dealercash = dealercash +5
    elif cardpull == cardguess:
        dealercash = dealercash - playerbet
        playercash = playercash + playerbet
    else:
        playercash = playercash - playerbet
        dealercash = dealercash + playerbet

    if playercash <= 0:
        print("you lose")
        exit()
    elif dealercash <= 0:
        print("you win")
        exit()
    else:
        betandpull()
        

def main():
    printrules()
    betandpull()

# main() call

main()
    
