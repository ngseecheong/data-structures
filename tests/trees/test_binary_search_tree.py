import random

from trees import BinarySearchTree


def assert_traverse_order(item_list, bst: BinarySearchTree):
    for i, j in zip(item_list, bst.traverse()):
        assert i == j

    for i, j in zip(item_list[::-1], bst.traverse(True)):
        assert i == j


def test_insert_ordered():
    bst = BinarySearchTree()

    item_list = list(range(10))

    for item in item_list:
        bst.add_node(item)

    assert_traverse_order(item_list, bst)


def test_insert_random():
    bst = BinarySearchTree()

    item_list = list(range(10))

    shuffled_item_list = item_list[:]
    random.shuffle(shuffled_item_list)

    for item in shuffled_item_list:
        bst.add_node(item)

    assert_traverse_order(item_list, bst)
