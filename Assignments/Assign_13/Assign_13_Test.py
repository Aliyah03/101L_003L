import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):

    # TEST 1
    def test_total_return_total_of_list(self):
        result=Grades.total([1,10,22])
        self.assertEqual(result, 33, "The total function should return 33")

    # TEST 2
    def test_total_return_0(self):
        result=Grades.total([])
        self.assertEqual(result, 0, "The total function should return 0")

    # TEST 3
    def test_average_one(self):
        result=Grades.average([2,5,9])
        self.assertAlmostEqual(result, 5.3333, 3, "The average function should return 5.3333")

    # TEST 4
    def test_average_two(self):
        result=Grades.average([2,15,22,9])
        self.assertAlmostEqual(result, 12, 4,"The average function should return 12")

    # TEST 5
    def test_average_returns_nan(self):
        result=Grades.average([])
        self.assertIs(math.nan, result, "the average function should return nan when passed an empty list")

    # TEST 6
    def test_median_one(self):
        result=Grades.median([2,5,1])
        self.assertEqual(result, 2)

    # TEST 7
    def test_median_two(self):
        result=Grades.median([5,2,1,3])
        self.assertEqual(result, 2.5)

    # TEST 8
    def test_median_returns_ValueError(self):
        with self.assertRaises(ValueError):
            result=Grades.median([])



unittest.main()