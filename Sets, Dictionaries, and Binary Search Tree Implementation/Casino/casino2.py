from easyinput import read
from copy import deepcopy

"""
Write a program to compute the profits of the players of a casino. 
The operations that can be done are: enter the casino, leave the casino, 
or win a quantity (maybe negative) of money.
"""

class MapBase:
    #------------------------------- nested Item class -------------------------------
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key  # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)  # opposite of eq

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class BST_OrdSet(MapBase):
    #----- nested _Node class ------------------
    class _Node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, ele, le=None, ri=None):
            self._element = ele
            self._left    = le
            self._right   = ri

    #---------Ordered Set public methods -------

    """def __init__(self):
      self._root = None
      self._size = 0
      """


    def __init__(self, *rest):
        n = len(rest) # rest is the list of arguments
        if n == 0:
            self._root = None
            self._size = 0
        elif n == 1: # This case is only used for printing the tree.
            self._root = rest[0] # Size cannot be computed efficiently.
        else:
            self._root = self._Node(rest[0], rest[1]._root, rest[2]._root)
            self._size = 1 + rest[1]._size + rest[2]._size


    # Return True if the set is empty.
    def is_empty(self):
        return self._root is None

    # Return the number of elements in the set.
    def __len__(self):
        return self._size

    # Returns True if the set contains element x
    def search(self, x):
        if self.is_empty():
            return False
        return self._search(self._root, x)

    # Find the smallest element in a non-empty set.
    def findMin(self):
        if self.is_empty():
            raise Empty('Set is empty')
        return self._findMin(self._root)._element

    # Find the largest element in a non-empty set.
    def findMax(self):
        if self.is_empty():
            raise Empty('Set is empty')
        return self._findMax(self._root)._element

    # Insert element x, if it was not in the set.
    def insert(self, k, v):
        x = self._Item(k, v)
        if self.is_empty():
            self._root = BST_OrdSet._Node(x)
            self._size += 1
            return True
        else:
            return self._insert(self._root, x)

    # Remove element x from the set.
    def remove(self, k):
        if self.is_empty():
            return False, None
        x = self._Item(k, None)

        return self._remove(self._root, x)

    # Generate an iteration of the set elements
    # in ascending order.
    def __iter__(self):
        yield from self._inorder(self._root)


    #----BST based Ordered Set private methods -------

    # Search x in subtree rooted at 'node'.
    def _search(self, node, x):
        if x == node._element:
            return True
        elif x < node._element:
            return self._search(node._left, x) if node._left is not None else False
        else:
            return self._search(node._right, x) if node._right is not None else False

    # Returns a reference to the node containing the
    # smallest element in the subtree rooted at node.
    def _findMin(self, node):
        if node._left is None:
            return node
        return self._findMin(node._left)

    # Returns a reference to the node containing the
    # largest element in the subtree rooted at node.
    def _findMax(self, node):
        while node._right is not None:
            node = node._right # iterative implementation
        return node

    # Insert x in subtree rooted at 'node'.
    def _insert(self, node, x, pa=None, leftC=False):
        if node is None:
            if leftC:
                pa._left = self._Node(x)
                return True
            else:
                pa._right = self._Node(x)
                return True
        else:
            if x < node._element:
                return self._insert(node._left, x, node, True)
            elif node._element < x:
                return self._insert(node._right, x, node, False)
            else:
                return False #element already in tree

    # Remove x from subtree rooted at 'node'.

    def _remove(self, node, x, pa=None, leftC=False):
        if node is None:
            return False, None# x is not in the set
        if x < node._element:
            return self._remove(node._left, x, node, True)
        elif node._element < x:
            return self._remove(node._right, x, node, False)
        else: # x is equal to node._element
            answer = deepcopy(node._element)
            self._size -= 1
            if node._left is not None and node._right is not None: # node has two children
                m = self._findMin(node._right)
                node._element = m._element
                self._remove(node._right, m._element, node, False)
                # x is equal to node._element
                # node has at most one child
                # node's left child is not empty
            elif node._left is not None:
                if pa is None: # node is the BST root
                    self._root = node._left
                elif leftC: # node is left child of pa
                    pa._left = node._left
                else:       # node is right child of pa
                    pa._right = node._left
            else: # node's left child is empty
                # node's right child might be empty
                if pa is None:
                    self._root = node._right
                elif leftC:
                    pa._left = node._right
                else:
                    pa._right = node._right
            return True, answer._value

    def increase_value(self, k, increase):
        if self.is_empty():
            return False
        x = self._Item(k, None)
        return self._increase_value(self._root, x, increase)

    def _increase_value(self, node, x, increase):
        if x == node._element:
            node._element._value += increase
            return True
        elif x < node._element:
            return self._increase_value(node._left, x, increase) if node._left is not None else False
        else:
            return self._increase_value(node._right, x, increase) if node._right is not None else False

                # Generate an iteration of the BST elements in in-order.
    def inorder(self):
        if self.is_empty():
            return
        yield from self._inorder(self._root)

    def _inorder(self, nod):
        if nod is not None:
            yield from self._inorder(nod._left)
            yield nod._element._key, nod._element._value
            yield from self._inorder(nod._right)


            #------------- Methods to run the examples ------------

    # Returns the element stored at the root node
    def root_element(self):
        return self._root._element

        # Returns the left subtree
    def left_subtree(self):
        return BST_OrdSet(self._root._left)

    # Returns the right subtree
    def right_subtree(self):
        return BST_OrdSet(self._root._right)


# Prints a binary tree in pre-order (to check examples).
def printPreOrdre(t):
    if not t.is_empty():
        print(t.root_element(), end=' ')
        printPreOrdre(t.left_subtree())
        printPreOrdre(t.right_subtree())
    else: print(-1, end=' ')

# Read binary tree in pre-order (to run examples).
def readt():
    e = read(int)
    if e != -1:
        left = readt()
        right = readt()
        return BST_OrdSet(e,left,right)
    return BST_OrdSet()


if __name__ == '__main__':
    dictionary = BST_OrdSet()
    name = read(str)
    while name is not None:
        action = read(str)
        if action == 'enters':
            if not dictionary.insert(name, 0):
                print(name + ' is already in the casino')
        elif action == 'leaves':
            left, money = dictionary.remove(name)
            if left:
                print(name + ' has won ' + str(money))
            else:
                print(name + ' is not in the casino')
        else:
            amount = read(int)
            if not dictionary.increase_value(name, amount):
                print(name + ' is not in the casino')
        name = read(str)
    print('----------')
    for name, m in dictionary.inorder():
        print(name + ' is winning ' + str(m))