import pytest
import calculation

# class全体の前後にsetupとteardownを入れたい場合
class TestCal(object): # pytestでclassを使う場合

    @classmethod # デコレータを追記
    def setup_class(cls): # setup_class(cls)を追記
        print('start')
        cls.cal = calculation.Cal()

    @classmethod # デコレータを追記
    def teardown_class(cls): # teardown_class(cls)を追記
        print('end')
        del cls.cal

    def setup_method(self, method): # 引数にmethod
        print('method={}'.format(method.__name__))
        # self.cal = calculation.Cal()

    def tearDown_method(self, method): # 引数にmethod
        print('method={}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4 # assertだけでよい, calの宣言不要

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError): # pytest.raises
            self.cal.add_num_and_double('1', '1') # calの宣言不要