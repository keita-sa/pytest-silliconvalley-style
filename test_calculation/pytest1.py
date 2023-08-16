import pytest
import calculation

def test_add_num_and_double():
    cal = calculation.Cal()
    assert cal.add_num_and_double(1, 1) == 4

# def test_add_num_and_double():
#     cal = calculation.Cal()
#     assert cal.add_num_and_double(1, 1) == 4
#
# class CalTest(unittest.TestCase):
#     def test_add_num_and_double(self):
#         cal = calculation.Cal()
#         self.assertEqual(cal.add_num_and_double(1, 1), 4)