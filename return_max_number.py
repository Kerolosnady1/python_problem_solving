# Enter first number: 4  
# Enter second number: 10  
# Enter third number: 7  

# Output: The largest number is: 10

while True:
    try:
        number_one = int(input("Enter first number: ").strip())
        number_two = int(input("Enter second number: ").strip())
        number_three = int(input("Enter third number: ").strip())

        max_val = max(number_one, number_two, number_three)

        print(f"The largest number is: {max_val}")
        break

    except ValueError:
        print("Enter a number, not text!")
        continue