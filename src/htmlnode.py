class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        value = ""
        for prop_item in self.props:
            value += f"{prop_item[0]}={prop_item[1]} "
        return value


        