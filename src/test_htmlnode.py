import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_one_attr(self):
        node = HTMLNode("h1","This is a title",None,{"Attr":"value"})
        self.assertEqual(node.props_to_html()," Attr=\"value\"")         

    def test_multiple_attr(self):
        node = HTMLNode("h1","This is a title",None,{"Attr":"value", "Attr2":"value2"})
        self.assertEqual(node.props_to_html()," Attr=\"value\" Attr2=\"value2\"")

    def test_to_html(self):
        node = HTMLNode("h1","This is a title",[],{"Attr":"value"})
        self.assertRaises(NotImplementedError,node.to_html)      

    def test_to_html_none(self):
        node = HTMLNode("h1","This is a title",None,None)
        self.assertEqual(node.props_to_html(),"")    
if __name__ == "__main__":
    unittest.main()


