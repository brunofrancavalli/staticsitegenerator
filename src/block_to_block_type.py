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
        lines = text.split('\n')
        count = 1
        increasing_count = True
        for line in lines:
            groups = re.findall(r"^(([0-9]+)\. .*)", line)
            if int(groups[0][1]) != count:
                increasing_count = False
                break
            count += 1
        if increasing_count:
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH
    else:
        return BlockType.PARAGRAPH

