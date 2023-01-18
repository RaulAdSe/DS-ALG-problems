from easyinput import read_line, read
from collections import deque

# def supermarket(n, info_inicial):
#     list_d = []
    
#     for i in range(n):
#         list_d.append(deque())
        
#     for i in range(n):
#         for j in range(len(info_inicial[i].split())):
#             list_d[i].append(info_inicial[i].split()[j])
#     return(list_d)

if __name__ == "__main__":
    
     n =  read(int)     #La primera expresió és n
     # names_fila = []
     
     # for i in range(n):
     #     nam = read_line()
     #     names_fila.append(nam)
     # En lloc de guardar totes les files i anar donant-li-les una per una a cada queue dintre de la funció supermarket ho faig directament!
     
     
     list_of_queues = []
     
     for i in range(n):
         line = read_line()
         list_of_queues.append(deque(line.split()))
     
         
     # list_of_queues  = supermarket(n, names_fila)
     
     # Print name of the customers that leave the queues, in the order that they departed

     read_line() # Llegeix la empty line entremig

     ordre = read(str)

     print('DEPARTS',end='\n')
     print('-------', end='\n')
     
     # ordre = read(str)    
     # No consigo salir  de este bucle
     while ordre is not None: 
     #ordre == 'LEAVES' or ordre == 'ENTERS' :

         if ordre == 'LEAVES':
                 n_i = read(int)
                 if 0 < n_i <= n and len(list_of_queues[n_i-1]) > 0:
                     print(list_of_queues[n_i-1].popleft(), end='\n')

         elif ordre == 'ENTERS':
                 name = read(str)
                 n_i = read(int)
                 if 0 < n_i <= n:
                     list_of_queues[n_i-1].append(name)
        
         ordre = read(str)
         # line = read_line()
         # try:
         #     ordre = line.split()[0]
         # except:
         #     ordre = None

     print('')        # Printejo la línia buida entre departs i final contents

     # Print de la info final
     print('FINAL CONTENTS', end='\n')
     print('--------------', end='\n')
     for i in range(n):
         if len(list_of_queues[i]) == 0:                   # Si no hi ha ningú a la fila que ploteje buida i canvie de linia
            print('queue {}:'.format(i+1), end='\n')
         else:
             print('queue {}:'.format(i+1), end=' ')
         
         for j in range(len(list_of_queues[i])):
             #if j == len(list_of_queues[i]) - 1:         # Això no hagués fucionat mai perque la queue es va actualitzant, llavors la len varia!
            if len(list_of_queues[i]) == 1:                 # Ara si, quan sol quedi un element
                print('{}'.format(list_of_queues[i].popleft()), end='\n')       # Quan sigui l'últim de la cua que canvie de linia
            else:
                print('{}'.format(list_of_queues[i].popleft()), end=' ')




    # El read no acabe bé al spyder!!











