

# Example Input: Ahmed
# Example Output: Hello, Ahmed!

def say_hello(name):
    return f"Hello, {name}"


while True:
    user_name = input("Enter your name: ").strip().title()

    if not user_name.isalpha():
        print("This isn't name!")
        continue

    else:
        print(say_hello(user_name))
        break
