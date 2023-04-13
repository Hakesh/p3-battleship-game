

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

    wrong_option = True
    while wrong_option:
        options_input = input("Enter what you want to do next here: ")

        if options_input == "1":
            print("placeholder")
            wrong_option = False
    
        elif options_input == "2":
            print("placeholder")
            wrong_option = False

        else:
            print("\n---------")
            print("Invalid option! Please only select between option 1 and 2. Try again. \n")


print("-" * 39)
print("Hello and welcome to a game of Hangman! \n")
main()

# Write your code to expect a terminal of 80 characters wide and 24 rows high
