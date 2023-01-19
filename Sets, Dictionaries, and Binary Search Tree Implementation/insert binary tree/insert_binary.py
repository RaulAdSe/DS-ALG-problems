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

      # Tot això és privat. Necessito fer mètodes públics per consultar-ho. Mai puc canviar-los.
  #------------------- public methods --------------------
  # Constructor
  def __init__(self, *rest):
    n = len(rest) # rest is the list of arguments 
    if n == 0:      
      self._root = None
    elif n == 1:   
      self._root = rest[0]
    else:          
       self._root = self._Node(rest[0], rest[1]._root, rest[2]._root)  # rest[0] 
      # self._root = self._Node(rest[0], rest[1], rest[2])  a mi m'agrada així             # rest[1] i rest[2] son subtrees!
                                                                                            # El constructor vol subtrees segmenta en root.
                                                                        
  # Checks whether the tree is empty.
  def is_empty(self):
    return self._root == None # He canviat això!

  # Returns the element stored in the root node    
  def root_element(self):
    return self._root._element    

  # Returns the left subtree 
  def left_subtree(self):
    return BinTree(self._root._left)
 
  # Returns the right subtree 
  def right_subtree(self):
    return BinTree(self._root._right)

  def LOOKUP(self, lookupval):
        
    if lookupval < self.root_element():  # Miraré a l'esquerra
        if self.left_subtree().is_empty() == False:  # Això em comprova que l'àrbre que agafe com a subtree amb recursivitat no està buit.
            return self.left_subtree().LOOKUP(lookupval) # recursively check the left tree
        else:
            return 0 # can't go any further so return false
    elif lookupval > self.root_element():    # Miraré a la dreta
        if self.right_subtree().is_empty() == False:
            return self.right_subtree().LOOKUP(lookupval)
        else:
            return 0
    else:
        return 1
    

         
  def insert(self, num):
      
    # Segons el meu constructor d'àrbre, en el moment que creo un node he de tenir els seus dos vehins de baix!!!
    # És recurssiu, per això no ho puc fer "sobre la marxa"
    # Al read ja ve per ordre, per això el left i després el right!!
    
    # O puc renombrar el parent per a introduir el child!?
    
    # Ara cal la recursivitat si no està empty
    # if self.left_subtree().is_empty():
        
    # Li he de dir les condicions al NUM!!!
    
    if self.LOOKUP(num) == 0:   # Si és un binary tree no pot tenir elements repetits!
        if self.root_element()>num:
            if self._root._left == None and  self._root._right != None:
                left_subtree = BinTree(num, BinTree(), BinTree(self._root._right))
                self = BinTree(self.root_element(), left_subtree, self.right_subtree())
            elif self._root._left == None and  self._root._right == None:
                left_subtree = BinTree(num, BinTree(), BinTree())
                right_subtree = BinTree()
                self = BinTree(self.root_element(), left_subtree, right_subtree)
            else:
                self.left_subtree().insert(num) # Recursivitat
        elif self.root_element()<num:
            if self._root._right == None and  self._root._left != None:
                right_subtree = BinTree(num, BinTree(self._root._left), BinTree())
                self = BinTree(self.root_element(), self.left_subtree(), right_subtree)
            elif self._root._right == None and  self._root._left == None:
                right_subtree = BinTree(num, BinTree(), BinTree())
                left_subtree = BinTree()
                self = BinTree(self.root_element(), left_subtree, right_subtree)
            else:
                self.right_subtree().insert(num) # Recursivitat
    return self   
# No sé si això cal :(
# La cosa és que en això em torna 3 nodes al tree (no va la recursivitat)
# Sense això no em torna més que el root :(

# AIXÒ S'HA D'ARREGLAR DE CARA AL FINAl



# self._root._right és un node. 
# El qual està bé perquè quan faig right_subtree se'm fa un tree amb eixe node.

# Reads a binary tree     
def readBinTree():
  element = read(str)
  if element == '-1':
    return BinTree()
  left = readBinTree()
  right = readBinTree()
  return BinTree(element, left, right) 

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
        
# t._root._right  # Això ja és un node, no cal que li demaner root
        

        
if __name__ == '__main__':
    x = read(int)
    t = BinTree(x, BinTree(), BinTree())
    while x is not None:
        t=t.insert(x)
        # t.insert(x)
        x = read(int)
    
    printPreOrder_iter(t)