# Delera, Aritz B.

# Import the calculator_input
from calculator_input import CalculatorInput

# cretae a class calculator
class Calculator:
    # use a Non-Parametrized Constructor
    def __init__(self):
        # initialize the calculator_input
        self.input = CalculatorInput()
         
    # test if numbers are able to output
    def test(self):
     number_1 = self.input.get_user_number("first")
     number_2 = self.input.get_user_number("second")

     result = number_1 + number_2
     return result

calculator = Calculator()
result = calculator.test()
print("Result:", result)