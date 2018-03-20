import unittest

from translateyoudao.translate import translate, request_api


class TestTranlate(unittest.TestCase):
    def test_translate(self):
        results = translate('hello', '你好')
        for result in results:
            self.assertNotEqual(result, False)

    def test_request_api(self):
        result = request_api('hello')
        self.assertNotEqual(result, False)


if __name__ == '__main__':
    unittest.main()
