"""
Write a program that forms a binary search tree from a given sequence of natural numbers. E
ach new integer must be placed at the only leaf that allows to mantain the propierty of the binary search trees. 
The repeated elements must be ignored.
"""

from easyinput import read

class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild=None
     
def insert(root,newValue):
    #if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root=BinaryTreeNode(newValue)
        return root
    #binary search tree is not empty, so we will insert it into the tree
    #if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue<root.data:
        root.leftChild=insert(root.leftChild,newValue)
    elif newValue>root.data:
        #if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild=insert(root.rightChild,newValue)
    return root

def preorder(root):
    #if root is None return
        if root==None:
            return
        #traverse root
        print(root.data)
        #traverse left subtree
        preorder(root.leftChild)
        #traverse right subtree
        preorder(root.rightChild) 
                  
        
if __name__ == '__main__':
    x = read(int)
    root= insert(None,x)

    while x is not None:
        insert(root,x)
        x = read(int)

        
    preorder(root)

# Com aquí no me calia llegir recursivament res, ho he fet tot més senzill.