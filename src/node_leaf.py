from node_html import NodeHtml

class NodeLeaf(NodeHtml):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        html_string = ""

        # open tag if one exist
        if self.tag is not None and self.tag:
            html_string += f"<{self.tag}>"
        # middle part
        html_string += self.value

        # close tag if one exist
        if self.tag is not None and self.tag:
            html_string += f"</{self.tag}>"

        return html_string
