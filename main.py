# Node class from https://www.geeksforgeeks.org/avl-tree-in-python/
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# AVL tree: a binary search tree with a balance condition
# for all nodes, the height of the left and the right must not be more than 1 apart.
class AVL_Tree():
    def __init__(self, rootVal):
        self.root = Node(rootVal)

    def insert(self, value): #void
        #for now we will insert alphabetically, but do no balancing
        newNode = Node(value)
        parentNode = self.root

        success = False
        while not success:
            if newNode.val < parentNode.val:
                if parentNode.left == None:
                    parentNode.left = newNode
                    success = True
                else:
                    parentNode = parentNode.left
            elif newNode.val > parentNode.val:
                if parentNode.right == None:
                    parentNode.right = newNode
                    success = True
                else:
                    parentNode = parentNode.right
        

    #def search(self, value): #return a node
    #def delete(self, value): #void

#Function from https://www.geeksforgeeks.org/binary-search-tree-in-python/
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def main():
    myTree = AVL_Tree("b")
    myTree.insert("a")
    myTree.insert("c")
    myTree.insert("d")

    inorder(myTree.root)

# Expected tree:
#  /b\
# a  c\
#      d

if __name__ == '__main__':
    main()