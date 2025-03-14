import unittest

from node_text import NodeText, TextType
from node_text_to_node_html import text_node_to_html_node, HtmlTagType

class TestNodeTextToNodeHtml(unittest.TestCase):
    def test_text(self):
        text = "This is a text node"
        node = NodeText(text, TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, HtmlTagType.TEXT)
        self.assertEqual(html_node.value, text)

    def test_bold(self):
        text = "This is a text node"
        node = NodeText(text, TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, HtmlTagType.BOLD)
        self.assertEqual(html_node.value, text)

    def test_italic(self):
        text = "This is a italic node"
        node = NodeText(text, TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, HtmlTagType.ITALIC)
        self.assertEqual(html_node.value, text)

    def test_code(self):
        text = "This is a code node"
        node = NodeText(text, TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, HtmlTagType.CODE)
        self.assertEqual(html_node.value, text)

    def test_link(self):
        text = "This is a link node"
        link = "http://www.google.com"
        node = NodeText(text, TextType.LINK, link)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, HtmlTagType.LINK)
        self.assertEqual(html_node.value, text)
        self.assertEqual(html_node.props, [("href",node.url)])

    def test_image(self):
        text = "This is a image node"
        link = "http://www.google.com"
        node = NodeText(text, TextType.IMAGE, link)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, HtmlTagType.IMAGE)
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, [("src",node.url),("alt",node.text)])

if __name__ == "__main__":
    unittest.main()