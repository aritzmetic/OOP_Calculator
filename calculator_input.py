# define a class input
class CalculatorInput:
    # create a method to get the user's operatiom
    def get_operation(self):
        return input("\033[31mWhich of the available operators would you like to make use of?: \033[0m")

    # create a method to get the user's number
    def get_user_number(self, order):
        return float(input("\033[32mType in the {} number of what you wish to calculate: \033[0m".format(order)))
    def get_repeat_question(self):
        return input("\033[36mDo you wish to make another calculation? (Y/N): \033[0m")

    def is_repeat_question(self, question):
        return question.upper() == "Y"
 