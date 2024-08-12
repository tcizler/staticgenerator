from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value ,tag = None, props = None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value == None:
            raise ValueError("node is missing a value")
        if self.tag == None:
            return self.value
        attrs = self.props_to_html()
        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"
    