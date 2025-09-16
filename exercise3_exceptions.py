'''
ValueTooHighError
'''

class ValueTooHighError(Exception):
    pass


while True:
    number = input("Enter a number: ").strip()

    if number.isdigit():
        number = int(number)

        if number > 100:
            raise ValueTooHighError
        
        
        else:
            print(f"{number} is smaller than 100.")
            break

    else:
        print("This isn't an integer number!")
        continue

