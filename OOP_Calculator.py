# Delera, Aritz B.

# Import the calculator_input, calculator_operations, and calculator_display
from calculator_input import CalculatorInput
from calculator_operations import CalculatorOperations
from calculator_display import CalculatorDisplay

# cretae a class calculator
class Calculator:
    # use a Non-Parametrized Constructor
    def __init__(self):
        # initialize the calculator_input, calculator_operations, and calculator_display
        self.input = CalculatorInput()
        self.operations = CalculatorOperations()
        self.display = CalculatorDisplay()
    
    # display the introduction
    def display_intro(self):
        self.display.display_opening()

    # test if numbers are able to output
    def test(self):
        # use while loop
        while True:
            # display the operations
            self.display.display_operations()
            # display the random trivia
            self.display.display_trivia()

            user_operation = self.input.get_operation()

            # use try-except method for exception handling
            try:
                while not self.operations.is_valid_operation(user_operation):
                    # display invalid operations
                    self.display.display_invalid_operation_message()
                    user_operation = self.input.get_operation()

                while True:
                    try:
                        number_1 = self.input.get_user_number("First")
                        number_2 = self.input.get_user_number("Second")
                        break
                    except ValueError:
                        print("\033[30mInvalid input. Please try again.\033[0m")

                result = self.operations.calculate_result(user_operation, number_1, number_2)

                # display the processing message
                self.display.display_processing_message()
                # display the result
                self.display.display_result(result)

            # add the exception handling
            except ZeroDivisionError:
                print("\033[30mInvalid Divisor. Zero is not applicable as a divisor!\033[0m")
                continue
            except TypeError:
                print("\033[30mInvalid data. Please try again.\033[0m")
                continue

            question = self.input.get_repeat_question()
            if not self.input.is_repeat_question(question):
                break
        # display the outro
        self.display.display_goodbye_message()
