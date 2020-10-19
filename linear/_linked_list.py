from typing import Optional


class Node:
    next = None

    def __init__(self, value):
        self.value = value


class LinkedList:
    head = None
    tail = None

    def add_value_end(self, value) -> Node:
        """
        Add new value to end of list. O(1) time

        :param value:
        :return:
        """
        if self.tail is None:
            self.tail = Node(value)
            self.head = self.tail
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

        return self.tail

    def add_value_start(self, value) -> Node:
        """
        Add new value to beginning of list. O(1) time

        :param value:
        :return:
        """
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

        return self.head

    def pop_value_start(self) -> Optional[Node]:
        """
        Pop value from start of list. None will be returned if empty. O(1)

        :return:
        """
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            return None
