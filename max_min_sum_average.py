# Enter numbers separated by space: 5 8 2 9 4
# Max: 9
# Min: 2
# Sum: 28
# Average: 5.6

while True:

    converted = []

    user_input = input("Enter numbers seperated by space: ").strip().split()

    try:
        converted = [int(x) for x in user_input]

        maximum = max(converted)

        minimum = min(converted)

        total = sum(converted)

        average = total / len(converted)

        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")
        print(f"Sum: {total}")
        print(f"Average: {average}")
        break



    except ValueError:
        print("Not numbers!")
