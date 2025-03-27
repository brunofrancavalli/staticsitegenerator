from node_leaf import NodeLeaf
from node_text import NodeText, TextType

from enum import Enum

class HtmlTagType(Enum):
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"
    TEXT = ""

def node_text_to_node_html(node_text:NodeText):
    if node_text.text_type == TextType.TEXT:
        text = node_text.text.replace("\n"," ")
        return NodeLeaf(HtmlTagType.TEXT, text)
    elif node_text.text_type == TextType.BOLD:
        return NodeLeaf(HtmlTagType.BOLD, node_text.text)
    elif node_text.text_type == TextType.ITALIC:
        return NodeLeaf(HtmlTagType.ITALIC, node_text.text)
    elif node_text.text_type == TextType.CODE:
        return NodeLeaf(HtmlTagType.CODE, node_text.text)
    elif node_text.text_type == TextType.LINK:
        return NodeLeaf(HtmlTagType.LINK, node_text.text, [(f"href",node_text.url)])
    elif node_text.text_type == TextType.IMAGE:
        return NodeLeaf(HtmlTagType.IMAGE, None, [("src",node_text.url), ("alt",node_text.text)])
    else:
        raise ValueError(f"Invalid TextType option {node_text.text_type}")