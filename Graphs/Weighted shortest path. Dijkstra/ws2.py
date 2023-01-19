"Write a program that, given a directed graph with positive costs at the arcs, and two vertices x and y, "
"prints the path of minimum cost that goes from x to y."

from heapq import heapify, heappop, heappush
from easyinput import read, read_line

def write(v, pare):
    if v == origen:
        print(v, end ='')
    else:
        write(pare[v],pare) #recursiu
        print(' ' +str(v), end ='')
        
def dijkstra(G, origen, destino, pare):
    acabat = [False] * n
    dist[origen] = 0
    pq = []
    heappush(pq,(0, origen))    # Pars: <vertex,dist>
    
    while len(pq)>0:
        # p = pq[0][0]    # extreiem el pes
        # v = pq[0][1]    # extreiem el vertex
        p, v = heappop(pq) 
        
        if acabat[v] == False:   # Sol testejo camins si no he acabat amb el node

            if v== destino: # quan trobo el desti acaba
                return
            # for i in range(len(G[v])):
            #     pes = G[v][i][0]  # extreiem el pes de v a adj
            #     adj = G[v][i][1]    # extreuen el vertex adjacent a v
            for pes, adj in G[v]:
                if p + pes < dist[adj]:
                    pare[adj] = v
                    dist[adj] = p + pes
                    heappush(pq,(dist[adj], adj))
                acabat[v] = True    # Quan acabo d'explorar tots els veins ja he acabat este node. No aniria un indent més a l'esquerra?


if __name__ == '__main__':
    n = read(int)
    m = read(int)
    
    while n is not None and m is not None:
       
       G = [[] for _ in range(n)]
       
       for i in range(m):
           a = read(int)
           b = read(int)
           c = read(int)
           G[a].append((c,b))

       origen = read(int)
       destino = read(int)
       dist = [float('inf')]*n    # dijkstra va canviant destino
       pare = [0]*n     # dijkstra va canviant pare

       dijkstra(G, origen, destino, pare)
       
       if dist[destino] != float('inf'):
           write(destino,pare)
           print()
       else:
           print("no path from " + str(origen) + " to " +str(destino))
           
       n = read(int)
       m = read(int)