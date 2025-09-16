while True:
    numbers = input("Enter numbers separated by space: ").strip().split()

    try:
        converted = [int(number) for number in numbers]

        if converted:
            con_len = len(converted)

            for x in range(con_len - 1):
                for y in range(con_len - x - 1):
                    if converted[y] > converted[y + 1]:
                        converted[y], converted[y + 1] = converted[y + 1], converted[y]

            print(f"Sorted list = {converted}")
        
            break

        else:
            print("N/A the list is empty.")
    
    except ValueError:
        print(f"N/A not all are numbers.")