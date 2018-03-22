import unittest

from translateyoudao.translate import translate, request_api


class TestTranlate(unittest.TestCase):
    def test_translate(self):
        results = translate('pretty', '再见')
        self.assertEqual(results, {'再见': 'goodbye', 'pretty': '漂亮的'})

    def test_request_api(self):
        result = request_api('hello')
        self.assertEqual(result, '你好')

    def test_diy_translate(self):
        results = translate('你好', '再见', word_from='zh-CHS', word_to='ja')
        self.assertEqual(results, {'你好': 'こんにちは', '再见': 'さようなら'})

    def test_diy_request_api(self):
        result = request_api('你好', word_from='zh-CHS', word_to='ja')
        self.assertEqual(result, 'こんにちは')


if __name__ == '__main__':
    unittest.main()
