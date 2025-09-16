'''
This program design to convert any number from fahrenheit to celsius and vise versa.
First step:
    - It will print Enter (1/2/3), if you enter 1, then you want the number you will write
    to convert to celsius, but if you enter 2, then you want it to convert to fahrenhiet,
    or if you enter 3 it will get you out safly.
    NOTE: If you enter any other thing like any other number or text, it will print
    <Invalid, just enter one of (1/2/3)!!>

Second step:
    - If you enter a valid number (1/2), then it will ask you to enter the number you
    want to convert.
    NOTE: If you enter text the program will print, <Invalid, just enter one of (1/2/3)!!>

Third step:
    - If you enter the number you want to use as celsius or fahrenheit, and enter
    the number you want to convert, then the output will be -
    <the_number_you_entered_after_converting ((C/F) => as you entered)>
'''

fahrenheit_to_celsius_factor = 5/9

celsius_to_fahrenheit_factor = 9/5

def convert_to_celsius(fahrenheit):
    return f"{fahrenheit * fahrenheit_to_celsius_factor:.1f}°C"

def convert_to_fahrenheit(celsius):
    return f"{celsius * celsius_to_fahrenheit_factor:.1f}°F"

while True:
    print("".center(50,"="))
    print(" Choose the weather number ".center(50, "-"))
    print(" 1 => Celsius ".center(50, "*"))
    print(" 2 => Fahrenheit ".center(50, "*"))
    print(" 3 => Exit ".center(50,"*"))
    print("".center(50,"="))

    type_of_temp = input("Enter (1/2/3): ").strip()

    if type_of_temp.isdigit():
        type_of_temp = int(type_of_temp)
        if type_of_temp == 1:
            pass
        elif type_of_temp == 2:
            pass
        elif type_of_temp == 3:
            print("Bye Bye")
            print(" Exiting...! ".center(50, "-"))
            break
        else:
            print("Invalid, just enter one of (1/2/3)!!")
            continue

    else:
        print("Invalid, just enter one of (1/2/3)!!")
        continue

   
    temp_number = input("Enter the number you want to convert: ").strip()

    if temp_number.isdigit():
        temp_number = float(temp_number)

        if type_of_temp == 1:
            print(convert_to_celsius(temp_number))
            break

        elif type_of_temp == 2:
            print(convert_to_fahrenheit(temp_number))
            break

        else:
            print("Invalid, just enter one of (1/2)!!")

    else:
        print("Invalid, just write a number.")

