positive_int = int(input("Enter the size of the pattern in positive number: ".strip()))

while positive_int > 0:

    for row in range(positive_int):

        print("*", end="")

    print()

    positive_int -= 1