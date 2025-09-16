# Enter numbers separated by space: 3 11 5
# No even numbers found.
# Odd numbers: 3 11 5
# Max odd number = 11
# Min odd number = 3

while True:

    numbers = input("Enter numbers separated by space: ").strip().split()

    try:

        converted = [int(number) for number in numbers]

        evens = [even for even in converted if even % 2 == 0]

        odds = [odd for odd in converted if odd % 2 != 0]

        if evens:
            print("Evens:", *evens)
            print(f"Max even number: {max(evens)}")
            print(f"Min even number: {min(evens)}")

        else:
            print("No even numbers found.")

        if odds:
            print("Odds:", *odds)
            print(f"Max odd number: {max(odds)}")
            print(f"Min odd number: {min(odds)}")

        else:
            print("No odd numbers found.")

        break


    except ValueError:
        print("Not numbers!")


#           OR          #
#       Default Way:    #


# while True:

#     numbers = input("Enter numbers separated by space: ").strip().split()

#     try:
#         converted = [int(number) for number in numbers]

#         evens = [even for even in converted if even % 2 == 0]

#         odds = [odd for odd in converted if odd % 2 != 0]


#         if evens:
#             print("Evens", *evens)

#             largest_even = evens[0]
#             smallest_even = evens[0]
#             for x in range(len(evens)):
#                 if largest_even < evens[x]:
#                     largest_even = evens[x]

#                 elif smallest_even > evens[x]:
#                     smallest_even = evens[x]

#             print(f"Max: {largest_even}")
#             print(f"Min: {smallest_even}")

#         else:
#             print("No even numbers found.")


#         if odds:
#             print("Evens", *odds)

#             largest_odd = odds[0]
#             smallest_odd = odds[0]
#             for x in range(len(odds)):
#                 if largest_odd < odds[x]:
#                     largest_odd = odds[x]

#                 elif smallest_odd > odds[x]:
#                     smallest_odd = odds[x]

#             print(f"Max: {largest_odd}")
#             print(f"Min: {smallest_odd}")

#         else:
#             print("No odd numbers found.")

#         break


#     except ValueError:
#         print("Not numbers!")