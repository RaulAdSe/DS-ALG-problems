from easyinput import read, read_line
"""
Given a directed graph, calculate how many strongly connected components it has.
"""

# Algorithm:
    # Reverse graph
    # Dft on G, stack fully explored nodes in order
    # pop stack and Dft on Gt
    # count +1 till stack empty


# DFS visit all the connected vertices of the given vertex. Stacks them in order of explored
def DFSUtil_stack(G, v, vis, stack):
        # Mark the current node as visited
        vis[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in G[v]:
            if (not vis[i]):
                DFSUtil_stack(G, i, vis, stack)
        stack.append(v)     

# El mateix però sense guardar al stack. 
def DFSUtil(G, v, vis):
        # Mark the current node as visited
        vis[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in G[v]:
            if (not vis[i]):
                DFSUtil(G, i, vis)

def count_comp(G, Gt):
    
    # Dfs in input graph
    stack = []
    count = 0
    vis = [0] * len(G)
    for i in range(n):
        if vis[i] == 0:     # Si està explorat explorat ...
            DFSUtil_stack(G, i, vis, stack) # Quan algún vis es torni True això hauria de apendejar al stack
    
    # Dfs in reverse graph using stack
    vis = [0] * len(G)  # reset visited values
    while len(stack) > 0:
        v = stack.pop() # Vaig treient (LIFO) el stack 
        if vis[v] == 0:
            DFSUtil(Gt, v, vis)
            count += 1
    return count


if __name__ == '__main__':
    
    graph_num = 1

    nn = read(int)
    for k in range(nn):     # k son els casos
        n = read(int)
        G = [[] for _ in range(n)]
        Gt = [[] for _ in range(n)]
        m = read(int)
        for i in range(m):
            u = read(int)
            v = read(int)
            G[u].append(v)
            Gt[v].append(u)

        count = count_comp(G, Gt)
        print('Graph #'+str(graph_num)+' has '+str(count)+' strongly connected component(s).')
        graph_num += 1


 
