import unittest
import test.test_sample
import test.test_sample2
import test.test_sample3

class TestRunner(unittest.TestCase):

    def test_runner(self):
        test_suite = unittest.TestSuite() # unittest.TestSuite()オブジェクトを生成

        # testクラスを見つけ出す
        tests = unittest.defaultTestLoader.discover("test", pattern="test_*.py")

        # 見つけたtestクラスを追加する
        test_suite.addTest(tests)
        unittest.TextTestRunner().run(test_suite) # TextTestRunner().run()が呼び出されるとaddしたテストクラスが実行される

        # test_suite.addTest(unittest.makeSuite(test.test_sample.TestSample)) # addTestでテストクラスを指定
        # test_suite.addTest(unittest.makeSuite(test.test_sample2.TestSample2))
        # test_suite.addTest(unittest.makeSuite(test.test_sample3.TestSample3))

