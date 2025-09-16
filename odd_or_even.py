

while True:
    try:
        number = int(input("Enter a number: ").strip())
        if number % 2 == 0:
            print(f"{number} is even.")
            break

        else:
            print(f"{number} is odd.")
            break

    except ValueError:
        print("Not a number!")