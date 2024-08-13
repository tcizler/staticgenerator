from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self,children,tag = None,props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("node is missing a tag")
        if self.children == None:
            raise ValueError("node has no children")
        childrenHTML = ""
        for node in self.children:
            childrenHTML += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{childrenHTML}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, children: {self.children} , {self.props})"

    
t = ParentNode([
        LeafNode("Bold text", "b"),
        LeafNode("Normal text", None),
        LeafNode("italic text", "i", {"style":".stinky"}),
        LeafNode("Normal text", None),
    ],    
    "p"
)
print(t.to_html())