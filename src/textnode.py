from leafnode import LeafNode


class TextNode:
    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(text_node.text, None)
    elif text_node.text_type == "bold":
        return LeafNode(text_node.text,"b")
    elif text_node.text_type == "italic":
        return LeafNode(text_node.text,"i")
    elif text_node.text_type == "code":
        return LeafNode(text_node.text,"code")
    elif text_node.text_type == "link":
        return LeafNode(text_node.text,"a",{"href":text_node.url})
    elif text_node.text_type == "image":
        return LeafNode("","img",{"alt":text_node.text,"src":text_node.url})
    else:
        raise ValueError("invalid text type")
    

