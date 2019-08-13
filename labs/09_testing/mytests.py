'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.


Function Division:

# Takes two numbers and if they denominator is non zero divides the numerator by the denominator

Function PrimeNumber:

# Takes a number and decides if it is a prime number

'''

import unittest
from mycode import primenumber


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_PrimeNumber_PrimenumberAsArgument_ReturnsTrue(self):
        self.assertTrue(primenumber(37))

    def test_PrimeNumber_NonPrimenumberAsArgument_ReturnsFalse(self):
        self.assertFalse(primenumber(10))

    def test_PrimeNumber_StringAsArgument_ReturnsException(self):
        self.assertRaises(TypeError, primenumber(10))


if __name__ == '__main__':
    unittest.main()




