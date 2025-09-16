# Enter numbers separated by space: 2 4 6
# Even numbers: 2 4 6
# Sum of even numbers = 12
# No odd numbers found.


while True:

    numbers = input("Enter numbers separated by space: ").strip().split()

    odds = []

    evens = []

    converted = []

    try:
        converted = [int(number) for number in numbers]

        odds = [x for x in converted if x % 2 != 0]

        evens = [y for y in converted if y % 2 == 0]

        # if evens == []:
        # if not evens:
        #     print("No even numbers found.")
            

        # if odds == []:
        # if not odds:
        #     print("No odd numbers found.")
            

        # if evens != []:
        if evens:
            print("Even numbers:", *evens)
            print(f"Sum of even numbers: {sum(evens)}")

        else:
            print("No even numbers found.")

        # if odds != []:
        if odds:
            print("Odds:", *odds)
            print(f"Sum of odd numbers: {sum(odds)}")

        else:
            print("No odd numbers found.")

        break

        

    except ValueError:
        print("Not numbers!")

