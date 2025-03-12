import unittest

from node_text import NodeText, TextType

class TestNodeText(unittest.TestCase):
    def test_eq(self):
        node = NodeText("This is a text node", TextType.BOLD)
        node2 = NodeText("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = NodeText("This is a text node", TextType.BOLD,"https://google.com")
        node2 = NodeText("This is a text node", TextType.BOLD,"https://google.com")
        self.assertEqual(node, node2)

    def test_ne_name(self):
        node = NodeText("This is a text node 1", TextType.BOLD)
        node2 = NodeText("This is a text node 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_ne_name(self):
        node = NodeText("This is a text node", TextType.ITALIC)
        node2 = NodeText("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_ne_url(self):
        node = NodeText("This is a text node", TextType.BOLD,"https://google.com")
        node2 = NodeText("This is a text node", TextType.BOLD,"https://bing.com")
        self.assertNotEqual(node, node2)
    
    def test_checkvalues(self):
        node = NodeText("This is a text node", TextType.BOLD,"https://google.com")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertEqual(node.url,"https://google.com")





if __name__ == "__main__":

    unittest.main()