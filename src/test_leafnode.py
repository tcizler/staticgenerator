import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_one_attr(self):
        leaf = LeafNode("Click", "a", {"href":"https://google.com"})
        self.assertEqual(leaf.to_html(),"<a href=\"https://google.com\">Click</a>")         

    def test_multiple_attr(self):
        node = LeafNode("This is a title","h1",{"Attr":"value", "Attr2":"value2"})
        self.assertEqual(node.props_to_html()," Attr=\"value\" Attr2=\"value2\"")

    def test_to_html_no_props(self):
        leaf = LeafNode("This is a header", "h1")
        self.assertEqual(leaf.to_html(),"<h1>This is a header</h1>")        


if __name__ == "__main__":
    unittest.main()


