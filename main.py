import random

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
        
        #Now, we have to check if our AVL tree remains balanced after the insertion
        # (insert balance checking code here)


    def search(self, value): #return a node, or "None"
        currNode = self.root

        comparisons = 0
        #Since this is a binary search tree we only need to go deeper left or right, not traverse the entire tree.
        #Only stop when the current node doesn't exist or when we have found the value
        while currNode != None and value != currNode.val:
            #Binary search yayyy
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
#Helper function, prints all values of the tree using "in" order
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

#Helper function, prints all values and their heights using "in" order
def inorder_height(root, height = 0):
    if root:
        inorder_height(root.left, height+1)
        print(root.val, height)
        inorder_height(root.right, height+1)

def inorder_iterative(root):
    currNode = root
    stack = []
    previousAction = 0

    count = 0
    while True:
        while currNode.left != None and previousAction != "L" and previousAction != "R": #L step of LVR
            stack.append(currNode)
            stack.append("L")
            currNode = currNode.left
            previousAction = "Down"

        if previousAction != "R": print(currNode.val) #V step of LVR

        if currNode.right != None and previousAction != "R": #R step of LVR
            stack.append(currNode)
            stack.append("R")
            currNode = currNode.right
            previousAction = "Down"
        else:
            if len(stack) == 0: #this exit condition will exit if the root has no children on the right
                break
            #go back up
            previousAction = stack.pop()
            currNode = stack.pop()

        #if len(stack) == 0 and previousAction == "R":
        #    break
        if count > 9999999:
            print("Loop limit exceeded for inorder_iterative")
            break

def inorder_iterative_height(root):
    currNode = root
    stack = []
    previousAction = 0
    currHeight = 0

    count = 0
    while True:
        while currNode.left != None and previousAction != "L" and previousAction != "R": #L step of LVR
            stack.append(currNode)
            stack.append("L")
            currNode = currNode.left
            previousAction = "Down"
            currHeight += 1

        if previousAction != "R": print(currNode.val, currHeight) #V step of LVR

        if currNode.right != None and previousAction != "R": #R step of LVR
            stack.append(currNode)
            stack.append("R")
            currNode = currNode.right
            previousAction = "Down"
            currHeight += 1
        else:
            if len(stack) == 0: #this exit condition will exit if the root has no children on the right
                break
            #go back up
            previousAction = stack.pop()
            currNode = stack.pop()
            currHeight -= 1

        if count > 9999999:
            print("Loop limit exceeded for inorder_iterative")
            break

def tree_height(root):
    currNode = root
    stack = []
    previousAction = 0
    currHeight = 0
    maxHeight = 0

    count = 0
    while True:
        while currNode.left != None and previousAction != "L" and previousAction != "R": #L step of LVR
            stack.append(currNode)
            stack.append("L")
            currNode = currNode.left
            previousAction = "Down"
            currHeight += 1
            if currHeight > maxHeight: maxHeight = currHeight

        #if previousAction != "R": print(currNode.val, currHeight) #V step of LVR

        if currNode.right != None and previousAction != "R": #R step of LVR
            stack.append(currNode)
            stack.append("R")
            currNode = currNode.right
            previousAction = "Down"
            currHeight += 1
            if currHeight > maxHeight: maxHeight = currHeight
        else:
            if len(stack) == 0: #this exit condition will exit if the root has no children on the right
                break
            #go back up
            previousAction = stack.pop()
            currNode = stack.pop()
            currHeight -= 1

        if count > 9999999:
            print("Loop limit exceeded for inorder_iterative")
            break
    print(f"Max height of the tree was {maxHeight}")

def main():
    myTree = AVL_Tree("b")
    myTree.insert("a")
    myTree.insert("c")
    myTree.insert("d")
    myTree.insert("e")

    inorder_height(myTree.root)
    print("-"*35)
    inorder_iterative_height(myTree.root)
    tree_height(myTree.root)


if __name__ == '__main__':
    main()