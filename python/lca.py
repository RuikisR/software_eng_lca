# Python Implementation of LCA
# Raivo Ruikis
# 17330501

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def get_path(root, n):
    if root is None:
        return None
    path = []
    path.append(root.key)
    if root.key == n:
        return path
    path_left = get_path(root.left, n)
    path_right = get_path(root.right, n)
    if path_left is not None:
        path += path_left
    elif path_right is not None:
        path += path_right
    else:
        return None
    return path


def get_lca(root, n1, n2):
    path_n1 = get_path(root, n1)
    path_n2 = get_path(root, n2)
    if path_n1 is None or path_n2 is None:
        return None

    for i in range(min(len(path_n1), len(path_n2))):
        if path_n1[i] != path_n2[i]:
            return path_n1[i - 1]
