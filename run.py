from words_list import words
import os




def rules():
    clear_terminal()
    print("-" * 30)
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
                print("placeholder")

            elif option_choice == "n" or option_choice == "N":
                option_choice = True
                clear_terminal()
                main()

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


def main():
    """
    The main menu for the game, lets the user read the rules for Hangman
    or starts the game depending on user input
    """

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
            print("placeholder")
            option_choice = True

        elif options_input == "2":
            option_choice = True
            rules()

        else:
            print("\n---------")
            print("Invalid option! Please only select between option 1 and 2. Try again. \n")


print("-" * 39)
print("Hello and welcome to a game of Hangman! \n")
main()

# Write your code to expect a terminal of 80 characters wide and 24 rows high
