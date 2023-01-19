from easyinput import read, read_line

# Mitjançant un diccionari transformo el problema en l'anterior
def dfs(G, u, y, vis):   # Exploro tot, si arribo a y paro
    vis[u] = True
    for v in G[u]:  # G[u] is the list of nieghbours of u
        if not vis[v] and not vis[y]:
            dfs(G, v, y, vis)

if __name__ == '__main__':
    n = read(int)
    dic_nodes = {}
    for i in range(n):
        dic_nodes[read(str)] = i
        
    m = read(int)
    
    G = [[] for _ in range(n)]
    
    for i in range(m):
        u = read(str)
        v = read(str)
        G[dic_nodes[u]].append(dic_nodes[v])

    x = read(str)
    y = read(str)
    
    vis = [False] * n
    dfs(G, dic_nodes[x], dic_nodes[y], vis)

    if vis[dic_nodes[y]]:
        print('yes')
    else:
        print('no')