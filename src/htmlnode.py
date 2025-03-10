class HtmlNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        value = ""
        if self.props != None:
            for prop_item in self.props:
                value += f" {prop_item[0]}={prop_item[1]}"
        return value
    
    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"       