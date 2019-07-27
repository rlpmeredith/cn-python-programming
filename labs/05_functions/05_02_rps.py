'''
Code a game of rock paper scissors.

'''
Tested 27-7-19
import random

# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    # for example if the variable hand is 0, it should return the string "scissor"
    if hand == 0:
        return "scissor"
    elif hand == 1:
        return "rock"
    elif hand == 2:
        return "paper"


# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    if computer == player:
        return "You Tied!"
    elif player == "scissor" and computer == "paper":
        return "You Won"
    elif player == "rock" and computer == "scissor":
        return "You Won"
    elif player == "paper" and computer == "rock":
        return "You Won"
    else:
        return "You Lost"
'''
Start here:
'''

# take in a number 0-2 from the user that represents their hand

user_hand = int(input("Enter your hand: "))

# generate a random number 0-2 to use for the computer's hand

comp_hand = random.randint(0, 2)

# call the function get_hand to get the string representation of the user's hand

user_hand_str = get_hand(user_hand)

# call the function get_hand to get the string representation of the computer's hand

comp_hand_str = get_hand(comp_hand)

# call the function determine_winner to figure out the winner

winner = determine_winner(comp_hand_str, user_hand_str)

# print out the player hand and computer hand

print(f"Computer hand is {comp_hand_str} Player Hand is {user_hand_str}")

# print out the winner

print(winner)