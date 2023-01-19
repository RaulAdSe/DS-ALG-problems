"""
Write a program that reads a binary search tree with natural numbers, 
and that, for each read natural after that, indicates if it is or not in the tree,
"""

from easyinput import read, read_line
class Node:
    def __init__(self, data, left = None, right = None):
        
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self,*rest):
        n = len(rest)
        if n ==1:
            self.root = Node(rest[0])    # Rest[0] és l'anitc rootdata
        elif n ==3:                         # Els root lefts i rights seràn subtrees
            self.root = Node(rest[0])    # Rest[0] és l'anitc rootdata
            self.root.left = rest[1] # Rest[1] és un subtree
            self.root.right = rest[2] # Rest[2] és un subtree
            # self.root.left.root = Node(rest[1].root) # Rest[1] és un subtree
            # self.root.right.root = Node(rest[2].root) # Rest[2] és un subtree

    def LOOKUP(self, lookupval):
        if self.root.data != None:  # Em cal ficar això perquè els  if self.root.left is not None no funcionen
            if lookupval < self.root.data:
                if self.root.left is not None: 
                    return self.root.left.LOOKUP(lookupval) # recursively check the left tree
                else:
                    return 0 # can't go any further- so return false
            elif lookupval > self.root.data:
                if self.root.right is not None:
                    return self.root.right.LOOKUP(lookupval)
                else:
                    return 0
            else:
                return 1
        else:
            return 0

# # Reads a binary tree     
# def readBinTree():
#   element = read(int)
#   Tree = BinaryTree(element)
#   if element == -1:
#     return BinaryTree(None)
#   left = readBinTree()
#   right = readBinTree()
#   return Node(element, left, right)

# Amb aquesta simplificació lo únic que he de fer és trobar una manera de llegir recursiva amb la nova estructura.

def readBinTree_2():
    element = read(int)
    if element == -1:
      return BinaryTree(None)
    left = readBinTree_2()
    right = readBinTree_2()
    return BinaryTree(element, left, right)


# Print preorder
def preorder(t):
    #if root is None return
        if t==None:
            return
        #traverse root
        if t.root.data != None:
            print(t.root.data)
        #traverse left subtree
        preorder(t.root.left)
        #traverse right subtree
        preorder(t.root.right) 


# # Lo únic que me falta és una manera de llegir
# Tree = BinaryTree(24)
# Tree.root.left = Node(11)
# Tree.root.left.left = Node(199)
# Tree.root.left.right = Node(167)
# Tree.root.right = Node(2)
# Tree.root.right.right = Node(8)

# print(Tree.LOOKUP(11))
# print(Tree.LOOKUP(13))


if __name__ == '__main__':
    read(int) #the number of internal nodes is also given just before, you may ignore it
    T = readBinTree_2()
    read_line() # This reads the empty line after
   
    x = read(int)
    while x is not None:
        print(str(x) + ' ' + str(T.LOOKUP(x)))
        x = read(int)