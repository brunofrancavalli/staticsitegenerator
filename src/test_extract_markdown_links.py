import unittest

from extract_markdown_links import extract_markdown_links

class test_extract_markdown_links(unittest.TestCase):
    def test_url_link_2entries(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_url_link_1entry(self):
        text = "This is text with a link to boot dev and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_url_link_0entries(self):
        text = "This is text with a link to boot dev and to youtube"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])
    
    
if __name__ == "__main__":
    unittest.main()