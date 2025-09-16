'''
ZeroDivisionError
'''
while True:
    number_one = input("Enter the first number: ").strip()
    if number_one.isdigit():
        number_one = int(number_one)

    else:
        print("This isn't an integer number.")
        continue

    number_two = input("Enter the second number: ").strip()

    if number_two.isdigit():
        number_two = int(number_two)

    else:
        print("This isn't an integer number.")
        continue

    try:
        print(number_one / number_two)

    except ZeroDivisionError:
        print("You cann't divide number with zero.")

    finally:
        print("The process is ended successfully.")
        break
    