class HTMLNode:
    def __init__(self, tag = None, value = None, children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        propHTML = ""
        if self.props == None:
            return propHTML
        for prop in self.props:
           propHTML += f" {prop}=\"{self.props[prop]}\""
        return propHTML
    
