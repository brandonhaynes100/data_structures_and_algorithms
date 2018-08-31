class Node:
    def __init__(self, val, data=None, left=None, right=None):
        self.value = val
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        pass

    def __repr__(self):
        pass


class BinaryTree:
    def __init__(self, interable=None):
        self.root = None

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, value):
        pass

    def in_order(self, callable=lambda node: print(node)):
        """Go left, visit, then go right
        """
        # underscore means helper method
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left is not None:
                _walk(node.left)

            # Visit
            callable(node)

            # Go right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """Visit, go left, then go right
        """
        # underscore means helper method
        def _walk(node=None):
            if node is None:
                return

            # Visit
            callable(node)

            # Go left
            if node.left is not None:
                _walk(node.left)

            # Go right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
        """Go left, then go right, visit
        """
        # underscore means helper method
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left is not None:
                _walk(node.left)

            # Go right
            if node.right is not None:
                _walk(node.right)

            # Visit
            callable(node)

        _walk(self.root)