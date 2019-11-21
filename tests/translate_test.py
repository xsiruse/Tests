import unittest
from unittest.mock import patch

from src.translate import translate_it


class MyTestCase(unittest.TestCase):

    text = 'hello'
    @patch('src.translate.input', return_value=text)
    def test_translate(self, text):
        result = translate_it('en', 'ru')
        self.assertEqual(result['text'][0], 'привет')
        self.assertEqual(result['code'], 200)


if __name__ == '__main__':
    unittest.main()
