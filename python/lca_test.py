from lca import Node, get_lca
import unittest


class LCATest(unittest.TestCase):

    def setUp(self):
        self.root = Node(50)
        self.root.left = Node(17)
        self.root.left.left = Node(9)
        self.root.left.left.right = Node(14)
        self.root.left.left.right.left = Node(12)
        self.root.left.right = Node(23)
        self.root.left.right.left = Node(19)
        self.root.right = Node(76)
        self.root.right.left = Node(54)
        self.root.right.left.right = Node(72)
        self.root.right.left.right.left = Node(67)

    def test_lca(self):
        self.assertIsNone(get_lca(None, 14, 19), "None was not returned")
        self.assertEqual(get_lca(self.root, 14, 19), 17, "Incorrect result")


if __name__ == '__main__':
    unittest.main()
