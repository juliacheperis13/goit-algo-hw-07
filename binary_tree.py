class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Tree:
    root = None

    def insert(self, key):
        self.root = self.__insert(self.root, key)

    def insert_items(self, items):
        for item in items:
            self.insert(item)

    def min_value_node(self):
        current = self.root

        if current is not None:
            while current.left:
                current = current.left
            return current
        else:
            return None

    def max_value_node(self):
        current = self.root

        if current is not None:
            while current.right:
                current = current.right
            return current
        else:
            return None

    def total_sum(self):
        return self.__total_sum(self.root)

    def __total_sum(self, node):
        if node is not None:
            return node.val + self.__total_sum(node.left) + self.__total_sum(node.right)
        else:
            return 0

    def __insert(self, node, key):
        if node is None:
            return Node(key)
        else:
            if key < node.val:
                node.left = self.__insert(node.left, key)
            else:
                node.right = self.__insert(node.right, key)
        return node
