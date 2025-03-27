from node_html import NodeHtml

class NodeLeaf(NodeHtml):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        html_string = ""

        # open tag if one exist
        if self.tag.value:
            html_string += f"<{self.tag.value}>"
        # middle part
        html_string += self.value

        # close tag if one exist
        if self.tag.value:
            html_string += f"</{self.tag.value}>"

        return html_string
