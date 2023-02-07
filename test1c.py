import unittest

from Shapes import Shape, ShapeList

class Test1c(unittest.TestCase):
    def test_input_choice_exception(self):
        
    
    def test_mean(self):
        data = [1, 2, 3, 7, 10.5, 2.5, 2]
        result = mean(data)
        self.assertEqual(result, 4, 'Should be 4')



if __name__ == '__main__':
    unittest.main()