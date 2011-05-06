#!/usr/bin/env python
"""
Sneaky Hunt the Wumpus!
"""
import random

# All the possible directions
all_directions = ['n', 's', 'e', 'w']

# The number of turns until you find the Wumpus!
turns_to_victory = random.randint(7, 12)

# How likely (out of 10) you are to hear the Wumpus
chance_hear_wumpus = 3

# Main game loop
for x in range(turns_to_victory):
    if x == 0:
        print "You are in a maze of twisty passages, all alike. Where's the"\
           " Wumpus..?"
    else:
        print "You are in yet another dark mysterious room."
    random.shuffle(all_directions)
    how_many = random.randint(2, 4)
    exits = sorted(all_directions[:how_many])
    while True:
        choice = raw_input("Which direction " + str(exits) + "? ").lower()
        if choice in exits:
            break
        else:
            print "Can't go that way..."
    wumpus_close = random.randint(0, 10)
    if chance_hear_wumpus <= wumpus_close and not x == turns_to_victory:
        print "You hear the Wumpus...."
print "You found the Wumpus! Well done!"
