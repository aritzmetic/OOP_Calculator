# import pyfiglet, random, and time
import pyfiglet
import random
import time

# create a class display
class CalculatorDisplay:
    # use a Non-Parametrized Constructor
    def __init__(self):
        # initialize the quotes
        self.trivia = [
            "Did you know that the word 'addition' comes from the Latin word 'addere', which means 'to give more'?", 
            "Did you know that the word 'subtraction' comes from the Latin word 'subtrahere', which means 'to take away'?", 
            "Did you know that the word 'multiplication' comes from the Latin word 'multiplicare', which means 'to increase in number'?",
            "Did you know that the word 'division' comes from the Latin word 'dividere', which means 'to separate'?"
        ]

        self.goodbye_quotes = [
            "Mathematics is the language in which God has written the universe. - Galileo Galilei",
            "In mathematics, the art of proposing a question must be held of higher value than solving it. - Georg Cantor",
            "The study of mathematics, like the Nile, begins in minuteness but ends in magnificence. - Charles Caleb Colton"
        ]

    # define the opening
    def display_opening(self):
        opening = pyfiglet.figlet_format("= O.O.P =", font="starwars")
        print(opening)
        print("=" * 61)
        print(" Welcome to AritzMetic's Calculator! ".center(60, "+"))
        print("=" * 61)

    # define the display operations
    def display_operations(self):
        print()
        print("+" * 61)
        print()
        print("\033[30mPress the letter of the operation you choose!\033[0m")
        print()
        print("-" * 61)
        print()
        print("A for Addition".center(60))
        print("S for Subtraction".center(60))
        print("M for Multiplication".center(60))
        print("D for Division".center(60))
        print()
        print("-" * 61)

    # define the random trivia
    def display_trivia(self):
        print()
        print("-" * 61)
        print()
        print(random.choice(self.trivia))
        print()
        print("+" * 61)
        time.sleep(2)

    # define the processing message
    def display_processing_message(self):
        print()
        print(":" * 61)
        print("\033[33mProcessing...\033[0m" .center(60))
        print(":" * 61)
        print()
        time.sleep(2)

    # define the display of the result
    def display_result(self, result):
        try:
            print(f"\033[41mWe appreciate your willingness to wait. The result of your math is {result}!\033[0m")
        except Exception:
            print("\033[30mAn error occurred while displaying the result.\033[0m")

    # define the invalid operation
    def display_invalid_operation_message(self):
        print("\033[30mThere is a problem with the operator you entered, possibly due to incorrect capitalization or invalid operation. Could you just give it another shot?\033[0m")

    # define the outro quote
    def display_goodbye_message(self):
        print("Thank you for using AritzMetic's Calculator!")
        print(random.choice(self.goodbye_quotes))
        closing = pyfiglet.figlet_format(" = THE END = ", font="doom")
        print(closing)


