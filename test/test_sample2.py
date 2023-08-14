import unittest
from sample_lib import sample


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('***全体前処理***')

    @classmethod
    def tearDownClass(cls):
        print('***全体後処理***')

    def setUp(self):
        print('+ テスト前処理')

    def tearDown(self):
        print('+ テスト後処理')

    def test_add_num(self):
        """
        add_numの単体テスト
        """
        self.assertEqual(7, sample.add_num(3, 4))

    def test_is_positive(self):
        """
        is_numの単体テスト
        """
        self.assertTrue(sample.is_positive(3))
        self.assertFalse(sample.is_positive(0))
        self.assertFalse(sample.is_positive(-1))

