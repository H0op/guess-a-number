"""Simple guess a number game that has randomly selected number
"""

from random import randint  #To generate a random number
name = input("Hello! What is your name? ")
print("\nWelcome to Guess a number game "+name)

def game():
    """prints and runs our guessing game
    """    
    rand_number = randint(1,100)   #Generates a random number
    print("You have 6 chances to guess the number...")
    print('Well, ' + name + ', I am thinking of a number between 1 and 100')
    i = 0
    while i<6:  #6 Chances to the user
        try:
            user_number = int(input('\nTake a guess: '))
        except ValueError:
            print("This is not a valid number. Please try again")
            continue
        if user_number < 1 or user_number > 100: #make it when its <0 or >100
            print("This is an invalid number. Please try again")
            continue
        elif user_number < rand_number:
            print("\n" + name + ", my number is actual greater than your guessed number")
            i = i+1
        elif user_number > rand_number:
            print("\n" + name + ", my number is lower than your guessed number")
            i = i+1
        elif user_number == rand_number:
            print("\nCongratulations " + name + "!! You have guessed the correct number!")
            print(f"It took you {i} tries")
            break
        
        print("You now have " + str(6-i)+ " chances left" )
    if i==0:
        print("Sorry you lost the game!!")
        print("The number I was thinking of was " + str(rand_number))

def main():
    """keeping game in a loop and runs game()
    """    
    game()
    while True:
        another_game = input("Do you wish to play again?(y/n): ")
        if another_game == "y":
            game()
        else:
            break
main()
print(f"\nThank you for playing my guessing game {name}. See you again")