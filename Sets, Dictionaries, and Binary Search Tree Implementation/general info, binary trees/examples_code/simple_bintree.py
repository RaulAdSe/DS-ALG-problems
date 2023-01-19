from easyinput import read
from collections import deque

class BinTree:
  #------------------- nested _Node class ---------------------
  class _Node:
    __slots__ = '_element', '_left', '_right'  

    def __init__(self, element, left=None, right=None):
      self._element = element  
      self._left  = left
      self._right  = right

      
  #------------------- public methods --------------------
  # Constructor
  def __init__(self, *rest):
    n = len(rest) # rest is the list of arguments 
    if n == 0:      
      self._root = None
    elif n == 1:   
      self._root = rest[0]
    else:          
      self._root = self._Node(rest[0], rest[1]._root, rest[2]._root)


  # Checks whether the tree is empty.
  def is_empty(self):
    return self._root == None

  # Returns the element stored in the root node    
  def root_element(self):
    return self._root._element    

  # Returns the left subtree 
  def left_subtree(self):
    return BinTree(self._root._left)

  # Returns the right subtree 
  def right_subtree(self):
    return BinTree(self._root._right)
         
        

# Reads a binary tree     
def readBinTree():
  element = read(str)
  if element == '-1':
    return BinTree()
  left = readBinTree()
  right = readBinTree()
  return BinTree(element, left, right)


# Prints a binary tree in in-order
def printInordre(t, depth=0):
  if not t.is_empty(): 
     printInordre(t.left_subtree(), depth+1)
     print(' '*2*depth, end='')
     print(t.root_element())
     printInordre(t.right_subtree(), depth+1)


# Prints a binary tree in in-order with right subtree processed before left subtree
def printInordre_draw(t, depth=0):
  if not t.is_empty(): 

     printInordre_draw(t.right_subtree(), depth+1)
     
     print(' '*2*depth, end='')
     print(t.root_element())

     printInordre_draw(t.left_subtree(), depth+1)
     
# Prints a binary tree in pre-order
def printPreOrder_iter(t):
  if not t.is_empty():
    s = deque()
    s.append(t) # s is used as a Stack
    while len(s) != 0:
      t = s.pop()
      print(' ', t.root_element(), end='')
      if not t.right_subtree().is_empty():
        s.append(t.right_subtree())
      if not t.left_subtree().is_empty():
        s.append(t.left_subtree())


# Prints each element with its depth. 
def write_depth(t, depth=0):
    if not t.is_empty():
        print(t.root_element(), ' depth:', depth)
        write_depth(t.left_subtree(), depth+1) 
        write_depth(t.right_subtree(), depth+1) 

# Prints each element with its height. 
def height(t):
    if t.is_empty(): return -1
    else:
        h_left = height(t.left_subtree())
        h_right = height(t.right_subtree())
        h = 1 + max(h_left, h_right)    
        print(t.root_element(), ' height:', h)
        return h
        
     
if __name__ == '__main__':
    t = readBinTree()
    print('\nIn-order traversal\n')
    printInordre(t)
    print('\nIn-order traversal to draw a tree\n')
    printInordre_draw(t)
    print('\nPre-order traversal\n')
    printPreOrder_iter(t)
    print('\n\n\n')
    height(t)
    print('\n\n\n')
    write_depth(t)
    print()

