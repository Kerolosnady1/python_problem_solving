'''
This program is dynamic shopping list manager.
You can add, remove, view,  or exit the program.
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
    4- If you write 3 the program will show you all the items inside the list.
    5- If you write 4 the program will get you out safely with bye bye.
'''

def display():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def shopping_list_manager():
    shopping_list = []

    while True:
        display()

        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            choosen_number = int(choice)

        else:
            print("Invalid you must write 1, 2, 3, or 4")
        
        if choosen_number == 1:
            add_items = input("Enter the item to add: ").strip()
            
            if add_items.isdigit():
                item_is_number = int(add_items)
                shopping_list.append(item_is_number)
            else:
                shopping_list.append(add_items)

        elif choosen_number == 2:
            remove_items = input("Enter the item to remove: ").strip()
            if remove_items.isdigit():
                remove_number = int(remove_items)
                shopping_list.remove(remove_number)
                print(f"{remove_number} removed successfully.")
            
            elif remove_items not in shopping_list:
                print(f"{remove_items} is not in the list")

            else:
                shopping_list.remove(remove_items)
                print(f"{remove_items} removed successfully.")

        elif choosen_number == 3:
            print(f"Your list: {shopping_list}")

        elif choosen_number == 4:
            print("Goodebye!")
            print("Exiting...!")
            break

        else:
            print("Invalid choice. Please try again.")


shopping_list_manager()