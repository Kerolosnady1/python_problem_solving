'''
Exercise 2: Writing Basic Unit Tests

Instruction:

Use the unittest module in Python to create a test case for the buggy function
 from Exercise 1.
Write test methods to check different scenarios (e.g., valid input, invalid input)
 and verify expected behavior.
'''



import unittest
def test_input():

    print("Write this email in input, email@email.com")

    input_ = input("Enter here: ").strip().lower()



class checking(unittest.TestCase):

    def checker(self):
        # user_input = test_input()
        self.assertTrue( == "email@email.com", "Should be email@email.com")


if __name__ == "__main__":
    unittest.main()
    







