'''
FileNotFoundError
'''

file_name = input("Enter the file name: ").strip().lower()

try:
    f = open(file_name)

except FileNotFoundError:
    print("This file name not found!")

else:
    print(f.read())

