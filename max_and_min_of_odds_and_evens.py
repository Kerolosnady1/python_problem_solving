# Enter numbers separated by space: 5 3 11
# No even numbers found.
# Odd numbers: 5 3 11
# Max odd number = 11


while True:

    numbers = input("Enter numbers separated by space: ").strip().split()


    try:
        converted = [int(number) for number in numbers]

        evens = [even for even in converted if even % 2 == 0]

        odds = [odd for odd in converted if odd % 2 != 0]

        if evens:
            print("Evens:", *evens)
            print(f"Max even number = {max(evens)}")

        else:
            print("No even numbers found.")
        
        if odds:
            print("Odds:", *odds)
            print(f"Max odd number = {max(odds)}")

        else:
            print("No odd numbers found.")

        break



    except ValueError:
        print("Not numbers!")



#               (OR)                #

# This is a default loop

# while True:

#     numbers = input("Enter numbers separated by space: ").strip().split()

#     try:

#         converted = [int(number) for number in numbers]

#         evens = [even for even in converted if even % 2 == 0]

#         odds = [odd for odd in converted if odd % 2 != 0]

#         if evens:
#             print("Evens:", *evens)

#             largest_number_even = evens[0]

#             for x in range(len(evens)):
#                 if evens[x] >= largest_number_even:
#                     largest_number_even = evens[x]

#             print(f"Max even number = {largest_number_even}")

#         else:
#             print("No even numbers found.")

#         if odds:
#             print("Odds:", *odds)

#             largest_number_odd = odds[0]

#             for x in range(len(odds)):
#                 if odds[x] >= largest_number_odd:
#                     largest_number_odd = odds[x]

#             print(f"Max even number = {largest_number_odd}")

#         else:
#             print("No odd numbers found.")

#         break
    

#     except ValueError:
#         print("Not numbers!")