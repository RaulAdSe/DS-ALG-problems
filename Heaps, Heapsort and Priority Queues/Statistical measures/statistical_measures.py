from  easyinput import read
import heapq
"""
Write a program to compute the most common statistical measures (minimum, maximum and average) 
of several integer numbers. These numbers are known increasingly. At every moment, 
it is also possible to delete the smallest element.
"""

if __name__ == '__main__':

    q = []
    numeros = 0
    suma = 0
    s = read(str)
    
    while s is not None:
        
        if (s == "number"):
            x = read(int)
            
            if numeros == 0:
                max = min = x
            if len(q) == 0:
                max = x
                
            heapq.heappush(q, x)
            numeros += 1
            suma += x
            average = (suma)/numeros
                        
            if x > max:
                max = x
            if x < min:
                min = x
                
            print('minimum: ' + str(min) +', maximum: '+str(max)+', average: '+str("{0:.4f}".format(average)))
            
        elif s == 'delete':
            if len(q)>0:
                if numeros == 1:
                    delete = q[0]   # Deleting means removing the smallest element
                    suma -= delete
                    heapq.heappop(q)
                    print('no elements')
                    average = suma/numeros
                    numeros -= 1
                    min = max = 0
                else:
                    delete = q[0]   # Deleting means removing the smallest element
                    suma -= delete
                    numeros -= 1
                    average = suma/numeros
                    heapq.heappop(q)
                    min = q[0]
                    print('minimum: ' + str(min) +', maximum: '+str(max)+', average: '+str("{0:.4f}".format(average)))
            else:
                print('no elements')
                
        s = read(str)

                
        
        
                    
                    
                    
                    
            
        