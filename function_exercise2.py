'''
This program designed to return the area of a rectangle.
You give it the length and width and it returns the value for you.
You can also use decimal/floating point number to return your number in more specific.
'''

def area_of_rectangle(length, width):
    return length * width

length_input = float(input("Enter the length of the rectangle: ").strip())
width_input = float(input("Enter the width of the rectangle: ").strip())

print(f"Your Rectangle Area is: {area_of_rectangle(length_input, width_input)}")