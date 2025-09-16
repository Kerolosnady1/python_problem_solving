# Enter numbers separated by space: 3 11 5
# No even numbers found.
# Odd numbers: 3 11 5
# Max odd number = 11
# Min odd number = 3
# Count of odds = 3

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
            print(f"Count of evens = {len(evens)}")

        else:
            print("No even numbers found.")

        
        if odds:
            print("Odds:", *odds)
            print(f"Max odd number = {max(odds)}")
            print(f"Min odd number = {min(odds)}")
            print(f"Count of odds = {len(odds)}")

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

#         evens = [even for even in converted if even % 2 == 0]

#         odds = [odd for odd in converted if odd % 2 != 0]

#         if evens:
#             print("Evens:", *evens)

#             max_even = evens[0]
#             min_even = evens[0]


#             for x in range(1, len(evens)):
#                 if max_even < evens[x]:
#                     max_even = evens[x]

#                 if min_even > evens[x]:
#                     min_even = evens[x]

#             print(f"Max even number = {max_even}")
#             print(f"Min even number = {min_even}")
#             print(f"Count of evens = {len(evens)}")

#         else:
#             print("No even numbers found.")

        
#         if odds:
#             print("Odds:", *odds)

#             max_odd = odds[0]
#             min_odd = odds[0]

#             for x in range(1, len(odds)):
#                 if max_odd < odds[x]:
#                     max_odd = odds[x]

#                 if min_odd > odds[x]:
#                     min_odd = odds[x]

#             print(f"Max odd number = {max_odd}")
#             print(f"Min odd number = {min_odd}")
#             print(f"Count of odds = {len(odds)}")

#         else:
#             print("No odd numbers found.")


#         break

#     except ValueError:
#         print("Please enter only numbers separated by spaces.")
