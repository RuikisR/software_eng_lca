# Python Implementation of LCA
# Raivo Ruikis
# 17330501

class Node:
    def __init__(self, key):
        self.key = key
        self._children = [None, None]

    def add_child(self, child):
        if self._children[0] is None:
            self._children = []
        if isinstance(child, Node):
            self._children.append(child)
        else:
            self._children.append(Node(child))

    @property
    def children(self):
        c = []
        for child in self._children:
            if child is not None:
                c.append(child)
        return c

    @property
    def left(self):
        return self._children[0]

    @property
    def right(self):
        return self._children[1]

    @left.setter
    def left(self, left_child):
        self._children[0] = left_child

    @right.setter
    def right(self, right_child):
        self._children[1] = right_child

    def __repr__(self):
        return f"Node({self.key})"


def get_path(root, n, depth=0):
    if root is None:
        return None
    current = (root, depth)
    if root.key == n:
        return [[current]]
    paths = []
    for child in root.children:
        sub_paths = get_path(child, n, depth + 1)
        print(sub_paths)
        if sub_paths:
            for p in sub_paths:
                paths.append(p)
                paths[-1].insert(0, current)
    if len(paths) == 0:
        return None
    return paths


def get_lca(root, n1, n2):
    paths_n1 = get_path(root, n1)
    paths_n2 = get_path(root, n2)
    print(paths_n1)
    print(paths_n2)
    if paths_n1 is None or paths_n2 is None:
        return None

    path_n1 = paths_n1[0]
    path_n2 = paths_n2[0]
    for i in range(min(len(path_n1), len(path_n2))):
        if path_n1[i] != path_n2[i]:
            return path_n1[i - 1]
