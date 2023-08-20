import pytest

import calculation

# pytestの例外処理
class TestCal(object): # pytestでclassを使う場合
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1, 1) == 4 # assertだけでよい

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError): # pytest.raises
            cal = calculation.Cal()
            cal.add_num_and_double('1', '1')