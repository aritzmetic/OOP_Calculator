from OOP_Calculator import Calculator
from calculator_operations import CalculatorOperations

# Create a class for storing the result
class StoringCalculator(Calculator):
    # use a Non-Parametrized Constructor
    def __init__(self):
        super().__init__()
        self.history = []

    # override the calculate_result method to store the history
    def calculate_result(self, operator, number_1, number_2):
        result = self.operations.calculate_result(operator, number_1, number_2)
        equation = f"{number_1} {operator} {number_2} = {result}"
        self.history.append(equation)
        return result

    # Add a new method to save the history to a file
    def save_history_to_file(self):
        filename = "calculation_history.txt"
        with open(filename, "w") as file:
            for equation in self.history:
                file.write(equation + "\n")
        print(f"Calculation history saved to {filename}.")
