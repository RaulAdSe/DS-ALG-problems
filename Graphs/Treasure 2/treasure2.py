from easyinput import read
import collections

"""
Write a program that, given a map with treasures and obstacles, computes the distance 
from a given initial position to the nearest accessible treasure. 
The allowed movements are horizontal or vertical, but not diagonal.
"""

def ok(x, y, map):
    nr = len(map) # number of rows
    if nr == 0: 
        return 
    nc = len(map[0])  # number of columns
    return( 0 <= x < nr and 0 <= y < nc and map[x][y] != 'X') # Comprovo que no m'hagi sortit del map i que no apunte cap node no accessible

def dist_min(orix, oriy, map):
    files = len(map)
    columnes = len(map[0])
    
    q = collections.deque()
    dist = [[0 for _ in range(columnes)] for _ in range(files)] # Molt important! for i in range: for j in range
    
    q.append((orix,oriy))
    dist[orix][oriy] = 0
    
    while len(q) > 0:
        punt = q.popleft()      # Si vull fer servir una queue he de ficar popleft, no obstant, obtinc out of range.
        # Arreglar
        x, y = punt[0], punt[1]
        
        if map[x][y] =='t':     # He arribat al tresor, retorno distància
            return dist[x][y]
            # print(dist[x][y])
        
        map[x][y] = 'X'  # Marco d'on surto com una X per no tornar-hi
        
        if (ok(x+1, y, map)):       # Exploro les 4 direccions
            q.append((x+1,y))
            dist[x+1][y] = dist[x][y] + 1
        if (ok(x-1, y, map)):
            q.append((x-1,y))
            dist[x-1][y] = dist[x][y] + 1
        if (ok(x, y+1, map)):
            q.append((x,y+1))
            dist[x][y+1] = dist[x][y] + 1
        if (ok(x, y-1, map)):
            q.append((x,y-1))
            dist[x][y-1] = dist[x][y] + 1
    return -1       # Si la q està buida, no he trobat cap camí a un tresor.
    
    
    
if __name__ == '__main__':
    n = read(int)
    m = read(int)
    map = [['.' for _ in range(m)] for _ in range(n)]   # Crear el mapa
    for i in range(n):
      for j in range(m):
        cell = read(chr)
        if cell != '.': map[i][j] = cell

    orix = read(int) - 1    # Resto 1 perquè python indexa des de 0
    oriy = read(int) - 1
    
    dist = dist_min(orix, oriy, map)
    
    if(dist == -1):
        print("no treasure can be reached")
    else:
        print("minimum distance: " + str(dist))
    





