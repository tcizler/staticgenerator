import unittest

from textnode import TextNode,text_node_to_html_node
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://google.com")
        node2 = TextNode("This is a text node", "bold", "https://google.com")
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text is different", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_uneq_url(self):
        node = TextNode("This is a text node", "bold", "https://google.com")
        node2 = TextNode("This is a text node", "bold",)
        self.assertNotEqual(node, node2)
        
    def test_convert_node_plaintext(self):
        text_node = TextNode("This is a plain boring text","text",None)
        leaf_node = LeafNode("This is a plain boring text")
        self.assertEqual(text_node_to_html_node(text_node),leaf_node)
        
    #def test_convert_node_b(self):
     #   text_node = TextNode("Text","bold",None)
     #  leaf_node = LeafNode("Text","b")
     #  self.assertEqual(text_node_to_html_node(text_node),leaf_node)


if __name__ == "__main__":
    unittest.main()