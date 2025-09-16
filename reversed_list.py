while True:

    user_list = []

    input_ = input("Enter anything with space: ").strip().split()

    # for y in input_:
    #     if y.isdigit():
    #         user_list = [int(x) for x in input_]
    #         user_list.reverse() # default loop
    
    if all(x.isdigit() for x in input_):
        user_list = [int(x) for x in input_] # Shortcut loop

    else:
        user_list = input_

    user_list.reverse()
    print("Your list reversed:", *user_list)
    break