import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        html_code = node.to_html()
        self.assertEqual(html_code, "<p>Hello, world!</p>")

    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Hello, world!")
        html_code = node.to_html()
        self.assertEqual(html_code, "Hello, world!")

if __name__ == "__main__":

    unittest.main()