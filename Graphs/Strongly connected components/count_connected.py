from easyinput import read, read_line

# def dfs(G, u, y, vis):
#     vis[u] = True
#     for v in G[u]:  # G[u] is the list of nieghbours of u
#         if not vis[v] and not vis[y]:
#             dfs(G, v, y, vis)

# DFS visit all the connected vertices of the given vertex.
def DFSUtil(G, v, vis):
 
        # Mark the current node as visited
        vis[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in G[v]:
            if (not vis[i]):
                DFSUtil(G, i, vis)

# Function to return the number of connected components in an undirected graph
# DFS visit all the connected vertices of the given vertex.
# When iterating over all vertices, whenever we see unvisited node, it is because it was not visited by DFS done on vertices so far.
# That means it is not connected to any previous nodes visited so far i.e it was not part of previous components.
# Hence this node belongs to new component.
def NumberOfconnectedComponents(G):
    n = len(G)
    # Mark all the vertices as not visited
    vis = [False]*n
    # To store the number of connected components
    count = 0
     
    for v in range(n):
        if vis[v] == False:
            count += 1
            DFSUtil(G, v, vis)  # Aquí estic contant connected components!!
             
    return count

if __name__ == '__main__':
    # n = read(int)     # Això ho he de fer com read_line perque m pot ser None!
    # m = read(int)
    
    txt = read_line()
    graph_num = 1
    # count = 0   # He vist qeu dfs del mateix node SI em dona True


    while txt is not None:
        possibles_numeros = [int(s) for s in txt.split() if s.isdigit()]
        n = possibles_numeros[0]
        if len(possibles_numeros)>1:
            m = possibles_numeros[1]
        else:
            m = None
        
        if m is not None:
        
            G = [[] for _ in range(n)]
            
            for i in range(m):
                u = read(int)
                v = read(int)
                G[u].append(v)
        
            read_line() # empty line
            count = NumberOfconnectedComponents(G)
            
            if count > 1:
                count += 1
            
            print('Graph #'+str(graph_num)+' has '+str(count)+' strongly connected component(s).')
            
            txt = read_line()
            graph_num += 1
                        
        else:
            read_line()  # empty line
            txt = read_line()


 
