import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_childre(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        
        html_code = node.to_html()
        self.assertEqual(html_code, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_no_tag(self):
        grandchild_node = LeafNode("b", "grandchild")
        parent_node = ParentNode(None, [grandchild_node])

        with self.assertRaises(ValueError):
            value = parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = ParentNode("p", None)

        with self.assertRaises(ValueError):
            value = parent_node.to_html()
            
if __name__ == "__main__":
    unittest.main()