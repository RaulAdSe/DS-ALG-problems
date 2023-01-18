# Array Based Stack with Maximum Capacity
from easyinput import read

class Empty(Exception):
  """Error attempting to access an element from an empty container"""
  pass
class Full(Exception):
  """Error attempting to introduce element"""
  pass #@ Falta

class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self, n=None): #@ valor por defecto None
    self._n = 0 # Los atributos deben tener nombres que comienzan con _
    # porque son no-públicos. Este atributo representa el tamaño real del Stack, el número de elementos que tiene en cada momento
    """Create an empty stack."""
    self._data=[None]*n #@ Queremos evitar append


  def __len__(self):
    return self._n #@ No queremos tener que recorrer cada vez que se pregunte len()

  def is_full(self):
    """Return True if the stack is full."""
    return len(self._data) == self._n #@ len(self._data) es la capacidad máxima.
  


  def is_empty(self):
    """Return True if the stack is empty."""
    return self._n == 0 #@

  def push(self, e):
    """Add element e to the top of the stack."""
    if self.is_full():
      raise Full('Stack full')
    self._data[self._n]=e
    self._n+=1
    #@ No devuelve nada return self._data.insert(self.a-1,e)               # new item stored at end of list


  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty') #Obliga a que ocurra el exception, o llama a ese error
    return self._data[self._n-1]                 #@  the last item in part of the list used 

  def pop(self):
    c=0
    """Remove and return the element from the top of the stack (i.e., LIFO).
    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    #@ No queremos usar pop ni append. Lee lo que os he dicho sobre 'Amortization' en el capítulo 5 del libro de Goodrich c=self._data.pop(self.a-1)
    #self._data.insert(self.a-1,"")
    self._n-=1
    return self._data[self._n]
    # remove last item from list

if __name__ == '__main__':
    n = read(int)      # Si li dono al enter estic ficant None com a maxlen.
    S = ArrayStack(n)       # Aquest n és el que em farà de maxlen
    ordre = read(str)
    while ordre is not None:
        if ordre == 'push':
            try:
                e = read(int)
                S.push(e)
                print('Stack size: {}'.format(len(S)))
            except Full:
                print('Stack was full')
        elif ordre == 'pop':
            try:
                print('{} removed'.format(S.pop()))
            except Empty:
                print('Stack is empty')

        elif ordre == 'empty':
            if S.is_empty():
                print('Stack is empty')
            else:
                print('Stack is not empty')

        elif ordre == 'top':
            if S.is_empty():
                print('Stack is empty')
            else:
                print('top element: {}'.format(S.top()))

        elif ordre == 'len':

                print('Stack size: {}'.format(len(S)))

        ordre = read(str)       # Imprescindible per a continuar el bucle!
