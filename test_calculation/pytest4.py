import pytest
import calculation

# pytestでのsetupとteardown
class TestCal(object): # pytestでclassを使う場合
    def setup_method(self, method): # 引数にmethod
        print('method={}'.format(method.__name__))
        self.cal = calculation.Cal()

    def tearDown_method(self, method): # 引数にmethod
        print('method={}'.format(method.__name__))
        del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4 # assertだけでよい, calの宣言不要

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError): # pytest.raises
            self.cal.add_num_and_double('1', '1') # calの宣言不要