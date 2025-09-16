# This program give only one user permission, not list of users sign up.
# The next program will use list (.append() and .find()) to add more users.

def separator() -> None:
    print("".center(80, "="))

def sign_up() -> None:
        separator()
        print(" Welcome To Kero Sign Up Section <3 ".center(80, "="))
        separator()
        global sign_up_email, sign_up_password
        while True:
            sign_up_email = input("Enter your mail: ").strip().lower()
            if not sign_up_email:
                separator()
                print(" Can't be empty. PLease, enter your email. ".center(80, "^"))
                separator()
                continue
            else:
                sign_up_password = input("Enter your password: ").strip()
                if not sign_up_password:
                    separator()
                    print(" Can't be empty. Please, enter your password. ".center(80, "^"))
                    separator()
                    continue
                else:
                    break

def scientific_calc() -> None:
    separator()
    print(" Welcome To Kero Scientific Calculator Section <3 ".center(80, "="))
    separator()
    while True:
        list_of_numbers = input("Enter the list of numbers separated by space: ").strip().split()
        separator()
        operator = input("Enter the operator ( '+' / '-' / '*' / '/' ): ").strip()
        separator()

        try:
            converted_numbers = [int(number) for number in list_of_numbers]

            if operator == '+':
                if converted_numbers:
                    total = converted_numbers[0]
                    for x in range(1, len(converted_numbers)):
                        total += converted_numbers[x]

                    print(f"> Sum of your numbers is {total} <".center(80, "="))
                    break

                else:
                    print(" The list is empty ".center(80, "^"))
                    continue
            
            elif operator == '-':
                if converted_numbers:
                    menus = converted_numbers[0]
                    for x in range(1, len(converted_numbers)):
                        menus -= converted_numbers[x]
                    
                    print(f"> Subtract of your numbers is {menus} <".center(80, "="))
                    break

                else:
                    print(" The list is empty ".center(80, "^"))
                    separator()
                    continue

            elif operator == '*':
                if converted_numbers:
                    multiply = converted_numbers[0]
                    for x in range(1, len(converted_numbers)):
                        multiply *= converted_numbers[x]

                    print(f"> Product of your numbers {multiply} <".center(80, "="))
                    break

                else:
                    print(" The list is empty or even zero. ".center(80, "^"))
                    continue

            elif operator == '/':
                if converted_numbers:
                    divide = converted_numbers[0]
                    for x in range(1, len(converted_numbers)):
                        divide /= converted_numbers[x]

                    print(f"> Division of your numbers is {divide} <".center(80, "="))
                    break

                else:
                    print(" Can't divide over zero. ".center(80, "^"))
                    continue

            else:
                separator()
                print(" Invalid operator. ".center(80, "^"))
                separator()
                try:
                    try_again = int(input("If you want to try again, enter (1), if you want to exit, enter (0): ").strip())
                    if try_again == 1:
                        continue
                    elif try_again == 0:
                        separator()
                        print("Bye Bye\nExiting...")
                        separator()
                        break
                    else:
                        separator()
                        print(" Invalid choice. Please, enter (1 / 0) ".center(80, "^"))
                        separator()
                        continue
                except ValueError:
                    separator()
                    print(" This ain't number! ".center(80, "^"))
                    separator()


        except ValueError:
            separator()
            print(" This ain't numbers! ".center(80, "^"))
            separator()
            try:
                try_again = int(input("If you want to try again, enter (1), if you want to exit, enter (0): ").strip())
                if try_again == 1:
                    continue
                elif try_again == 0:
                    break
                else:
                    separator()
                    print(" Invalid choice. Please, enter (1 / 0) ".center(80, "^"))
                    separator()
                    continue

            except ValueError:
                separator()
                print(" This ain't number! ".center(80, "^"))
                separator()

def sign_in() -> None:
        separator()
        print(" Welcome To Kero Sign In Section <3 ".center(80,"="))
        separator()
        while True:
            separator()
            sign_in_email = input("Enter your email to login: ").strip().lower()
            separator()
            if sign_in_email == sign_up_email:
                sign_in_password = input(f"Enter your password related to {sign_in_email}: ").strip()
                separator()
                if sign_in_password == sign_up_password:
                    scientific_calc()
                    separator()
                    break
                else:
                    separator()
                    print(f"The password related to {sign_in_email} is incorrect.")
                    separator()
                    try:
                        try_again = int(input("If you want to try again, enter (1), if you want to exit, enter (0): ").strip())
                        separator()
                        if try_again == 1:
                            continue
                        elif try_again == 0:
                            separator()
                            print("Bye Bye\nExiting...")
                            separator()
                            break
                        else:
                            separator()
                            print(" Invalid choice. Please, enter (1 / 0) ".center(80, "^"))
                            separator()
                            continue
                    except ValueError:
                        print("This ain't number!")
            else:
                separator()
                print(" Your email isn't valid. ".center(80, "^"))
                separator()
                continue

while True:
    separator()
    print("To Know, You Can't Use Kero Calculator Without Sign In With Email and Password.")
    separator()
    print("Enter one of:\n1]Sign up\n2]Sign in\n3]Exit\nTo Use Kero Scientific Calculator.")
    separator()
    choice = input("Enter here your choice: ").strip()
    separator()
    if choice.isdigit():
        print(" Please, enter the name of your choice not the number. ".center(80, "^"))
        separator()
    else:
        if choice.lower() == 'sign up':
            sign_up()
        elif choice.lower() == 'sign in':
            sign_in()
        elif choice.lower() == 'exit':
            separator()
            print("Bye Bye\nExiting...")
            separator()
            break
        else:
            separator()
            print(" This isn't valid choice. ".center(80, "^"))
            print("> Try again. <".center(80, "="))
            separator()
            continue