# Enter numbers separated by space: 4 5 8 2 3 1
# No median number. Try again.
# Enter numbers separated by space: 4 5 8 2 1   
# Median number = 4
# Range of numbers = 7
# Absolute values = 1 2 4 5 8
import math

while True:
    numbers = input("Enter numbers separated by space: ").strip().split()

    try:
        converted = [int(number) for number in numbers]
        converted.sort()

        count = len(converted) # 5

        median = count / 2

        if count % 2 != 0:
            print(f"Median number = {converted[int(median)]}")

            max_number = converted[-1]
            min_number = converted[0]
            
            range_val = max_number - min_number

            print(f"Range of numbers = {range_val}")

            abs_value = [abs(x) for x in converted]

            print("Absolute values =", *abs_value)
        
        else:
            print("No median number. Try again.")
            continue

        break


    except ValueError:
        print("Please enter only numbers separated by spaces.")