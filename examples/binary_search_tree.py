from trees import BinarySearchTree

if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.add_value(5)
    bst.add_value(3)
    bst.add_value(2)
    bst.add_value(1)
    bst.add_value(20)
    bst.add_value(24)
    bst.add_value(25)
    bst.add_value(26)
    bst.add_value(7)
    bst.add_value(4)
    bst.add_value(6)
    bst.add_value(8)
    bst.add_value(23)
    bst.add_value(21)
    bst.add_value(22)

    print(bst.pop_min())
    print(bst.pop_min())
    print(bst.pop_min())
    print(bst.pop_min())
    print(bst.pop_min())

    print('-----')

    for value in bst.traverse():
        print(value)
