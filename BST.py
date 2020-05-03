'''
BST implements Binary Search Tree Algorithms
   @author: Shelby Neal
   Emplid: 6030859
   Email: ssn287@email.vccs.edu
   Purpose: Programming Assignment #6
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, node): #insert node function
    if root is None: #base case, tree is empty
        root = node #insert the root
    else:
        if root.value < node.value: #check if new node is less than root
            if root.right is None: #check if right is empty
                root.right = node #insert right
            else:
                insert(root.right, node) #recur right
        else:
            if root.left is None: #check if left is empty
                root.left = node #insert left
            else:
                insert(root.left, node) #recur left

def findMin(node): #find minimum node function
    current = node
    while(current.left):
        current = current.left
    return current

def delete(root, key): #delete node function
    if root is None: #base case
        return root
    if key < root.value: #check if key is in left subtree
        root.left = delete(root.left, key) #recur through left subtree
    elif key > root.value: #check if key is in right subtree
        root.right = delete(root.right, key) #recur through right subtree
    else: #check if root is key
        if root.left is None: #check if left is empty
            return root.right #return right
        elif root.right is None: #check if right is empty
            return root.left #return left
        temp = findMin(root.right) #find minimum node in right subtree
        root.value = temp.value #replace root with new value
        root.right = delete(root.right, temp.value) #delete replaced node
    return root #returns the new root
        
def preorder(root): #preorder tree traversal function
    if root:
        print(root.value) #first print node data
        preorder(root.left) #then recur left
        preorder(root.right) #then recur right

def inorder(root): #inorder tree traversal function
    if root:
        inorder(root.left) #first recur left
        print(root.value) #then print node data
        inorder(root.right) #then recur right

def postorder(root): #postorder tree traversal function
    if root:
        postorder(root.left) #first recur left
        postorder(root.right) #then recur right
        print(root.value) #then print node data

def findLargest(root): #find largest node function
    if root == None: #base case
        return 0
    result = root.value #first check root
    left = findLargest(root.left) #then recur through left subtree
    right = findLargest(root.right) #then recur through right subtree
    if left > result: #check largest in left subtree
        result = left
    if right > result: #check largest in right subtree
        result = right
    return result #return largest node value in binary search tree

'''
driver to test functions
'''
root = Node(9)
insert(root, Node(5))
insert(root, Node(2))
insert(root, Node(4))
insert(root, Node(11))
print("\nPreorder binary tree traversal:\n")
preorder(root)
print("\nInorder binary tree traversal:\n")
inorder(root)
print("\nPostorder binary tree traversal:\n")
postorder(root)
print("\nThe largest node is: ", findLargest(root), "\n")
num = int(input("Which node would you like to delete (enter a node value):"))
delete(root, num)
print("\nThe new tree (inorder) is:\n")
inorder(root)