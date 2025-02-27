from enum import Enum

class TextType(Enum):
    BOLD_TEXT = "**"
    ITALIC_TEXT = "_"
    CODE_TEXT = "`"
    LINK_FORMAT = "[]()"
    IMAGE_FORMAT = "![]()"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__():
        return TRUE
    
    