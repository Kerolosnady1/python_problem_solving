
# Enter a number: 7  
# Output: Prime number

# Enter a number: 9  
# Output: Not a prime number


while True:

    try:
        number = int(input("Enter a number: ").strip())

        if number <= 1:
            print("This number is smaller than or equal 1.")
            continue

        is_prime = True

        for x in range(2, number):
            if number % x == 0:
                is_prime = False
                break

        if is_prime:
            print("Prime number.")
            break

        else:
            print("Not prime number.")
            break
        

    except ValueError:
        print("This isn't an integer!")
