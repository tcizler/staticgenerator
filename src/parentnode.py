from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(children,tag = None,props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("node is missing a tag")
        if self.children == None:
            raise ValueError("node has no children")
        output = ""
        for node in self.children:
            if node.tag != None:
                output += f"<{node.tag}{node.props_to_html()}>{node.value}</{node.tag}>"
            else:
                output += f"{node.value}"
        return output

## add Repr ##    

    
t = ParentNode([
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],    
    "p"
)
print(t)