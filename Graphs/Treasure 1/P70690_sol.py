from easyinput import read

"""
Write a program that, given a map with treasures and obstacles, 
tells if it is possible to reach some treasure from a given initial position. 
The allowed movements are horizontal or vertical, but not diagonal.
"""

# Returns the adjacency list of node corresponding to position (r,c) in map.
def adj(map, node):
  lst = []
  nr = len(map) # number of rows
  if nr == 0: return lst
  nc = len(map[0])  # number of columns
  for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
    ar = node[0] + dr
    ac = node[1] + dc
    if 0 <= ar < nr and 0 <= ac < nc and map[ar][ac] != 'X':    # Comprovo que no m'hagi sortit del map i que no apunte cap node no accessible
      lst.append((ar, ac))
  return lst    # Al ser una quadrícula, retorna els 4 nodes que té al costat (no els de diagonal)


# Returns True if tesor is reachable from node in map
def search(map, disc, node):
  r = node[0]
  c = node[1]
  disc[r][c] = True
  if map[r][c] == 't':  # ja estic al tresor com a posició inicial
      return True
  for ni in adj(map, node):     # per a cada node veí del inicial (adj list)
    if not disc[ni[0]][ni[1]]:      # Si no estàn descoberts
      if search(map, disc, ni): return True     # Comença la cerca des d'aquest
  return False
# Molt recurssiu


if __name__ == '__main__':
    n = read(int)
    m = read(int)
    map = [['.' for _ in range(m)] for _ in range(n)]   # Crear el mapa
    # dics[r][c] means that position at row r and column c has been discovered.
    disc = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
      for j in range(m):
        cell = read(chr)
        if cell != '.': map[i][j] = cell
    r = read(int) - 1
    c = read(int) - 1
    source = (r,c)
    print("yes" if search(map, disc, source) else "no")
    

