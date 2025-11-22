# https://github.com/mdamoses-gh/lab11-MM-ZX.git
# Partner 1: Moises Miranda Manzanedo
# Partner 2: Ziyue Xu

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        assert add(1, 2) == 3
        assert add(5, 2) == 7
        assert add(12, 7) == 19

    def test_subtract(self): # 3 assertions
        assert subtract(5, 2) == 3
        assert subtract(12, 7) == 5
        assert subtract(3, 2) == 1

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        assert mul(2, 3) == 6
        assert mul(-4, 5) == -20
        assert mul(0, 10) == 0

    def test_divide(self): # 3 assertions
        assert div(2, 10) == 5
        assert div(4, 20) == 5
        assert div(-2, 10) == -5
    ###########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        assert logarithm(2, 4) == 2
        assert logarithm(5, 25) == 2
        assert logarithm(10, 1000) == 3

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
        with self.assertRaises(ValueError):
            logarithm(5, 0)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    def test_hypotenuse(self): # 3 assertions
        assert hypotenuse(3, 4) == 5
        assert hypotenuse(5, 12) == 13
        assert hypotenuse(0, 0) == 0

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
        assert square_root(9) == 3
        assert square_root(0) == 0
    ##########################
        with self.assertRaises(ValueError):
            square_root(-1)
# Do not touch this
if __name__ == "__main__":
    unittest.main()