'''
This program for greeting the user.
It takes the name from the user as an input and greet him/her.
'''

def greeting(name):
    return f"Hello {name}, Welcome."


user_name = input("Write your name: ").strip().capitalize()

print(greeting(user_name))