# Enter numbers separated by space: 2 3 4 5
# Max = 5
# Min = 2
# Sum = 14
# Average = 3.5
# Product = 120

import math

while True:

    numbers = input("Enter numbers separated by space: ").strip().split()

    try:
        converted = [int(number) for number in numbers]

        evens = [even for even in converted if even % 2 == 0]

        odds = [odd for odd in converted if odd % 2 != 0]

        if evens:
            print("Evens:", *evens)
            print(f"Max even number = {max(evens)}")
            print(f"Min even number = {min(evens)}")
            print(f"Sum of even number = {sum(evens)}")
            print(f"Average of even numbers = {sum(evens) / len(evens)}")
            print(f"Product of even numbers = {math.prod(evens)}")

        else:
            print("No even numbers found.")


        print("".center(50, "="))


        if odds:
            print("Odds:", *odds)
            print(f"Max odd number = {max(odds)}")
            print(f"Min odd number = {min(odds)}")
            print(f"Sum of odd numbers = {sum(odds)}")
            print(f"Average of odd numbers = {sum(odds) / len(odds)}")
            print(f"Product of odd numbers = {math.prod(odds)}")

        else:
            print("No odd numbers found.")

        break

    except ValueError:
        print("Please enter only numbers separated by spaces.")


#           OR          #
# Manual solution:

# while True:

#     numbers = input("Enter numbers separated by space: ").strip().split()

#     try:
#         converted = [int(number) for number in numbers]

#         max_number = converted[0]

#         min_number = converted[0]

#         total = converted[0]

#         avg = 0

#         prod = converted[0]

#         for x in range(1, len(converted)):
#             if max_number < converted[x]:
#                 max_number = converted[x]

#             if min_number > converted[x]:
#                 min_number = converted[x]

#             total += converted[x]

#             avg = total / len(converted)

#             prod *= converted[x]

        
#         print(f"Max = {max_number}")
#         print(f"Min = {min_number}")
#         print(f"Sum = {total}")
#         print(f"Average = {avg}")
#         print(f"Product = {prod}")

#         break

#     except ValueError:
#         print("Please enter only numbers separated by spaces.")