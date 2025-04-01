from node_html import NodeHtml
from node_text_to_node_html import HtmlTagType

class NodeParent(NodeHtml):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self:NodeHtml):
        if self.tag is None:
            raise ValueError("missing tag value")
        if self.children is None:
            raise ValueError("missing children")
        
        html_code = f"<{self.tag}>"

        for child in self.children:
            if isinstance(child, list):
                for sub_child in child:
                    html_code += sub_child.to_html()
            else:
                html_code += child.to_html()

        html_code += f"</{self.tag}>"

        return html_code