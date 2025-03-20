import unittest

from node_text import TextType, NodeText

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_text_node_default(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        text_node_list = text_to_text_node(text)

        self.assertEqual(text_node_list,
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

if __name__ == "__main__":
    unittest.main()
