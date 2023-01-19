from easyinput import read


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

class SamePerson(Exception):
    """pair with one-self"""
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

    def pair(self, name1, name2):
        if name1 == name2:
            raise SamePerson('Pair with one-self is illegal')
        e1 = self._Item(name1, None)
        e2 = self._Item(name2, None)
        if self.is_empty():
            self._root = self._Node(e1)
            node2 = self._insert_or_find(self._root, e2)
            self._root._element._value = node2
            node2._element._value = self._root
        else:
            node1 = self._insert_or_find(self._root, e1)
            node2 = self._insert_or_find(self._root, e2)
            if node1._element._value is not None:
                node1._element._value._element._value = None
            if node2._element._value is not None:
                node2._element._value._element._value = None
            node1._element._value = node2
            node2._element._value = node1


    def _insert_or_find(self, node, x, pa=None, leftC=False):
        if node is None:
            if leftC:
                pa._left = self._Node(x)
                return pa._left
            else:
                pa._right = self._Node(x)
                return pa._right
        else:
            if x < node._element:
                return self._insert_or_find(node._left, x, node, True)
            elif node._element < x:
                return self._insert_or_find(node._right, x, node, False)
            else:
                return node

    def __iter__(self):
        yield from self._inorder(self._root)

    # OJO! Generate an iteration of the BST elements in in-order.
    def inorder_pairs(self):
        if self.is_empty():
            return
        yield from self._inorder_pairs(self._root)

    def _inorder_pairs(self, nod):
        if nod is not None:
            yield from self._inorder_pairs(nod._left)
            if nod._element._value is not None:
                yield nod._element._key, nod._element._value._element._key
            yield from self._inorder_pairs(nod._right)

    def inorder_singles(self):
        if self.is_empty():
            return
        yield from self._inorder_singles(self._root)

    def _inorder_singles(self, nod):
        if nod is not None:
            yield from self._inorder_singles(nod._left)
            if nod._element._value is None:
                yield nod._element._key
            yield from self._inorder_singles(nod._right)

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


if __name__ == '__main__':
    t = BST_OrdSet()
    action = read(str)
    while action is not None:
        if action == 'affair':
            name1 = read(str)
            name2 = read(str)
            t.pair(name1, name2)
        else:
            print('COUPLES:')
            for name1, name2 in t.inorder_pairs():
                if name1 < name2:
                    print(name1, name2)
            print('ALONE:')
            for name1 in t.inorder_singles():
                print(name1)
            print('----------')
        action = read(str) 