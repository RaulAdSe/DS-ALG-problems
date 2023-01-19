from easyinput import read
import collections

# def ok(x, y, map):
#     nr = len(map) # number of rows
#     if nr == 0: 
#         return 
#     nc = len(map[0])  # number of columns
#     return( 0 <= x < nr and 0 <= y < nc and map[x][y] != 'X') # Comprovo que no m'hagi sortit del map i que no apunte cap node no accessible

def dist_min(orix, oriy, map):
    files = len(map)
    columnes = len(map[0])
    
    q = collections.deque()
    dist = [[0 for _ in range(columnes)] for _ in range(files)] # Molt important! for i in range: for j in range
    maxDist = -1
    
    q.append((orix,oriy))
    dist[orix][oriy] = 0
    
    while len(q) > 0:
        punt = q.popleft()      
        x, y = punt[0], punt[1]
        
        if map[x][y] != 'X':    # Si puc arribar per dos llocs alhoral'element x,y entrarà a la cua dos cops!
            
            if map[x][y] =='t':     # He arribat al tresor, retorno distància
                maxDist = dist[x][y]    # Com faig servir una queue el ultim element serà el que tingue dist màxima
            
            map[x][y] = 'X'  # Marco d'on surto com una X per no tornar-hi
            
            if (0 <= x + 1 < files and 0 <= y < columnes and map[x+1][y] != 'X'):
                q.append((x+1,y))
                dist[x+1][y] = dist[x][y] + 1
            if (0 <= x - 1 < files and 0 <= y < columnes and map[x-1][y] != 'X'):
                q.append((x-1,y))
                dist[x-1][y] = dist[x][y] + 1
            if (0 <= x < files and 0 <= y + 1< columnes and map[x][y+1] != 'X'):
                q.append((x,y+1))
                dist[x][y+1] = dist[x][y] + 1
            if (0 <= x < files and 0 <= y -1 < columnes and map[x][y-1] != 'X'):
                q.append((x,y-1))
                dist[x][y-1] = dist[x][y] + 1
    return maxDist     # He explorat tot el mapa
    
    
    
if __name__ == '__main__':
    n = read(int)
    m = read(int)
    map = [['.' for _ in range(m)] for _ in range(n)]   # Crear el mapa
    for i in range(n):
      for j in range(m):
        map[i][j] = read(chr)
        # if cell != '.':  = cell

    orix = read(int) - 1    # Resto 1 perquè python indexa des de 0
    oriy = read(int) - 1
    
    maxDist = dist_min(orix, oriy, map)
    
    if(maxDist == -1):
        print("no treasure can be reached")
    else:
        print("maximum distance: " + str(maxDist))