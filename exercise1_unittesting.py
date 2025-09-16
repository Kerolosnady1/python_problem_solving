'''
Exercise 1: Understanding the Importance of Testing

Instruction:

Write a small Python function (e.g., a function to calculate the square of
 a number) and intentionally introduce a bug (e.g., incorrect calculation logic).
'''
def calc_sqr_number():
    assert 5 ** 2 == 25, "Should be 25"

calc_sqr_number()