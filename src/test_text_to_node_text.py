import unittest

from node_text import TextType, NodeText
from text_to_node_text import text_to_node_text

class TestTextToNodeText(unittest.TestCase):
    def test_text_to_text_node_default(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        node_text_list = text_to_node_text(text)

        self.assertEqual(node_text_list,
            [
                NodeText("This is ", TextType.TEXT),
                NodeText("text", TextType.BOLD),
                NodeText(" with an ", TextType.TEXT),
                NodeText("italic", TextType.ITALIC),
                NodeText(" word and a ", TextType.TEXT),
                NodeText("code block", TextType.CODE),
                NodeText(" and an ", TextType.TEXT),
                NodeText("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                NodeText(" and a ", TextType.TEXT),
                NodeText("link", TextType.LINK, "https://boot.dev")
            ])
        
    def test_text_to_text_node_bold_inside_code(self):
        text = "text before `code block **bold should not work**` text after"

        node_text_list = text_to_node_text(text)

        self.assertEqual(node_text_list,
            [
                NodeText("text before ", TextType.TEXT),
                NodeText("code block **bold should not work**", TextType.CODE),
                NodeText(" text after", TextType.TEXT),
            ])
        
    def test_text_to_text_node_link_inside_code(self):
        text = "text before `code block [should not link](https://boot.dev)` text after"

        node_text_list = text_to_node_text(text)

        self.assertEqual(node_text_list,
            [
                NodeText("text before ", TextType.TEXT),
                NodeText("code block [should not link](https://boot.dev)", TextType.CODE),
                NodeText(" text after", TextType.TEXT),
            ])

if __name__ == "__main__":
    unittest.main()
