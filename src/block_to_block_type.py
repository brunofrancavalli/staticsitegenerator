import re

from block import BlockType

def block_to_block_type(text):
    if re.match(r"^#{1,6} ", text):
        return BlockType.HEADING
    elif re.match(r"^```.*```$", text):
        return BlockType.CODE
    elif re.match(r"^>", text):
        return BlockType.QUOTE
    elif re.match(r"- ", text):
        return BlockType.UNORDERED_LIST
    elif re.match(r"^[0-9]+\. ", text):
        groups = re.findall(r"^((1). .*(\n(\d+). .*)*)", text)
        count = 1
        increasing_count = True
        # must be increasing and first number is 1
        for group in groups:
            if int(group[0]) != count:
                increasing_count = False
                break
            count += 1
        
        if increasing_count:
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH
    else:
        return BlockType.PARAGRAPH

