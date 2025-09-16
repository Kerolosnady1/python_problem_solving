# Enter numbers separated by space: k
# Please enter only numbers separated by spaces.
# Enter numbers separated by space: 2 1 5 3 4 7
# Max: 7
# Min: 1
# Sum: 22
# Average: 3.6666666666666665
# Product: 840

import math

while True:

    numbers = input("Enter numbers separated by space: ").strip().split()

    try:
        converted = [int(number) for number in numbers]


        print(f"Max: {max(converted)}")
        print(f"Min: {min(converted)}")
        print(f"Sum: {sum(converted)}")
        print(f"Average: {sum(converted) / len(converted)}")
        print(f"Product: {math.prod(converted)}")

        break

    except ValueError:
        print("Please enter only numbers separated by spaces.")


#           OR          #
# Manual solution:

# while True:

#     numbers = input("Enter numbers separated by space: ").strip().split()

#     try:
#         converted = [int(number) for number in numbers]

#         if not numbers:
#             print("You didn't enter any number!")
#             continue
        
#         max_number = min_number = total = product = converted[0]
#         average = 0

#         for x in range(1, len(converted)):
            
#             if max_number < converted[x]: max_number = converted[x]

#             if min_number > converted[x]: min_number = converted[x]

#             total += converted[x]

#             product *= converted[x]

#         average = total / len(converted)

#         print(f"Max: {max_number}\nMin: {min_number}\nSum: {total}\nAverage: {average}\nProduct: {product}")
#         break


#     except ValueError:
#         print("Please enter only numbers separated by spaces.")