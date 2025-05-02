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

def main():
    myTree = AVL_Tree("b")
    myTree.insert("a")
    myTree.insert("c")
    myTree.insert("d")

    print(f"Root: {myTree.root.val}")
    print(f"Left of root: {myTree.root.left.val}")
    print(f"Right of root: {myTree.root.right.val}")
    print(f"Right right of root: {myTree.root.right.right.val}")

 
    #Jordan’s created code  
    # This code checks each node and prints its height 

    if myTree.root: 
        print(f"Height of root {myTree.root.val}: {get_height(myTree.root)}") 
    if myTree.root.left: 
        print(f"Height of left child {myTree.root.left.val}: {get_height(myTree.root.left)}") 
    if myTree.root.right: 
        print(f"Height of right child {myTree.root.right.val}: {get_height(myTree.root.right)}") 
    if myTree.root.right.right: 
        print(f"Height of right-right child {myTree.root.right.right.val}: {get_height(myTree.root.right.right)}")

# Expected tree:
#  /b\
# a  c\
#      d

if __name__ == '__main__':
    main()
