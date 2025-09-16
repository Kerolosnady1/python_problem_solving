'''
Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:

Division by Zero: Use a try-except block to catch ZeroDivisionError.
Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block 
 to catch ValueError for non-numeric inputs.
Return appropriate messages for errors or the result for successful division.
'''

def safe_divide(numerator, denominator):

    try:
        return f"Your result: {float(numerator) / float(denominator)}"

    except ZeroDivisionError:
        return "The denominator cann't be ZERO!"

    except ValueError:
        return "This isn't a number!"

    