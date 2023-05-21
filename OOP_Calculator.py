# Delera, Aritz B.

# Import the calculator_input, calculator_operations, and calculator_display
from calculator_input import CalculatorInput
from calculator_operations import CalculatorOperations

# cretae a class calculator
class Calculator:
    # use a Non-Parametrized Constructor
    def __init__(self):
        # initialize the calculator_input, calculator_operations, and calculator_display
        self.input = CalculatorInput()
        self.operations = CalculatorOperations()
    
    # display the introduction

    # test if numbers are able to output
    def test(self):
        # use while loop
        while True:
            # display the operations
            # display the random trivia

            user_operation = self.input.get_operation()

            # use try-except method for exception handling
            try:
                if self.operations.is_valid_operation(user_operation):
                    number_1 = self.input.get_user_number("First")
                    number_2 = self.input.get_user_number("Second")

                    result = self.operations.calculate_result(user_operation, number_1, number_2)

                    # display the processing message
                    # display the result

                    print(result)

                else:
                    # display invalid operations
                    print()
        
                question = self.input.get_repeat_question()
                if not self.input.is_repeat_question(question):
                    break
            
            # add the exception handling
            except ValueError:
                print("Invalid operation. Please try again.")
        
        # display the outro
calculator = Calculator()
calculator.test()