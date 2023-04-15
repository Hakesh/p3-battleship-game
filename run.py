from words_list import words
from hangman_ascii import hangman
import os
import random

def enter_username():
    """
    This functions lets the user type in a username and makes sure that it follows the requirements to continue
    or they will be asked to try again until it is valid
    """
    
    global username
    username = ""
    while True:
        print("-" * 79)
        username = input("Please enter a username to continue: ")
        username = username.capitalize()

        if username.isalpha() and len(username) >= 2 and len(username) <= 10:
            clear_terminal()
            print("-" * 79)
            print(f"Hello, {username}!\n\n\nLets play a game of Hangman, shall we?")
            print(hangman[8])
            break
                
        else:
            print(f'\nUsername "{username}" is invalid. Please make sure that: \n')
            print("    1. That there is no spaces in your username")
            print("    2. That the name is between 2-10 letters")
            print("    3. That there is no number(s) in your username\n")
    game()
    return username


def game():
    """
    placeholder
    """

    random_word = get_random_word()
    guesses = 8
    guessed_letters = []
    correct_guesses = []
    game_over = False
    player_win = False

    while not game_over and guesses > 0:
        hidden_word = ""
        for letter in random_word:
            if letter in correct_guesses:
                hidden_word += letter
            else: 
                hidden_word += "_"

        print("." * 79)
        print(f"\n\nYou have {guesses} guesses left!\n")
        print(f"What you have already guessed: {guessed_letters}\n\n")
        print(f"The word is {hidden_word}")
        if "_" not in hidden_word:
            game_over = True
            player_win = True
            break

        guess = input("\nGuess a letter: ").upper()
        print("-" * 79)
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                clear_terminal()
                print(f'\n\nYou have already guessed this letter: "{guess}"')
                print(hangman[guesses])

            elif guess not in random_word:
                clear_terminal()
                print(f'\n\n!!! "{guess}" is not in the word unfortunately !!!')
                guesses -= 1
                guessed_letters.append(guess)
                print(hangman[guesses])

            else: 
                clear_terminal()
                print(f'\n\nNice one! "{guess}" is in the word.')
                correct_guesses.append(guess)
                guessed_letters.append(guess)
                print(hangman[guesses])

        else:
            clear_terminal()
            print("\n\nInvalid guess. Please only guess with 1 letter!")
            print(hangman[guesses])

    if player_win == True:
        clear_terminal()
        print("GOOD JOB! You won!\n")
        print(f'''Game info:
        1. The word was: {random_word}
        2. You finished the word with {guesses} left!''')

        option_choice = input("\n\nDo you want to play again? \nPress 'Y' to play again or 'N' to go go back to the main menu.\n\nEnter here: ").upper()
        if option_choice == "Y":
            clear_terminal()
            game()
        elif option_choice == "N":
            clear_terminal()
            main_menu()

    else:
        clear_terminal()
        print(hangman[guesses])
        print(f"\n\n\You failed and have run out of guesses :-(\nThe word was {random_word}.")

        option_choice = input("\n\nDo you want to play again? \nPress 'Y' to play again or 'N' to go go back to the main menu.\n\nEnter here: ").upper()
        if option_choice == "Y":
            clear_terminal()
            game()
        elif option_choice == "N":
            clear_terminal()
            main_menu()


def get_random_word():
    """
    Gets a random word from the list "words" in the words_list.py file
    """
    word = random.choice(words)

    return word.upper()


def rules():
    clear_terminal()
    print("-" * 79)
    rules_text = """The rules are as follows:\n
    1. 
    2.
    3.
    4."""
    print(rules_text)
    
    option_choice = False
    while option_choice is False:
        try:
            option_choice = input("\nAre you ready to play? Y/N: ")

            if option_choice == "y" or option_choice == "Y":
                option_choice = True
                clear_terminal()
                enter_username()

            elif option_choice == "n" or option_choice == "N":
                option_choice = True
                clear_terminal()
                main_menu()

            else:
                raise ValueError("only Y or N are valid options")
        except ValueError as e:
            print(f"\nInvalid Data: {e}.\n")
            option_choice = False


def clear_terminal():
    """
    This function clears the terminal when called upon. 
    Taken from here: https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    """
    The main menu for the game, lets the user read the rules for Hangman
    or starts the game depending on user input
    """

    print("-" * 79)
    print("Hello and welcome to a game of Hangman! \n")
    print("Please select what you want to do next: ")
    options_text = """
    1. Start Game
    2. Read the rules for Hangman
    """
    print(options_text)

    option_choice = False
    while option_choice is False:
        options_input = input("Enter what you want to do next here: ")

        if options_input == "1":
            option_choice = True
            clear_terminal()
            enter_username()

        elif options_input == "2":
            option_choice = True
            rules()

        else:
            print("\n---------")
            print("Invalid option! Please select between option 1 and 2. Try again. \n")


def main():
    """
    Calls the funcion which starts the game
    """

    main_menu()

main()
