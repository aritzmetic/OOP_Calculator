from calculator_display import CalculatorDisplay
from termcolor import colored
from pyfiglet import Figlet
import pyfiglet
import random
import time

# Create a new class

class CalculatorDisplayAddition(CalculatorDisplay):
    #override the display opening
    def display_opening(self):
        f = Figlet(font='isometric2')
        print(colored(f.renderText('OOP'), 'blue'))
        print("=" * 61)
        print(" Welcome to AritzMetic's Calculator! ".center(60, "+"))
        print("=" * 61)
        name = input("\033[30mHi Smart Pipol! What is your name?: \033[0m")
        print()
        print("\033[40mHi", name, "! AritzMetic is here to help you in solving your Maths!\033[0m")
        time.sleep(2)
    
    #override the goodby message
    def display_goodbye_message(self):
        print("Thank you for using AritzMetic's Calculator!")
        print(random.choice(self.goodbye_quotes))
        t = Figlet(font= 'doom')
        print()
        print(colored(t.renderText('THE END'), 'green'))