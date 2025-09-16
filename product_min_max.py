# Enter numbers separated by space: 4 1 2 5 8 9 3
# Evens: 4 2 8
# Max even number = 8
# Product of even numbers = 64
# Odds: 1 5 9 3
# Max odd number = 9
# Product of odd numbers = 135


# import math

# multi_even = math.prod(evens) if evens else None
# multi_odd = math.prod(odds) if odds else None


while True:

    numbers= input("Enter numbers separated by space: ").strip().split()

    try:
        converted = [int(number) for number in numbers]

        evens = [even for even in converted if even % 2 == 0]

        odds = [odd for odd in converted if odd % 2 != 0]

        # multi_even = [multiply * for multiply in evens if evens != 0]
        multi_even = evens[0]
        if evens:
            for x in range(1,len(evens)):
                multi_even *= evens[x]

            print("Evens:", *evens)
            print(f"Max even number = {max(evens)}")
            print(f"Product of even numbers = {multi_even}")

        else:
            print("No even numbers found.")

        multi_odd = odds[0]
        if odds:
            for x in range(1, len(odds)):
                multi_odd *= odds[x]

            print("Odds:", *odds)
            print(f"Max odd number = {max(odds)}")
            print(f"Product of odd numbers = {multi_odd}")

        else:
            print("No odd numbers found.")

        break


    except ValueError:
        print("Please enter only numbers separated by spaces.")


#           OR          #
# Time complexity same as the previous code.

# import math

# while True:
#     numbers = input("Enter numbers separated by space: ").strip().split()

#     try:
#         converted = [int(num) for num in numbers]

#         evens = [x for x in converted if x % 2 == 0]
#         odds = [x for x in converted if x % 2 != 0]

#         if evens:
#             print("Evens:", *evens)
#             print(f"Max even number = {max(evens)}")
#             print(f"Product of evens = {math.prod(evens)}")
#         else:
#             print("No even numbers found.")

#         if odds:
#             print("Odds:", *odds)
#             print(f"Max odd number = {max(odds)}")
#             print(f"Product of odds = {math.prod(odds)}")
#         else:
#             print("No odd numbers found.")

#         break

#     except ValueError:
#         print("Please enter only numbers separated by spaces.")


#           OR          #
# Manual solution:

# while True:

#     numbers = input("Enter numbers separated by space: ").strip().split()

#     try:
#         converted = [int(number) for number in numbers]

#         evens = [even for even in converted if even % 2 == 0]

#         odds = [odd for odd in converted if odd % 2 != 0]

#         if evens:
#             print("Evens:", *evens)

#             max_even = evens[0]
#             prod_even = evens[0]

#             for x in range(1, len(evens)):
#                 if max_even < evens[x]:
#                     max_even = evens[x]

#                 prod_even *= evens[x]

#             print(f"Max even number = {max_even}")
#             print(f"Product of even numbers = {prod_even}")

#         else:
#             print("No even numbers found.")

        
#         if odds:
#             print("Odds:", *odds)

#             max_odd = odds[0]
#             prod_odd = odds[0]

#             for x in range(1, len(odds)):
#                 if max_odd < odds[x]:
#                     max_odd = odds[x]

#                 prod_odd *= odds[x]

#             print(f"Max odd number = {max_odd}")
#             print(f"Product of odd numbers = {prod_odd}")

#         else:
#             print("No odd numbers found.")

#         break
    

#     except ValueError:
#         print("Please enter only numbers separated by spaces.")
