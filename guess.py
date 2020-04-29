"""Simple guess a number game that has randomly selected number
"""

from random import randint #To generate a random number

def gameMenu(name) : 
    """Display initial menu to user"""

    print(f'Ready to play {name} ...?')
    menuChoice = ""
    menuChoice = input('Press Y to start game, or X to quit.\n\n').upper()
    menuLoop = True

    while menuLoop :

        clearConsole(0)

        if menuChoice == "Y" :
            clearConsole(0)
            playGame(name)
        elif menuChoice == "X" :
            clearConsole(0)
            print(f"\nThank you for playing my guessing game {name}. See you again")
            break
        else :
            print("This is not a valid input. Please try again")
            gameMenu(name)

    
def playGame(name) :
    """Obtain input from user, check against random number and display output"""

    intLower = 1 #default set to 0
    intHigher = 100 #default set to 1000
    rndNumber = 0
    guesses = 0 #number of tries/guesses
    rndNumber = randomNumber(intLower, intHigher)

    print('\nWell, I am thinking of a number between {0} and {1}'.format(intLower, intHigher))
    print("You have 6 chances to guess the number...")

    while guesses < 6:  #6 Chances to the user
        try:
            user_number = int(input(f'{name} please take a guess: '))
        except ValueError:
            clearConsole(1)
            print("This is not a valid number. Please try again")
            continue
        if user_number < 1 or user_number > 100: #make it when its <0 or >100
            clearConsole(1)
            print("This is an invalid number. Please try again")
            continue
        elif user_number < rndNumber:
            clearConsole(1)
            print("\nSorry, you didn't guess the number " + name + ", my number is actual greater than yours")
            guesses += 1
        elif user_number > rndNumber:
            clearConsole(1)
            print("\nSorry, you didn't guess the number " + name + ", my number is lower than yours")
            guesses += 1
        elif user_number == rndNumber:
            print("\nCongratulations " + name + "!! you have guessed the number!")
            print(f"It took you {guesses} tries")
            break
        
        print("You now have " + str(6-guesses)+ " chances left" )
    if guesses == 6:
        print("Sorry you lost the game!!")
        print("The number I was thinking of was " + str(rndNumber))
    print('Returning you to the menu...')
    clearConsole(3)
    gameMenu(name)

def randomNumber(a, b) :
    """Generates a random int from range a, b"""

    return(randint(a,b))

def clearConsole(wait) : #function to clear console on Linux or Windows
    """Clears console, with optional time delay.
    Will attempt to clear the console for Windows, should that fail it will attempt to clear the
    console for Linux.
    """

    import time
    import os
    time.sleep(wait) 
    # produces a delay based on the argument given to clearConsole()

    try :
       os.system('cls') #clears console on Windows
    except :
       os.system('clear') #clears console on Linux

def main() :
    """Display initial welcome message to user, spawn gameMenu()
    """    
    print('\nHello, welcome to Guess a number game!\n')
    name = input("What is your name? ")
    gameMenu(name)

if __name__ == "__main__" :
    main()