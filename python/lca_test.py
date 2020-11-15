from lca import Node, get_lca
import unittest


class LCATest(unittest.TestCase):

    def setUp(self):
        self.root1 = Node(50)
        self.root1.left = Node(17)
        self.root1.left.left = Node(9)
        self.root1.left.left.right = Node(14)
        self.root1.left.left.right.left = Node(12)
        self.root1.left.right = Node(23)
        self.root1.left.right.left = Node(19)
        self.root1.right = Node(76)
        self.root1.right.left = Node(54)
        self.root1.right.left.right = Node(72)
        self.root1.right.left.right.left = Node(67)

        self.nodes = [Node(i) for i in range(1, 8)]
        self.nodes[0].add_child(self.nodes[1])
        self.nodes[0].add_child(self.nodes[2])
        self.nodes[1].add_child(self.nodes[3])
        self.nodes[1].add_child(self.nodes[4])
        self.nodes[2].add_child(self.nodes[5])
        self.nodes[3].add_child(self.nodes[6])
        self.nodes[4].add_child(self.nodes[6])
        self.nodes[5].add_child(self.nodes[4])
        self.nodes[6].add_child(self.nodes[6])

    def test_lca(self):
        self.assertIsNone(get_lca(None, 14, 19), "None was not returned")
        # self.assertEqual(get_lca(self.root1, 14, 19), 17, "Incorrect result")
        self.assertEqual(get_lca(self.nodes[0], 3, 4), 1, "Incorrect result")


if __name__ == '__main__':
    unittest.main()
