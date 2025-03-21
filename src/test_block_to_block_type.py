import unittest

from block_to_block_type import block_to_block_type
from block import BlockType

class test_extract_markdown_images(unittest.TestCase):
    def test_block_to_block_default(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph"), BlockType.PARAGRAPH)
    
    def test_block_to_block_heading_fail(self):
        self.assertEqual(block_to_block_type("#Just a normal paragraph"), BlockType.PARAGRAPH)

    def test_block_to_block_heading_1(self):
        self.assertEqual(block_to_block_type("# Just a normal heading"), BlockType.HEADING)

    def test_block_to_block_heading_2(self):
        self.assertEqual(block_to_block_type("## Just a normal heading"), BlockType.HEADING)
    
    def test_block_to_block_heading_6(self):
        self.assertEqual(block_to_block_type("###### Just a normal heading"), BlockType.HEADING)

    def test_block_to_block_heading_7_fail(self):
        self.assertEqual(block_to_block_type("####### Just a normal paragraph"), BlockType.PARAGRAPH)
    
    def test_block_to_block_code_correct(self):
        self.assertEqual(block_to_block_type("```Just a code area```"), BlockType.CODE)

    def test_block_to_block_code_missingstart(self):
        self.assertEqual(block_to_block_type("``Just a normal paragraph```"), BlockType.PARAGRAPH)

    def test_block_to_block_code_extraonstart(self):
        self.assertEqual(block_to_block_type("extra```Just a normal paragraph```"), BlockType.PARAGRAPH)

    def test_block_to_block_code_extraonend(self):
        self.assertEqual(block_to_block_type("```Just a normal paragraph```extra"), BlockType.PARAGRAPH)
    
    def test_block_to_block_code_missingend(self):
        self.assertEqual(block_to_block_type("```Just a normal paragraph``"), BlockType.PARAGRAPH)
    
    def test_block_to_block_quote(self):
        self.assertEqual(block_to_block_type("> Just a quote"), BlockType.QUOTE)
    
    def test_block_to_block_quote_space_on_the_start_of_line(self):
        self.assertEqual(block_to_block_type(" > Just an quote with issues"), BlockType.PARAGRAPH)

    def test_block_to_block_unordered_list(self):
        self.assertEqual(block_to_block_type("- Just an unordered list"), BlockType.UNORDERED_LIST)
    
    def test_block_to_block_unordered_list_space_on_the_start_of_line(self):
        self.assertEqual(block_to_block_type(" - Just an unordered list with issues"), BlockType.PARAGRAPH)

    def test_block_to_block_unordered_list_space_on_the_start_of_line(self):
        self.assertEqual(block_to_block_type("-Just an unordered list with issues"), BlockType.PARAGRAPH)

    def test_block_to_block_ordered_list(self):
        self.assertEqual(block_to_block_type("1. Just an ordered list"), BlockType.ORDERED_LIST)

    def test_block_to_block_ordered_list_two_characters(self):
        self.assertEqual(block_to_block_type("12. Just an ordered list"), BlockType.PARAGRAPH)

    def test_block_to_block_ordered_list_five_characters(self):
        self.assertEqual(block_to_block_type("122343. Just an ordered list"), BlockType.PARAGRAPH)

    def test_block_to_block_ordered_list_space_fail(self):
        self.assertEqual(block_to_block_type(" 122343. Just an ordered list"), BlockType.PARAGRAPH)

    def test_block_to_block_ordered_list_nospace_fail(self):
        self.assertEqual(block_to_block_type("122343.Just an ordered list"), BlockType.PARAGRAPH)
    
    def test_block_to_block_ordered_list_space_on_the_start_of_line(self):
        self.assertEqual(block_to_block_type(" 1. Just a quote with issues"), BlockType.PARAGRAPH)
    
    def test_block_to_block_ordered_list_multiline(self):
        self.assertEqual(block_to_block_type("1. Just an ordered list\n2. Second line\n3. third line"), BlockType.ORDERED_LIST)

    def test_block_to_block_ordered_list_multiline_outoforder(self):
        self.assertEqual(block_to_block_type("1. Just an ordered list\n3. Second line\n4. third line"), BlockType.PARAGRAPH)
    
if __name__ == "__main__":
    unittest.main()