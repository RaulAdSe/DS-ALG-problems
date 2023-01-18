# Modify the LinkedQueue class (included in the public_files section of the problem statement) by implementing a new method called concatenate. 
from easyinput import read

class Empty(Exception):
  """Error attempting to access an element from an empty container"""
  pass

class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class -------------
  # _ vol dir que és privat. El farem servir dintre de la classe però no fora.
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'  # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next
      # Sol té un link, el guardo a next!

  #------------------------------- queue methods -------------
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                   

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue. Raise Empty exception if the queue is empty. """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._head._element            

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO). Raise Empty exception if the queue is empty."""
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._head._element
    self._head = self._head._next         # El node que abans feia de head l'he tret. Tant el element com el link de head passen a ser els propis del següent node.
    self._size -= 1
    if self.is_empty():                   
      self._tail = None                   
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None)          
    if self.is_empty():
      self._head = newest                 
    else:
      self._tail._next = newest
    self._tail = newest                   
    self._size += 1

  def concatenate(self, q):
    # Insert your implementation below
    # Ho fare amb el primer node de q i ho generalitzare

    while q._size>0 :
      if q.is_empty():
        raise Empty('Queue is empty')

      newest_el = q._head._element
      q._head = q._head._next
      q._size -= 1
      if q.is_empty():                   
        q._tail = None

    # Ara ja l'he tret de q, el vull ficar a self

      newest = self._Node(newest_el, None)      
      if self.is_empty():
        self._head = newest                 
      else:
        self._tail._next = newest
      self._tail = newest                   
      self._size += 1
    
    
    # Done el concatenament. Falta fer lo del output. 

  def __str__(self):
    # In the implementation of this method, assume the queue instance
    # can only contain integer numbers. This is only true in the context
    # of this problem.
    # Insert your implementation below 
      # Si està empty o no ho ficaré com una exception a main
    elements = []
    node_actual = self._head  # Primer node
    for i in range(self._size):
      node_actual_elem = node_actual._element
      elements.append(node_actual_elem)     # Això és una llista de integers
      node_actual = node_actual._next
    return((' '.join(str(e) for e in elements)))            # Vull que surtin sense [] de la llista, i a més com a str



# COMENTARI INDIRECT METHODS: el __ x __ adapta una acció comú a una classe determinada
# així podem fer len() o str() de un mètode. No es .str()!

if __name__ == '__main__':
    n = read(int)
    linkedques_list = []
    for i in range(n):
        linkedques_list.append(LinkedQueue())
    
        
    q_n = read(int)          # La queue a la que es refereix. 
    ordre = read(str)           # Si aquesta ordre es enqueu o concatenate haurem de ficar un read(int) més!
    while ordre is not None:

        if ordre == 'enqueue':
                e = read(int)       
                linkedques_list[q_n - 1].enqueue(e)     # Li resto 1 perquè python indexa amb 0! La queue 1 correspon al index 0.
                print('queue {}: {} enqueued'.format(q_n, e))

        elif ordre == 'first':
                answer = linkedques_list[q_n - 1].first()
                print('queue {} first element: {}'.format(q_n, answer))
                
        elif ordre == 'len':
                lenght = len(linkedques_list[q_n - 1])
                print('queue {} has {} element(s)'.format(q_n, lenght))
                
        elif ordre == 'dequeue':
            if len(linkedques_list[q_n - 1]) == 0:
                print('queue {} is empty'.format(q_n))
            else:
                answer = linkedques_list[q_n - 1].dequeue()
                print('queue {}: {} dequeued'.format(q_n, answer))
                
        elif ordre == 'print':
                str_a_printejar = str(linkedques_list[q_n - 1])
                print('queue {}: {}'.format(q_n, str_a_printejar))
                
        elif ordre == 'is_empty':
            if len(linkedques_list[q_n - 1]) == 0:
                print('queue {} is empty '.format(q_n))
            else:
                print('queue {} is not empty '.format(q_n))
                
        elif ordre == 'concatenate':
            q_n_2 = read(int)
            linkedques_list[q_n - 1].concatenate(linkedques_list[q_n_2 - 1])  # Li he de passar dos queues
            str_a_printejar_1 = str(linkedques_list[q_n - 1])
            str_a_printejar_2 = str(linkedques_list[q_n_2 - 1])     
            print('queues {} and {} concatenated'.format(q_n, q_n_2))
            print('queue {}: {}'.format(q_n, str_a_printejar_1))
            print('queue {}: {}'.format(q_n_2, str_a_printejar_2))
        
        # Imprescindible per a continuar el bucle!

        q_n = read(int)         # La queue a la que es refereix
        ordre = read(str)       