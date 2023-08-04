import unittest
from taylor import taylor_sin


class TestTaylorSin(unittest.TestCase):

    def test_taylor_sin_degree_1(self):
        # Test for degree 1
        result, _  = taylor_sin(1,0.5,0)
        self.assertAlmostEqual(result, 0.5)

    def test_taylor_sin_degree_3(self):
        # Test for degree 3
        result, _  = taylor_sin(3,1.0,0)
        self.assertAlmostEqual(result, 0.83333333)

    def test_taylor_sin_degree_5(self):
        # Test for degree 5
        result, _  = taylor_sin(5, 2.0,0)
        self.assertAlmostEqual(result, 0.933333333)



if __name__ == '__main__':
    unittest.main()

