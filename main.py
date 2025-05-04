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

        # NEWLY ADDED 
        # Define a function to calculate height of a node
        def height(node):
            if not node:
                return 0
            # Height is 1 + the height of the taller child
            return 1 + max(height(node.left), height(node.right))

        # Define a function to compute the balance factor of a node
        def get_balance(node):
            if not node:
                return 0
            # Balance factor = height of left subtree - height of right subtree
            return height(node.left) - height(node.right)

        # Perform a left rotation (used in Right-Right or Right-Left imbalances)
        def rotate_left(unbalanced_node):
            print(f"Performing LEFT rotation on node: {unbalanced_node.val}")

            new_root = unbalanced_node.right               # Right child becomes the new root
            subtree_to_shift = new_root.left               # Temporarily store the left subtree of new root

            new_root.left = unbalanced_node                # Move the unbalanced node to the left of new root
            unbalanced_node.right = subtree_to_shift       # Reattach the stored subtree to the right of the old root

            return new_root                                # Return the new root after rotation

        # Perform a right rotation (used in Left-Left or Left-Right imbalances)
        def rotate_right(unbalanced_node):
            print(f"Performing RIGHT rotation on node: {unbalanced_node.val}")

            new_root = unbalanced_node.left                # Left child becomes the new root
            subtree_to_shift = new_root.right              # Temporarily store the right subtree of new root

            new_root.right = unbalanced_node               # Move the unbalanced node to the right of new root
            unbalanced_node.left = subtree_to_shift        # Reattach the stored subtree to the left of the old root

            return new_root                                # Return the new root after rotation

        # Rebalance a node if it has become unbalanced
        def rebalance_node(node):
            if not node:
                return None

            balance = get_balance(node)

            # Case 1: Left-heavy subtree
            if balance > 1:
                # Left-Left case (single right rotation)
                if get_balance(node.left) >= 0:
                    return rotate_right(node)
                # Left-Right case (double rotation: left then right)
                else:
                    node.left = rotate_left(node.left)
                    return rotate_right(node)

            # Case 2: Right-heavy subtree
            if balance < -1:
                # Right-Right case (single left rotation)
                if get_balance(node.right) <= 0:
                    return rotate_left(node)
                # Right-Left case (double rotation: right then left)
                else:
                    node.right = rotate_right(node.right)
                    return rotate_left(node)

            # Balanced case — no rotation needed
            return node

        # Recursively rebalance the tree from the bottom up (post-order traversal)
        def rebalance_from_root(node):
            if node is None:
                return None

            # First rebalance left and right subtrees
            node.left = rebalance_from_root(node.left)
            node.right = rebalance_from_root(node.right)

            # Then rebalance the current node
            return rebalance_node(node)

        # Apply rebalancing starting from the root and update the root reference
        self.root = rebalance_from_root(self.root)

    # -------------- END OF INSERTION CODE ------------------

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

#FIXED 
# calculates the hieght of each node in the tree
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def inorder_with_true_height(root):
    if root:
        inorder_with_true_height(root.left)   # Visits the left subtree.
        print(root.val, height(root))         # Prints the node’s value and its true height as calculated by the height() function.
        inorder_with_true_height(root.right)  # visits the right subtree

def main():

    # ===== Original wordTree with preset words =====
    wordTree = AVL_Tree("car")
    wordTree.insert("football")
    wordTree.insert("apple")
    wordTree.insert("ladder")
    wordTree.insert("family")
    wordTree.insert("bagel")
    wordTree.insert("motorcycle")
    wordTree.insert("dog")

    
    # Asks the user for a word to insert into the tree and search for it
    # the AVL tree shows after the user says "yes" to quit
    while True:
        newlyAddedWord = input("Enter a word to insert into the tree: ")
        try:
            wordTree.insert(newlyAddedWord)
            print(f'\n"{newlyAddedWord}" has been inserted into the tree.')
        except Exception as e:
            print(e)

        searchWord = input("\nSearch for a word: ")
        wordTree.search(searchWord)

        quitTreeProgram = input("\nDo you want to quit? (yes/no): ").strip().lower()
        if quitTreeProgram == "yes":
            break

    # the final output of the tree
    print("\nFinal AVL Tree (in-order with height):")
    inorder_with_true_height(wordTree.root)

    
    # Keep this original example tree if needed (are we using this for an example?)
    # myTree = AVL_Tree("a")
    # myTree.insert("b")
    # myTree.insert("c")
    # myTree.insert("d")
    # myTree.insert("e")

    # print("\nOriginal sample tree (in-order with height):")
    # inorder_height(myTree.root)
    # print()


if __name__ == '__main__':
    main()
    main()
