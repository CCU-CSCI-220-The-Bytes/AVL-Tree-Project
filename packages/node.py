"""
    Node Class and AVL Tree Development 

    Developed by Jordan and Thaddeus

"""


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

    def insert(self, value): #returns string and bool for error handling
        # Declare Variables
        errorMessage = ""
        errorFlag = False

        # Covers the invalid inputs
        # Checks if the input is a number (int or float)
        if isinstance(value, (int, float)) or (isinstance(value, str) and value.isnumeric()):
            # Returns Message and Status of Error (ErrorFlag)
            errorMessage = "The value cannot be a number"
            errorFlag = True
            return errorMessage, errorFlag

        # Checks if the value is an empty string
        if value == "":
            # Returns Message and Status of Error (ErrorFlag)
            errorMessage = "The value cannot be an empty string"
            errorFlag = True
            return errorMessage, errorFlag
        

        newNode = Node(value)
        parentNode = self.root

        # Handles if there is no root node!
        if parentNode is None:
            self.root = Node(value)
        else:
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
                    # Returns Message and Status of Error (ErrorFlag)
                    errorMessage =  f"The value {newNode.val} already exists in the tree"
                    errorFlag = True
                    return errorMessage, errorFlag
        

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
            # print(f"Performing LEFT rotation on node: {unbalanced_node.val}")

            new_root = unbalanced_node.right               # Right child becomes the new root
            subtree_to_shift = new_root.left               # Temporarily store the left subtree of new root

            new_root.left = unbalanced_node                # Move the unbalanced node to the left of new root
            unbalanced_node.right = subtree_to_shift       # Reattach the stored subtree to the right of the old root

            return new_root                                # Return the new root after rotation

        # Perform a right rotation (used in Left-Left or Left-Right imbalances)
        def rotate_right(unbalanced_node):
            # print(f"Performing RIGHT rotation on node: {unbalanced_node.val}")

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

        # Returns Message and Status of Error (ErrorFlag)
        # Since, successful it returns blank and false for flag.
        return errorMessage, errorFlag

    # -------------- END OF INSERTION CODE ------------------

    def search(self, value): #return a node or "None" and message
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
            resultMessage = f"The value \"{value}\" couldn't be found in {comparisons} comparisons"
        else:
            resultMessage = f"The value \"{value}\" was found in {comparisons} comparisons"
        return currNode, resultMessage
        
    # NEWLY ADDED 
    # AVL FUnction Deletion Code
    def delete(self, value):
        # Calculates the height of a given node
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        # Computes the balance factor of a node (left height - right height)
        def get_balance(node):
            if not node:
                return 0
            return height(node.left) - height(node.right)

        # Performs a left rotation on the given unbalanced node
        def rotate_left(z):
            new_root = z.right
            temp = new_root.left
            new_root.left = z
            z.right = temp
            return new_root
        
        # Performs a right rotation on the given unbalanced node
        def rotate_right(z):
            new_root = z.left
            temp = new_root.right
            new_root.right = z
            z.left = temp
            return new_root
        
        # Rebalances the node if it becomes unbalanced after deletion
        def rebalance(node):
            if not node:
                return None
            balance = get_balance(node)

            # Left heavy 
            if balance > 1:
                if get_balance(node.left) >= 0:
                    return rotate_right(node)
                else:
                    node.left = rotate_left(node.left)
                    return rotate_right(node)

            # Right heavy
            if balance < -1:
                if get_balance(node.right) <= 0:
                    return rotate_left(node)
                else:
                    node.right = rotate_right(node.right)
                    return rotate_left(node)

            return node

        # Finds the node with the smallest value in the given subtree
        def min_value_node(node):
            current = node
            while current.left is not None:
                current = current.left
            return current

        # Recursively deletes a node with the given key and rebalances the tree
        def delete_node(root, key):
            if not root:
                return root

            if key < root.val:
                root.left = delete_node(root.left, key)
            elif key > root.val:
                root.right = delete_node(root.right, key)
            else:
                # Node with one child or no child
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                # Node with two children: Get inorder successor
                temp = min_value_node(root.right)
                root.val = temp.val
                root.right = delete_node(root.right, temp.val)

            # calls for rebalance after deletion 
            return rebalance(root)
        
        # Starts deletion from the root and updates the root reference
        self.root = delete_node(self.root, value)
        
    # -------------- END OF DELETION CODE ------------------

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
