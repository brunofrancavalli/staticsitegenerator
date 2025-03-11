from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag, children,props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag value")
        if self.children is None:
            raise ValueError("missing children")
        
        html_code = f"<{tag}>"
        for child in children:
            html_code += child.to_html()
        html_code += f"</{tag}>"

        return html_code