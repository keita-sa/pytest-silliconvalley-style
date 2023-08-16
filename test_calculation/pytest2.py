import calculation

class TestCal(object): # pytestでclassを使う場合
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1, 1) == 4 # assertだけでよい