from node_html import NodeHtml
from node_text_to_node_html import HtmlTagType

class NodeParent(NodeHtml):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag value")
        if self.children is None:
            raise ValueError("missing children")
        
        html_code = f"<{self.tag}>"

        for child in self.children:
            html_code += child.to_html()

        html_code += f"</{self.tag}>"

        return html_code