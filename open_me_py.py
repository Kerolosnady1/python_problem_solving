'''
This game is for my love of my life.
The game is about to guess the password to take Kerolos Dawod Heart as -
a gift of connection.
You give it the password, if it true you get the output and it ask you -
to press on q and enter to get out.
If you write the wrong password the game continue until you got it.
and if you get the correct password but in the press q section write down -
any other thing the game will retry again.
'''

print("".center(60,"-"))
print("> This Game Created By Your Love <".center(60, "="))
print("".center(60,"-"))

print("".center(60, "^"))

print("".center(60,"="))
print(" This Game Is To Guess The Password To Win The Game ".center(60,"="))
print("".center(60,"="))

print("   => Here Is A Hint: ( K****** L**** S***** S* M*** ) <= ")

print("".center(60,"*"))
print(" The Loop Will Not End Until You Solve The Case ".center(60,"$"))
print("".center(60, "*"))


kerolos_answer = "Kerolos Loves Shrouq So Much"

truth = True

while truth: # if the condition is True it will continue the loop

    # Input:

    guess_game = input("\nGuess The Password To Take Kerolos Heart => ").strip()

    # Check if the input is like expected or not:

    if guess_game == kerolos_answer:
        # truth = False # Logic Reversed
        print("".center(60,"#"))
        print("# You Won!!! #".center(60,"#"))
        print("# Really My Love I Love You So Much <3 #".center(60,"#"))
        print("# You Are My Sunshine <3 #".center(60,"#"))
        print("# I Wish For You All The Best My Future Wife <3 #".center(60,"#"))
        print("# My Love Shosho <3 #".center(60,"#"))
        print("".center(60,"#"))

        print()

        quit = input("Press Q On The Keyboard To Quit The Game => ").strip().lower()
        
        if quit == "q":
            print("".center(40, "-"))
            print("Goodbye My Baby Girl <3".center(40,"-"))
            print("".center(40,"-"))

            print()
            
            truth = False
        
        else:
            print(" => The Game Continue Because You Didn't Write Q.")

            print()

            truth = True

    else:
        truth = True
        print("\n\t\t => Wrong Answer Try Again. <= ")
    
