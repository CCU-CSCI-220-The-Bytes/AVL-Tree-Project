# From https://www.geeksforgeeks.org/avl-tree-in-python/
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# AVL tree: a binary search tree with a balance condition
# for all nodes, the height of the left and the right must not be more than 1 apart.
class AVL_Tree():
    def __init__(self, rootVal):
        self.rootNode = Node(rootVal)

    def insert(self, value): #void
        #for testing purposes, just always insert to the left
        newNode = Node(value)
        parentNode = self.rootNode

        while parentNode.left != None:
            parentNode = parentNode.left
        parentNode.left = newNode

    #def search(self, value): #return a node
    #def delete(self, value): #void

def main():
    myTree = AVL_Tree("a")
    myTree.insert("b")
    myTree.insert("c")
    myTree.insert("d")

    currNode = myTree.rootNode
    while currNode != None:
        print(currNode.value)
        currNode = currNode.left



if __name__ == '__main__':
    main()