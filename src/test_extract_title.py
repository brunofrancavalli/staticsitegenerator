import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_hello(self):
        value = extract_title("# Hello")
        self.assertEqual(value, "Hello")

    def test_extract_title_hello(self):
        value = extract_title("#   Hello")
        self.assertEqual(value, "Hello")

    def test_extract_title_hello(self):
        value = extract_title("#Hello")
        self.assertEqual(value, "Hello")
    
    def test_extract_title_hello(self):
        with self.assertRaises(ValueError):
            extract_title("Hello")
            
if __name__ == "__main__":
    unittest.main()