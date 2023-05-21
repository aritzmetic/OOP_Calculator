# import operator
import operator

# create a class operations
class CalculatorOperations:
    # use a Non-Parametrized Constructor
    def __init__(self):
        # initialize the dictionary
        self.operator_dictionary = {"A": operator.add, "S": operator.sub, "M": operator.mul, "D": operator.truediv}

    # define a method is the operation is valid
    def is_valid_operation(self, operation):
        return operation in self.operator_dictionary

    # define a method that perform the calculations
    def calculate_result(self, operator, number_1, number_2):
        return self.operator_dictionary[operator](number_1, number_2)