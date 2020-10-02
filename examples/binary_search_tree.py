from trees import BinarySearchTree

if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.add_node(5)
    bst.add_node(3)
    bst.add_node(23)
    bst.add_node(7)

    for value in bst.traverse():
        print(value)
