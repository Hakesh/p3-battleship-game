# Write your code to expect a terminal of 80 characters wide and 24 rows high

def main():
    """
    The starting menu for the game, lets the user read the rules for Hangman
    or starts the game depending on user input
    """

    print("Please select what you want to do next: ")
    options_text = """
    1. Start Game
    2. Read the rules for Hangman
    """
    print(options_text)

    options_input = input("Enter what you want to do next here: ")
    if options_input == 1:
        print("placeholder")
    
    elif options_input == 2:
        print("placeholder")

    else:
        print("Invalid option! Please only select between option 1 and 2.")


print("-" * 39)
print("Hello and welcome to a game of Hangman! \n")
main()
