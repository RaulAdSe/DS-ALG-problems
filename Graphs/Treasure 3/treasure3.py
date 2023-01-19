from easyinput import read
import collections

# La funció anterior em dia que ee (poc eficient)

def ok(x, y, map):
    nr = len(map) # number of rows
    if nr == 0: 
        return 
    nc = len(map[0])  # number of columns
    return( 0 <= x < nr and 0 <= y < nc and map[x][y] != 'X') # Comprovo que no m'hagi sortit del map i que no apunte cap node no accessible

def num_tres(x,y,map):
    if ok (x,y,map):
        trobats = map[x][y] =='t'   # M'estalvio el if 
        map[x][y] ='X'     # marcat com visitat
        cont = (num_tres(x+1,y,map) + num_tres(x,y+1,map) + num_tres(x-1,y,map) + num_tres(x,y-1,map))
        return cont + trobats
    return 0    # Aqui trobats serà 0

    
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
    
    map2 = map.copy()
    num_tresors = num_tres(orix,oriy,map)
    
    print(num_tresors)
  





