# Enter numbers separated by space: 1 1 2 3 4 5 6 7 6
# Frequencies: {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 1}
# Top 3: [7, 6, 6]
# Less 3: [1, 1, 2]

from collections import Counter

while True:

    numbers = input("Enter numbers separated by space: ").strip().split()

    try:
        converted = [int(number) for number in numbers]

        counter = Counter(converted)
        print(f"Frequencies: {dict(counter)}")

        converted.sort(reverse=True)
        print(f"Top 3: {converted[:3]}")

        converted.sort()
        print(f"Less 3: {converted[:3]}")

        break


    except ValueError:
        print("Please enter only numbers separated by spaces.")