import unittest

assert 3 * 8 == 24, "Should Be 24"
'''
def test_case_one():

  assert 5 * 10 == 50, "Should Be 50"

def test_case_two():

  assert 5 * 50 == 250, "Should Be 250"

if __name__ == "__main__":

  test_case_one()
  test_case_two()

  print("All Tests Passed")

'''

class MyTestCase(unittest.TestCase):

  def test_one(self):

    self.assertTrue(100 > 99, "Should Be True")

  def test_two(self):

    self.assertEqual(40 + 60, 100, "Should Be 100")

  def test_three(self):

    self.assertGreater(100, 101, "Should Be True")

if __name__ == "__main__":

  unittest.main()