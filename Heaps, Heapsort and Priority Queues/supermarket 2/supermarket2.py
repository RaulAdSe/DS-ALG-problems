"""
A customer leaves a queue: If the queue is between 1 and n, and that queue is not empty, 
the oldest customer of that queue leaves it. Otherwise, the event is ignored. 
"""

from easyinput import read, read_line
from heapq import heapify, heappop, heappush

  
def escribe(v):
  print('FINAL CONTENTS')
  print('--------------')
  for i in range(len(v)):
    print('queue {}:'.format(i+1), end='')  
    while len(v[i]) != 0:
      print(' {}'.format(heappop(v[i])[1]), end='')
    print()


if __name__ == '__main__':
  n = read(int)
  v = [[] for _ in range(n)] # v is the supermarket containing the n priority queues
  for i in range(n):
    line_contents = read_line().split()
    v[i] = [(-float(line_contents[2*j+1]), line_contents[2*j]) \
            for j in range(len(line_contents)//2)]
        # Aquí estic ficant la edat i el nom de cada integrand de  cada cua.
        # Un exemple de input de cua és este: Cristina 10 Tomas 27
  
    heapify(v[i])  # This builds a max_heap from a list containing pairs of the 
                   # form (-age, name) with the customers in a queue.
                   # Age is stored as a negative number, because heapify builds
                   # a min-priority queue. Using -age instead of age, we get the 
                   # effect of a max-priority queue with respect to age, i.e. the
                   # older customers have higher priority.
                   
  # line_contents = read_line() # This reads the empty line after
  #                             # the n lines describing the queues


  # YOU MUST IMPLEMENT THIS FUNCTION TO FINISH THE PROBLEM
  ordre = read(str)

  print('DEPARTS',end='\n')
  print('-------', end='\n')
   

  while ordre is not None: 

      if ordre == 'LEAVES':
          n_i = read(int)
          if 0 < n_i <= n and len(v[n_i-1]) > 0:
              print(heappop(v[n_i-1])[1], end='\n')

      elif ordre == 'ENTERS':
          name = read(str)
          age = read(float)
          n_i = read(int)
          if 0 < n_i <= n and age >0:
              heappush(v[n_i-1],(-age, name))
      
      ordre = read(str)

  print('')        # Printejo la línia buida entre departs i final contents

  escribe(v)


  # On page 384 of Goodrich's book there is a description of the main functions
  # supported by Python's heapq module. In this problem you must use
  # heappush(L, element), heappop(L), and heapify(L), where L is a list. 

