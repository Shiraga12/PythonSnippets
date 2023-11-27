import random

def rps():
    strat = ["R","P","S"]
    com_move = '';
    player_move = '';
    
    while player_move != 'Q':
        com_move = random.choice(strat)
        player_move = input("Make your move! (R)ock (P)aper or (S)cissors? (Q)uit to stop playing.")
    
        if com_move == strat[0]: #    Rock
            print("Computer Choses Rock!\n")
            if player_move == "R":
                print("It's a tie!")
            elif player_move == "S":
                print("Computer Player Wins!\nUser Player Loses...")
            elif player_move == "P":
                print("User Player Wins!\nComputer Player Loses...")
        elif com_move == strat[1]: #  Paper
            print("Computer Choses Paper!\n")
            if player_move == "R":
                print("Computer Player Wins!\nUser Player Loses...")
            elif player_move == "S":
                print("User Player Wins!\nComputer Player Loses...")
            elif player_move == "P":
                print("It's a tie!")
        elif com_move == strat[2]: #  Scissors
            print("Computer Choses Scissors!\n")
            if player_move == "R":
                print("User Player Wins!\nComputer Player Loses...")
            elif player_move == "S":
                print("It's a tie!")
            elif player_move == "P":
                print("Computer Player Wins!\nUser Player Loses...")

rps()
