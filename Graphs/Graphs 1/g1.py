from easyinput import read

def dfs(G, u, y, vis):  # miro si puc arribar de u a y
    vis[u] = True
    for v in G[u]:  # G[u] is the list of nieghbours of u
        if not vis[v] and not vis[y]:
            dfs(G, v, y, vis)

if __name__ == '__main__':
    n = read(int)
    m = read(int)
    
    G = [[] for _ in range(n)]
    
    for i in range(m):
        u = read(int)
        v = read(int)
        G[u].append(v)

    x = read(int)
    y = read(int)
    
    vis = [False] * n
    dfs(G, x, y, vis)

    if vis[y]:
        print('yes')
    else:
        print('no')