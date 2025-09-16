rows = 1
while rows < 6:
    spaces = 1
    while spaces < 5:
        print(" " * (spaces + 2), end='')
        print("*" * (rows) , end='')

        spaces += 1
        rows += 1
    print()
