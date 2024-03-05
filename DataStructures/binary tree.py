class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def _print_tree(self, root, level, prefix):
        if root is not None:
            self._print_tree(root.right, level + 1, "R")
            print("  " * level + f"{prefix} -> {root.key}")
            self._print_tree(root.left, level + 1, "L")

    def _pre_order(self, root):
        if root:
            print(root.key, end=" ")
            self._pre_order(root.left)
            self._pre_order(root.right)

    def _post_order(self, root):
        if root:
            self._post_order(root.left)
            self._post_order(root.right)
            print(root.key, end=" ")

    def _in_order(self, root):
        if root:
            self._in_order(root.left)
            print(root.key, end=" ")
            self._in_order(root.right)

    def print_tree(self):
        print("Tree:")
        self._print_tree(self.root, 0, "Root")

    def pre_order(self):
        print("Pre-order Traversal:")
        self._pre_order(self.root)
        print()

    def post_order(self):
        print("Post-order Traversal:")
        self._post_order(self.root)
        print()

    def in_order(self):
        print("In-order Traversal:")
        self._in_order(self.root)
        print()

# Example usage:
binary_tree = BinaryTree()

# Insert nodes
binary_tree.insert(5)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(2)
binary_tree.insert(4)

# Print the tree
binary_tree.print_tree()

# Print traversals
binary_tree.pre_order()
binary_tree.post_order()
binary_tree.in_order()
