class BinarySearchTree:
    class Node:

        def __init__(self, value, parent=None):
            self.parent = parent
            self.left = None
            self.right = None
            self.value = value

    def __init__(self):
        self.root = None

    def add_node(self, value: int):
        if self.root is None:
            self.root = self.Node(value=value, parent=None)
            return

        def internal(parent, value_):
            if value_ <= parent.value:
                if parent.left is None:
                    parent.left = self.Node(value_, parent)
                else:
                    internal(parent.left, value_)

            if parent.value < value_:
                if parent.right is None:
                    parent.right = self.Node(value_, parent)
                else:
                    internal(parent.right, value_)

        return internal(self.root, value)

    def traverse(self, reverse=False):
        def internal(parent):
            if parent is None:
                return

            if reverse:
                yield from internal(parent.right)
            else:
                yield from internal(parent.left)

            yield parent.value

            if reverse:
                yield from internal(parent.left)
            else:
                yield from internal(parent.right)

        return internal(self.root)
