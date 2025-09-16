'''
This program for checking if the number is even or odd.
First you need to give it the number,
Then it will print the result for you.
'''

def even_or_odd(number):
    if number % 2 == 0:
        return f"The number is even."
    
    else:
        return f"The number is odd"
    
number_input = int(input("Enter the number you want to check: ").strip())

print(f"=> {even_or_odd(number_input)}")