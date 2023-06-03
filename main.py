from storing_calculator import StoringCalculator

def run_calculator():
    calculator = StoringCalculator()
    calculator.display_intro()
    calculator.test()
    calculator.save_history_to_file()

if __name__ == "__main__":
    run_calculator()
    