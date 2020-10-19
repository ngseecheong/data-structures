from linear import LinkedList


def test_linked_list_add_start():
    ll = LinkedList()

    for i in range(10):
        ll.add_value_start(i)

    for i in range(9, -1, -1):
        assert ll.pop_value_start() == i

    assert ll.pop_value_start() is None


def test_linked_list_add_end():
    ll = LinkedList()

    for i in range(10):
        ll.add_value_end(i)

    for i in range(10):
        assert ll.pop_value_start() == i

    assert ll.pop_value_start() is None
