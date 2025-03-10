import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD,"https://google.com")
        self.assertEqual(node, node2)

    # need to add more tests here
    def test_ne_name(self):
        node = TextNode("This is a text node 1", TextType.BOLD)
        node2 = TextNode("This is a text node 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_ne_name(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_ne_url(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD,"https://bing.com")
        self.assertNotEqual(node, node2)
    
    def test_checkvalues(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://google.com")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertEqual(node.url,"https://google.com")


if __name__ == "__main__":

    unittest.main()