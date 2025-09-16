'''
This program for multiplication table of one number.
First you write down the number then the program will,
Give you the number you write with the * operator with numbers from 1-10
'''

numbers_table = int(input("Enter a number to see its multiplication table: ".strip()))

for number in range(1,11):
    
    print(f"{numbers_table} * {number} = {numbers_table * number}")