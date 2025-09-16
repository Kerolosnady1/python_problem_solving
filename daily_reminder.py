'''
This program is for daily remainder.
You give it the input of high/medium/low,
Then give it one of yes/no or y/n and it write up advice for you.
Any other things you with got Not Valid Input!
This program tested carefully to not give you error by the interpreter.
'''

task = input("Enter your task: ").strip().capitalize()

priority = input("(high/medium/low): ").strip().lower()

time_bound = input("Is it time-bound? (Yes/No): ").strip().lower()


if (priority == 'high') and ((time_bound == 'yes') or (time_bound == 'y')):

    print(f"Remainder: '{task}' is a high priority task that requires immediate attention today!")
    

elif (priority == 'medium') and ((time_bound == 'yes') or (time_bound == 'y')):

    print(f"Remainder: '{task}' is a medium priority task that requires medium attention that you can do it today or tomorrow.")


elif (priority == 'low') and ((time_bound == 'yes') or (time_bound == 'y')):

    print(f"Remainder: '{task}' is a low priority task that requires low attention that you can do it at any time in this week.")
    

elif (priority == 'high') and ((time_bound == 'no') or (time_bound == 'n')):

    print(f"Remainder: '{task}' is a high priority task that requires high attention but you can do it today or tomorrow.")
    

elif (priority == 'medium') and ((time_bound == 'no') or (time_bound == 'n')):

    print(f"Remainder: '{task}' is a medium priority task that requires medium attention that you can do it at any time in this week.")
    

elif (priority == 'low') and ((time_bound == 'no') or (time_bound == 'n')):

    print(f"Remainder: '{task}' is a low priority task that requires low attention that you can do it in any time.")
    

else:

    print("Not Valid Input!")

