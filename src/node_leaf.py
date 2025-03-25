from node_html import NodeHtml

class NodeLeaf(NodeHtml):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        html_string = ""
        if self.tag is not None:
            html_string += f"<{self.tag.value}>"
        html_string += self.value
        if self.tag is not None:
            html_string += f"</{self.tag.value}>"

        return html_string
