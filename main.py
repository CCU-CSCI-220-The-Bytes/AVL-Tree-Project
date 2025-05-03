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
            elif newNode.val == parentNode.val:
                raise Exception(f"Value {newNode.val} already exists in tree")

    def search(self, value): #return a node, or "None"
        currNode = self.root

        comparisons = 0
        while currNode != None and value != currNode.val:
            if value < currNode.val:
                comparisons += 1
                currNode = currNode.left
            elif value > currNode.val:
                comparisons += 1
                currNode = currNode.right

        if currNode == None:
            print(f"Value \"{value}\" couldn't be found in {comparisons} comparisons")
        else:
            print(f"Value \"{value}\" was found in {comparisons} comparisons")

        return currNode
    #def delete(self, value): #void

#Function from https://www.geeksforgeeks.org/binary-search-tree-in-python/
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def inorder_height(root, height = 0):
    if root:
        inorder_height(root.left, height+1)
        print(root.val, height)
        inorder_height(root.right, height+1)

def main():
    myTree = AVL_Tree("a")
    myTree.insert("b")
    myTree.insert("c")
    myTree.insert("d")
    myTree.insert("e")

    inorder_height(myTree.root)
    print()

    nameTree = AVL_Tree("Jordan")
    nameTree.insert("Thaddeus")
    nameTree.insert("Trent")
    nameTree.insert("Tyler")
    nameTree.insert("Kevin")
    nameTree.insert("Bella")
    nameTree.insert("Aiden")
    nameTree.insert("Clarence")
    
    inorder_height(nameTree.root)
    print()

    nameTree.search("Aiden")
    nameTree.search("George")


if __name__ == '__main__':
    main()