import unittest

from extract_markdown_images import extract_markdown_images

class test_extract_markdown_images(unittest.TestCase):
    def test_url_rickroll(text):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(result,[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    
if __name__ == "__main__":
    unittest.main()