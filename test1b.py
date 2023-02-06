import unittest

from NumberList import NumberList
from MeanAndVariance import mean, variance

class Test1b(unittest.TestCase):
    def test_mean(self):
        data = [1, 2, 3, 7, 10.5, 2.5, 2]
        result = mean(data)
        self.assertEqual(result, 4, 'Should be 4')

    def test_variance(self):
        data = [-2, -1, 0, 1, 2, 3, 4, 5]
        result = variance(data)
        self.assertEqual(result, 6, 'should be 6')

if __name__ == '__main__':
    unittest.main()