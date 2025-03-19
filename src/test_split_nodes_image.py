import unittest

from split_nodes import split_nodes_image
from node_text import TextType, NodeText

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images_text_no_links(self):
        node = NodeText(
            "This text has no links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("This text has no links", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_text_has_link_only(self):
        node = NodeText(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )
    
    def test_split_images_text_before(self):
        node = NodeText(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("This is text with an ", TextType.TEXT),
                NodeText("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_split_images_text_before_middle_after(self):
        node = NodeText(
            "![image](https://i.imgur.com/zjjcJKZ.png) no more images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText(" no more images", TextType.TEXT)
            ],
            new_nodes,
        )
    
    def test_split_images_text_before_after(self):
        node = NodeText(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) no more images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("This is text with an ", TextType.TEXT),
                NodeText("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText(" no more images", TextType.TEXT)
            ],
            new_nodes,
        )
        
    def test_split_images_two_link(self):
        node = NodeText(
            "![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes,
        )

    def test_split_images_two_link_middle(self):
        node = NodeText(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText(" and another ", TextType.TEXT),
                NodeText("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes,
        )
        
    def test_split_images_text_before_two_links(self):
        node = NodeText(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("This is text with an ", TextType.TEXT),
                NodeText("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes,
        )

    def test_split_images_text_two_links_after(self):
        node = NodeText(
            "![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png) no more images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                NodeText(" no more images", TextType.TEXT)
            ],
            new_nodes,
        )


    def test_split_images_text_before_middle_after(self):
        node = NodeText(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) no more images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("This is text with an ", TextType.TEXT),
                NodeText("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText(" and another ", TextType.TEXT),
                NodeText("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                NodeText(" no more images", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_images_text_before_middle(self):
        node = NodeText(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                NodeText("This is text with an ", TextType.TEXT),
                NodeText("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                NodeText(" and another ", TextType.TEXT),
                NodeText("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
