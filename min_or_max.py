while True:
    converted = []
    numbers = input("Enter numbers with space: ").strip().split()

    for number in numbers:
        converted.append(int(number))

    minimum = converted[0]
    maximum = converted[0]

    for x in converted:
        if x < minimum:
            minimum = x

        if x > maximum:
            maximum = x

    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    break