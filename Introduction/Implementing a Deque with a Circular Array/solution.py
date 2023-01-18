from easyinput import read

class Empty(Exception):
  """Error attempting to access an element from an empty container"""
  pass

class ArrayDeQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayDeQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def last(self):
    """Return (but do not remove) the element at the back of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[int((self._front + self._size - 1) % len(self._data))]


  def delete_first(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    if 0 < self._size < len(self._data) // 4:
      self._resize(len(self._data) // 2)
    return answer

  def delete_last(self):
    """Remove and return the last element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():                   # la implementació circular està al mòdul de rear
      raise Empty('Queue is empty')
    rear_index = int((self._front + self._size - 1) % len(self._data))
    answer = self._data[rear_index]
    self._data[rear_index] = None         # help garbage collection
    self._size -= 1
    if 0 < self._size < len(self._data) // 4:
      self._resize(len(self._data) // 2)
    return answer


  def add_first(self, e):
    """Add an element to the front of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self._data))     # double the array size   
    self._front = (self._front - 1) % len(self._data)   # Implemento circularitat, m'estalvio si és més petit que 0 salto al final ...
    self._data[self._front] = e
    self._size += 1                     # és important actualitzar el size DESPRÉS de ficar el nou element


 
  def add_last(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self._data))     # double the array size
    # self.rear s'actualitza sol en funció de size quan el cridem! 
    avail = int(self._front + self._size) % len(self._data)

    # rear_index_updated = int((self._front + self._size - 1) % len(self._data))
    self._data[avail] = e
    self._size += 1                     # és important actualitzar el size DESPRÉS de ficar el nou element

    # Hauria de ser tots els casos perquè la circularitat ja està implementada en el mod

  # This is a private method, one should not edit it! (ho indica el _ de davant del mètode!)
  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned
                                           # si afegirem back index aquí hauriem de realiniar back
                                           # self_back = int((self._front + self._size - 1) % len(self._data))


# =============================================================================
# add first, add last, first, last, delete first, delete last, len, empty
# =============================================================================

if __name__ == '__main__':
    S = ArrayDeQueue()       
    ordre = read(str)
    while ordre is not None:

        if ordre == 'add_first':
                e = read(int)
                S.add_first(e)
                print('Size: {}; first element: {}'.format(S.__len__(), S.first()))

        elif ordre == 'add_last':
                e = read(int)
                S.add_last(e)
                print('Size: {}; last element: {}'.format(S.__len__(), S.last()))
                
        elif ordre == 'first':
            if S.__len__() == 0:
                print('Deque is empty')
            else:
                print('First element: {}'.format(S.first()))
                
        elif ordre == 'last':
            if S.__len__() == 0:
                print('Deque is empty')
            else:
                print('Last element: {}'.format(S.last()))
                
        elif ordre == 'delete_first':
            if S.__len__() == 0:
                print('Deque is empty')
            else:
                print('{} removed'.format(S.delete_first()))
                
        elif ordre == 'delete_last':
            if S.__len__() == 0:
                print('Deque is empty')
            else:
                print('{} removed'.format(S.delete_last()))
                
        elif ordre == 'len':
                print('Size: {}'.format(S.__len__()))
                
        elif ordre == 'is_empty':
            if S.__len__() == 0:
                print('Deque is empty')
            else:
                print('Deque is not empty')
        
        ordre = read(str)       # Imprescindible per a continuar el bucle!