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
        
        add_pre = False
        # is this a block?
        if len(self.children) == 1:
            if self.children[0].tag == HtmlTagType.CODE:
                add_pre = True
        
        html_code = f"<{self.tag}>"

        if(add_pre):
            html_code += "<pre>"

        for child in self.children:
            html_code += child.to_html()

        if(add_pre):
            html_code += "</pre>"

        html_code += f"</{self.tag}>"

        return html_code