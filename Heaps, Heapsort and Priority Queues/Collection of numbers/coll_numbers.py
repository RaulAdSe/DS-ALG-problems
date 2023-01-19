"""
Write a program to keep a collection of integer numbers, perhaps with repetitions, 
while performing the following operations: 
"""

from easyinput import read, read_line
import heapq


if __name__ == "__main__":
	
    consulta = read(str)
    heap = []
    
    while consulta is not None:		
        
        if(consulta == 'S'):
            x = read(int)
            heapq.heappush(heap,-x)
            # Stores a copy of the given number x
        
        elif (consulta == 'A' and len(heap)>0):
            print(-heap[0])
            #  Asks for the greatest number
            
        elif(consulta == 'R' and len(heap)>0):
            heapq.heappop(heap) 
            # Removes the greatest number (one of them, if it is repeated).

        elif(consulta == 'I'):
            x = read(int)
            if len(heap)>0:
                result = - heapq.heappop(heap)  + x           
                heapq.heappush(heap,-result)
            else:
                print('error!')
        # Increases the greatest number (one of them, if it is repeated) in x units.

        elif(consulta == 'D'):
            x = read(int)
            if len(heap)>0:
                result = - heapq.heappop(heap)  - x           
                heapq.heappush(heap,-result)
            else:
                print('error!')
        # Decreases the greatest number (one of them, if it is repeated) in x units.
                
        else:
            print('error!')
            
        consulta = read(str) 
