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


def main():
    root = Node(50)
    root.left = Node(17)
    root.left.left = Node(9)
    root.left.left.right = Node(14)
    root.left.left.right.left = Node(12)
    root.left.right = Node(23)
    root.left.right.left = Node(19)
    root.right = Node(76)
    root.right.left = Node(54)
    root.right.left.right = Node(72)
    root.right.left.right.left = Node(67)

    print(f"The LCA of 14 and 19 should be 17, and was found to be {get_lca(root, 14, 19)}")


if __name__ == '__main__':
    main()
