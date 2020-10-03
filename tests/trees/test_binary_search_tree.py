import random
import pytest
from trees import BinarySearchTree


def assert_traverse_order(item_list, bst: BinarySearchTree):
    for i, j in zip(item_list, bst.traverse()):
        assert i == j

    for i, j in zip(item_list[::-1], bst.traverse(True)):
        assert i == j


def test_traverse_ordered():
    bst = BinarySearchTree()

    item_list = list(range(10))

    for item in item_list:
        bst.add_value(item)

    assert_traverse_order(item_list, bst)


def test_traverse_random():
    bst = BinarySearchTree()

    item_list = list(range(10))

    shuffled_item_list = item_list[:]
    random.shuffle(shuffled_item_list)

    for item in shuffled_item_list:
        bst.add_value(item)

    assert_traverse_order(item_list, bst)


def test_traverse_empty():
    bst = BinarySearchTree()

    with pytest.raises(StopIteration):
        next(bst.traverse())


def test_pop_min_ordered():
    bst = BinarySearchTree()

    item_list = list(range(10))

    for item in item_list:
        bst.add_value(item)

    assert bst.pop_min() == 0


def test_pop_min_reverse_ordered():
    bst = BinarySearchTree()

    item_list = list(range(10))[::-1]

    for item in item_list:
        bst.add_value(item)

    assert bst.pop_min() == 0


def test_pop_min_random():
    bst = BinarySearchTree()

    item_list = list(range(10))

    shuffled_item_list = item_list[:]
    random.shuffle(shuffled_item_list)

    for item in shuffled_item_list:
        bst.add_value(item)

    assert bst.pop_min() == 0


def test_pop_min_empty():
    bst = BinarySearchTree()
    assert bst.pop_min() is None


def test_pop_max_ordered():
    bst = BinarySearchTree()

    item_list = list(range(10))

    for item in item_list:
        bst.add_value(item)

    assert bst.pop_max() == 9


def test_pop_max_reverse_ordered():
    bst = BinarySearchTree()

    item_list = list(range(10))[::-1]

    for item in item_list:
        bst.add_value(item)

    assert bst.pop_max() == 9


def test_pop_max_random():
    bst = BinarySearchTree()

    item_list = list(range(10))

    shuffled_item_list = item_list[:]
    random.shuffle(shuffled_item_list)

    for item in shuffled_item_list:
        bst.add_value(item)

    assert bst.pop_max() == 9


def test_pop_max_empty():
    bst = BinarySearchTree()
    assert bst.pop_max() is None
