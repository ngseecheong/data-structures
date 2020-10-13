from typing import Any, Generator, Optional


class BinarySearchTree:
    class SubTree:
        def __init__(self, min_=None):
            self.min = min_

    class Node:

        def __init__(self, value, parent=None, subtree=None):
            self.parent: Optional[BinarySearchTree.Node] = parent
            self.left: Optional[BinarySearchTree.Node] = None
            self.right: Optional[BinarySearchTree.Node] = None
            self.value: Optional[BinarySearchTree.Node] = value
            self.subtree: Optional[BinarySearchTree.SubTree] = subtree

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.root: Optional[BinarySearchTree.Node] = None

    def add_value(self, value: Any) -> Node:
        """
        A function to add values to the tree

        :param value: Any valid object that can be compared using <,>,= or any valid combinations
        :return: None
        """

        if self.root is None:
            self.root = BinarySearchTree.Node(value=value)
            self.root.subtree = BinarySearchTree.SubTree(min_=self.root)
            return self.root

        def internal(parent, value_):
            if value_ <= parent.value:
                if parent.left is None:
                    new_node = BinarySearchTree.Node(value_, parent, parent.subtree)
                    new_node.subtree.min = new_node
                    parent.left = new_node
                    return new_node
                else:
                    return internal(parent.left, value_)

            if parent.value < value_:
                if parent.right is None:
                    new_node = self.Node(value_, parent, subtree=BinarySearchTree.SubTree())
                    new_node.subtree.min = new_node
                    parent.right = new_node
                    return new_node
                else:
                    return internal(parent.right, value_)

        return internal(self.root, value)

    def traverse(self, reverse: bool = False) -> Generator:
        """
        A generator to traverse the the tree

        :param reverse: low to high (reverse=False) | high to low (reverse=True)
        :return: generator to traverse
        """
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

    def pop_min_at_parent(self, parent: Node):
        if parent is None:
            return None

        min_node: BinarySearchTree.Node = parent.subtree.min

        # Special case. We are at root. Which has no parents
        if min_node.parent is None:
            self.root = min_node.right
        else:
            # Min node has no successor on right, since this would be left most node in subtree
            # So we set the parent as min
            if min_node.right is None:
                min_node.parent.left = None
                min_node.parent.subtree.min = min_node.parent  # Cyclic
            else:
                # We have a right successor.
                if min_node.parent.left is min_node:
                    min_node.parent.left = min_node.right
                else:
                    min_node.parent.right = min_node.right
                min_node.right.parent = min_node.parent
                min_node.parent.subtree.min = min_node.right

        min_node.parent = None
        min_node.left = None
        min_node.right = None
        min_node.subtree = None

        value = min_node.value
        del min_node

        return value

    def pop_min(self) -> Any:
        """
        Gets the min value and removes it from the tree. O(1)

        :return: min value
        """

        return self.pop_min_at_parent(self.root)

    def pop_max(self) -> Any:
        """
        Gets the max value and removes it from the tree

        :return: max value
        """
        def internal(parent):
            if parent is None:
                return None

            if parent.right is None:
                if parent.parent is None:
                    self.root = parent.left
                else:
                    parent.parent.right = parent.left
                return parent.value
            else:
                return internal(parent.right)

        return internal(self.root)
