from easyinput import read
from heapq import heapify, heappop, heappush
'We must perform n tasks, one at a time. Furthermore, some tasks 
'must be done before others: there are m precedence relations between tasks. 
'Write a program to print a way to sort the n tasks satisfying the m given precedences.

'Fico cada relació x abans que y a un edge. Ojo que es directed!
'tasca per fer == indegree'
def ordenacio_topologica(G):
    n = len(G)
    ge = [0] * n
    for u in range(n):
        for i in range(len(G[u])):
            ge[G[u][i]] += 1    # ge conta indegree de u
    
    pq = []
    for i in range(n):
        if ge[i] == 0:  # Tasca independent de cap altra, per tant, primera
            heappush(pq, i) 
            
    l = []
    while len(pq) > 0 :
        x = heappop(pq) 
        l.append(x)
        for i in range(len(G[x])):  # La tasca 1a tasca te indegree 0 pero outdegree != 0
            v = G[x][i]
            ge[v] -= 1  # Com ja s'ha fet la tasca que he ficat a la pq, resto un indegree als veins
            if ge[v] == 0:  # Quan la tasca té indegree 0, la fico a la cua
                heappush(pq, v)
        
    return l
                
                       
if __name__ == '__main__':
    n = read(int)
    m = read(int)
    
    while n is not None and m is not None:
        
        G = [[] for _ in range(n)]
        for i in range(m):
            u = read(int)
            v = read(int)
            G[u].append(v)
        
        ord_top = ordenacio_topologica(G)
        
        for i in range(len(ord_top)-1):
            print(ord_top[i], end=' ')
        print(ord_top[-1], end='\n')
        
        n = read(int)
        m = read(int)
        

# Falta entendre què estem fent.
