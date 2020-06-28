class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BST:
    """Simple Binary Search Tree"""

    def __init__(self):
        self.root = None

    def insert(self, key, node=None):
        if node is None:
            if self.root is not None:
                node = self.root
            else:
                self.root = Node(key)
                return
        if key <= node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert(key, node.right)

    def find_node_and_parent(self, key):
        node = self.root
        parent = None
        while node is not None and node.key != key:
            parent = node
            node = node.left if key <= node.key else node.right
        return node, parent

    def key_exists(self, key):
        return self.find_node_and_parent(key)[0] is not None

    def remove(self, root, key):
        # Base Case
        if root is None:
            return root

        if key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                return temp

            elif root.right is None:
                temp = root.left
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.min_val(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.remove(root.right, temp.key)

        return root

    @staticmethod
    def min_val(node):
        # loop down to find the leftmost leaf
        while node.left is not None:
            node = node.left
        return node

    def print_in_order(self, node='root'):
        if node == 'root':
            node = self.root
        if node is not None:
            self.print_in_order(node.left)
            print(node.key, end=' ')
            self.print_in_order(node.right)


if __name__ == "__main__":
    bst = BST()
    for i in [1, 3, 5, 2, 4, 6, 234, 0, -1, 3, 36756]:
        bst.insert(i)
    bst.print_in_order()
    print()
    bst.remove(bst.root, 3)
    bst.remove(bst.root, 6)
    bst.print_in_order()
