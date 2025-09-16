while True:
    converted = []
    evens_list = []
    odds_list = []

    numbers = input("Enter numbers with space: ").strip().split()

    try:
            
        # for number in numbers:
        #         converted.append(int(number)) # Default list append

        converted = [int(number) for number in numbers] # list comprehension (append)

        for x in converted:
            if x % 2 == 0:
                evens_list.append(x)

            else:
                odds_list.append(x)

        # print(f"Evens:", end=" ")
        # for y in evens_list:
        #     print(f"{y}", end=" ") # Unpacking using for loop

        print(f"Evens:", *evens_list) # Unpacking using *

        # print()

        # print("Odds:", end=" ")
        # for z in odds_list:
        #     print(f"{z}", end=" ") # Unpacking using for loop

        print(f"Odds:", *odds_list) # Unpacking using *

        break

    except ValueError:
         print("Not a number!")

    

