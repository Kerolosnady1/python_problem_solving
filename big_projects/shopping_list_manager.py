'''
This program is dynamic shopping list manager.
You can add, remove, or exit the program.
The program design is really simple but handle all expected inputs, and errors.
How it works:
    1- You need to write a number 1 for adding section, 2 for removing section, and 3 for exit
        - if you write text input the program will print an invalid message.
        - if you write a number neither 1, 2, or 3 it will print invalid input.
    2- If you write 1 the program wiil wait for your input to put it in the list.
        - if you write a text or int will save it inside the list as you write.
        - if you write a floating point number (decimal) will save it as you write, but
        NOTE: it will save the floating point number as text not number.
    3- If you write 2 the program will wait for your input of the item you need to remove.
        - if you write integer, decimal, or text it will find it and remove it as you write.
        - if you write somthing not inside the list it will print this item is not in the list
    4- If you write 3 the program will get you out safely with bye bye.
'''
shopping_list = []

continues = True
print("".center(70,"-"))
print(" This is a shopping list manager, you can add, and remove items ".center(70,"-"))
print("".center(70,"-"))


while continues:
    choose = input("Choose (1.Adding | 2.Removing | 3.Exit): ").strip()

    if choose.isdigit():
        choose = int(choose)

    else:
        print("Invalid input, please choose 1, 2 or 3")
        continue

    if choose == 1:
        adding_item = input("Add Your Item: ").strip()
        
        if adding_item.isdigit():
            
            number = int(adding_item)
            shopping_list.append(number)
            print(f"{number} Added Successfully")
            print(f"Your items are {shopping_list}")
        
        else:
            shopping_list.append(adding_item)
            print(f"{adding_item} Added Successfully")

            print(f"Your items are {shopping_list}")

            # continues = False

    elif choose == 2:
        removing_item = input("Enter the name of item you want to remove: ").strip()

        for x in shopping_list:
            if removing_item == x:
                if x.isdigit():
                    removing_item = float(x)
                else:
                    shopping_list.remove(removing_item)
                    print(f"Your list now is {shopping_list}")
                    print(f"The item you removed is: {removing_item}")

                # continues = False

            else:
                print("This item is not in the list.")
                # continues = False


    elif choose == 3:
        print("Exiting...")
        print("Bye Bye")
        break

    else:
        print("Please, choose one of (1.Adding | 2.Removing | 3.Exit)")