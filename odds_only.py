# Enter numbers separated by space: 4 7 2 9 10
# Odd numbers: 7 9

while True:

    converted = []

    odds_list = []

    numbers = input("Enter numbers separated by spaces: ").strip().split()

    try:
        converted = [int(number) for number in numbers]

        for x in converted:
            if x % 2 != 0:
                odds_list.append(x)

            else:
                pass
            
        if odds_list == []:
            print("No odds found!")
            break

        else:
            print("Odds:", *odds_list)
            break



    
    except ValueError:
        print("Not numbers!")
