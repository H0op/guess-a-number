"""Simple guess a number game that has randomly selected numbers
"""
import random

number = random.randrange(1,100)
check="wrong"

print("Welcome to Guess a number game!")

while check == "wrong":
    response = input("Please choose a number between 1 and 100: ")
    try:
        val = int(response)
    except ValueError:
        print("This is not a valid number. Please try again")
        continue
    if val < number:
        print("This is lower than actual number. Please try again.")
    elif val > number:
        print("This is higher than actual number. Please try again.")
    else:
        print("This is the correct number")
        check="correct"

print("Thank you for playing my guessing game. See you again")