# From https://www.geeksforgeeks.org/avl-tree-in-python/
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# AVL tree: a binary search tree with a balance condition
# for all nodes, the height of the left and the right must not be more than 1 apart.
class AVL_Tree():
    def __init__(self, rootNode):
        self.root = rootNode

    #insert(self, newNode) 
    #search(self, value) 
    #delete(self, value) 

def main():
    myNode = Node("a")
    myNode.left = Node("c")
    myNode.right = Node("z")

    print(f" {myNode.value}")
    print("/ \\")
    print(f"{myNode.left.value}  {myNode.right.value}")



if __name__ == '__main__':
    main()