while True:
    total = 0

    try:    
        numbers = int(input("Enter a positive integers: ").strip())

        if numbers < 0:
            print("Not a positive number!")
            continue

        else:
            numbers = str(numbers)

            for number in numbers:
                number = int(number)

                total += number

       
        print(f"the sum of digits = {total}")
        break

    except ValueError:
        print("Not an integer number!")

        