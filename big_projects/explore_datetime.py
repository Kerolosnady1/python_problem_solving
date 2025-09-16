'''
This program built to tell you the time now and if you want to add number of days -
to add on the current time you are able.

Steps:
    - The current date and time will pop up.
    - It will tell you to enter the time you want to add.
    - If you don't want to add just enter 0 (ZERO).
    - If you jsut entered 0 the value will be None and None is for Nothing.
    - If you want to add just type a number.
    - If you enter anything either a number it will print you a message that -
        <This isn't an integer number!>
    - But if you enter a number it will calculate it for you and return the value -
        after calculation process.
'''

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return f"Current date and time: {current_date.strftime("%Y-%m-%d %I:%M:%S %p")}"

def calculate_future_date():
    while True:
        print("".center(50,"*"))
        number_of_days = input("Enter the number of days you want to add or 0 to exit: ").strip()

        if number_of_days.isdigit():
            number_of_days = int(number_of_days)
            if number_of_days == 0:
                print("Bye Bye")
                break
            else:
                future_date = datetime.now() + timedelta(days=number_of_days)
                return f"Future date: {future_date.strftime("%Y-%m-%d %I:%M:%S %p")}"
                break

        else:
            print(" This isn't an integer number! ".center(50, "^"))

def main():
    print("".center(50,"-"))
    print(display_current_datetime())
    print("".center(50,"-"))
    print()
    print(f"=> {calculate_future_date()} <=".center(50,"="))
    print("".center(50, "*"))

main()