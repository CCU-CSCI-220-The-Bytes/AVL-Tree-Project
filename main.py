# From https://www.geeksforgeeks.org/avl-tree-in-python/
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def main():
    myNode = Node("a")
    myNode.left = Node("c")
    myNode.right = Node("z")

    print(f" {myNode.value}")
    print("/ \\")
    print(f"{myNode.left.value}  {myNode.right.value}")



if __name__ == '__main__':
    main()