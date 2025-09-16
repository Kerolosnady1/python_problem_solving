'''
This program for two numbers simple calculation.
First you need to write down the first number, then the second number,
Then the operator you need to use for this case.
It will return the first number, then operator, then the second number, then the equal.
'''

number_one = float(input("Enter the first number: ".strip()))
number_two = float(input("Enter the second number: ".strip()))
operation = input("Enter the operator (+, -, *, /)".strip())

match operation:
    case "+":
        print(f"{number_one} + {number_two} = {number_one + number_two}")

    case "-":
        print(f"{number_one} - {number_two} = {number_one - number_two}")

    case "*":
        print(f"{number_one} * {number_two} = {number_one * number_two}")

    case "/":
        if number_two == 0:
            print("You cann't divide number over Zero")
        else:
            print(f"{number_one} / {number_two} = {number_one / number_two}")

    case _:
        print("This operator not found!")