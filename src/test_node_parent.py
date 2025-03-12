import unittest

from node_parent import NodeParent
from node_leaf import NodeLeaf

class TestNodeParent(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = NodeLeaf("span", "child")
        parent_node = NodeParent("div", [child_node])

        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = NodeLeaf("b", "grandchild")
        child_node = NodeParent("span", [grandchild_node])
        parent_node = NodeParent("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_childre(self):
        node = NodeParent(
            "p",
            [
                NodeLeaf("b", "Bold text"),
                NodeLeaf(None, "Normal text"),
                NodeLeaf("i", "italic text"),
                NodeLeaf(None, "Normal text"),
            ],
        )
        
        html_code = node.to_html()
        self.assertEqual(html_code, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_no_tag(self):
        grandchild_node = NodeLeaf("b", "grandchild")
        parent_node = NodeParent(None, [grandchild_node])

        with self.assertRaises(ValueError):
            value = parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = NodeParent("p", None)

        with self.assertRaises(ValueError):
            value = parent_node.to_html()
            
if __name__ == "__main__":
    unittest.main()