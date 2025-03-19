import unittest

from split_nodes import split_nodes_link
from node_text import TextType, NodeText

class TestSplitNodesImage(unittest.TestCase):
    def test_split_links_text_no_links(self):
        node = NodeText(
            "This text has no links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("This text has no links", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_text_has_link_only(self):
        node = NodeText(
            "[link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )
    
    def test_split_links_text_before(self):
        node = NodeText(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("This is text with an ", TextType.TEXT),
                NodeText("link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_split_links_text_before_middle_after(self):
        node = NodeText(
            "[link](https://i.imgur.com/zjjcJKZ.png) no more links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText(" no more links", TextType.TEXT)
            ],
            new_nodes,
        )
    
    def test_split_links_text_before_after(self):
        node = NodeText(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) no more links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("This is text with an ", TextType.TEXT),
                NodeText("link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText(" no more links", TextType.TEXT)
            ],
            new_nodes,
        )
        
    def test_split_links_two_link(self):
        node = NodeText(
            "[link](https://i.imgur.com/zjjcJKZ.png)[second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText("second link", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes,
        )

    def test_split_links_two_link_middle(self):
        node = NodeText(
            "[link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText(" and another ", TextType.TEXT),
                NodeText("second link", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes,
        )
        
    def test_split_links_text_before_two_links(self):
        node = NodeText(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)[second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("This is text with an ", TextType.TEXT),
                NodeText("link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText("second link", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes,
        )

    def test_split_links_text_two_links_after(self):
        node = NodeText(
            "[link](https://i.imgur.com/zjjcJKZ.png)[second link](https://i.imgur.com/3elNhQu.png) no more links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText("second link", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                NodeText(" no more links", TextType.TEXT)
            ],
            new_nodes,
        )


    def test_split_links_text_before_middle_after(self):
        node = NodeText(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png) no more links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("This is text with an ", TextType.TEXT),
                NodeText("link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText(" and another ", TextType.TEXT),
                NodeText("second link", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                NodeText(" no more links", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_links_text_before_middle(self):
        node = NodeText(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                NodeText("This is text with an ", TextType.TEXT),
                NodeText("link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText(" and another ", TextType.TEXT),
                NodeText("second link", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
