import unittest
import list_avg

class testCaseListAvg(unittest.TestCase):
        def test_normal_list(self):
                self.assertEqual(list_avg.avg([2,4,6]), 4)
        def test_empty_list(self):
                self.assertEqual(list_avg.avg([]), 0)
        def test_type_error(self):
                self.assertRaises(TypeError, list_avg.avg, 5) #invalid type of input


if __name__ == '__main__':
        unittest.main()
