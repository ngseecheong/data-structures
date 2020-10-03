from trees import BinarySearchTree

if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.add_value(5)
    bst.add_value(3)
    bst.add_value(2)
    bst.add_value(1)
    bst.add_value(23)
    bst.add_value(24)
    bst.add_value(25)
    bst.add_value(26)
    bst.add_value(7)

    print(bst.pop_max())

    print('-----')

    for value in bst.traverse():
        print(value)
