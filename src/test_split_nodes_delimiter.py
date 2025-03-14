import unittest

from split_nodes_delimiter import split_nodes_delimiter
from node_text import NodeText,TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_default_code(self):
        node = NodeText("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertListEqual( new_nodes,[NodeText("This is text with a ", TextType.TEXT),NodeText("code block", TextType.CODE),NodeText(" word", TextType.TEXT)])

if __name__ == "__main__":
    unittest.main()
