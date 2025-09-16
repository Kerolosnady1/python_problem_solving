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
            print(f"Odds:", *odds)
            print(f"Max odd number = {max(odds)}")
            print(f"Min odd number = {min(odds)}")
            print(f"Count of odds = {len(odds)}")
        
        else:
            print("No odd numbers found!")
        
        break



    except ValueError:
        print("Not Numbers!")