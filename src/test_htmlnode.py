import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_values(self):
        tag_value = "mytag"
        value_value = "myvalue"
        html = HtmlNode(tag_value, value_value)
        self.assertEqual(html.tag, tag_value)
        self.assertEqual(html.value, value_value)
    
    def test_tohtml_exception(self):
        tag_value = "mytag"
        value_value = "myvalue"
        html_node = HtmlNode(tag_value, value_value)

        with self.assertRaises(NotImplementedError):
            html_node.to_html()

    def test_proptohtml(self):
        tag_value = "mytag"
        value_value = "myvalue"
        html_node = HtmlNode(tag_value, value_value)

        html_code = html_node.props_to_html()

        self.assertEqual(html_code == '')

if __name__ == "__main__":

    unittest.main()