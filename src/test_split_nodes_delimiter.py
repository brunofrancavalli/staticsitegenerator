import unittest

from split_nodes_delimiter import split_nodes_delimiter
from node_text import NodeText,TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_default_code(self):
        node = NodeText("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual( new_nodes,[NodeText("This is text with a ", TextType.TEXT),NodeText("code block", TextType.CODE),NodeText(" word", TextType.TEXT)])

    def test_default_bold(self):
        node = NodeText("This is text with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual( new_nodes,[NodeText("This is text with a ", TextType.TEXT),NodeText("code block", TextType.BOLD),NodeText(" word", TextType.TEXT)])

    def test_default_italic(self):
        node = NodeText("This is text with a _code block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual( new_nodes,[NodeText("This is text with a ", TextType.TEXT),NodeText("code block", TextType.ITALIC),NodeText(" word", TextType.TEXT)])
    
    def test_default_code_at_start(self):
        node = NodeText("`code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual( new_nodes,[NodeText("code block", TextType.CODE),NodeText(" word", TextType.TEXT)])

    def test_default_code_at_end(self):
        node = NodeText("This is text with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual( new_nodes,[NodeText("This is text with a ", TextType.TEXT),NodeText("code block", TextType.CODE)])

    def test_default_code_with_spaces_at_start(self):
        node = NodeText("  `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual( new_nodes,[NodeText("  ", TextType.TEXT),NodeText("code block", TextType.CODE),NodeText(" word", TextType.TEXT)])

    def test_default_code_with_spaces_at_end(self):
        node = NodeText("This is text with a `code block`  ", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual( new_nodes,[NodeText("This is text with a ", TextType.TEXT),NodeText("code block", TextType.CODE),NodeText("  ", TextType.TEXT)])

    def test_default_code_no_closing_delimiter(self):
        node = NodeText("This is text with a `code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual( new_nodes,[NodeText("This is text with a ", TextType.TEXT),NodeText("code block word", TextType.CODE)])

if __name__ == "__main__":
    unittest.main()
