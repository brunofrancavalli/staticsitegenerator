from enum import Enum

class TextType(Enum):
<<<<<<< HEAD
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"
    LINK = "[]()"
    IMAGE = "![]()"

class TextNode:
    def __init__(self, text, text_type, url = None):
=======
    BOLD_TEXT = "**"
    ITALIC_TEXT = "_"
    CODE_TEXT = "`"
    LINK_FORMAT = "[]()"
    IMAGE_FORMAT = "![]()"

class TextNode:
    def __init__(self, text, text_type, url):
>>>>>>> c8fe633c41a00511a05e53283d0b83570f25273e
        self.text = text
        self.text_type = text_type
        self.url = url
    
<<<<<<< HEAD
    def __eq__(self, other):
        return True
=======
    def __eq__():
        return TRUE
>>>>>>> c8fe633c41a00511a05e53283d0b83570f25273e
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

    