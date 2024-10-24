from random import random

def generegraphe(n, p):
    adj = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1,n):
            if random() < p:
                adj[i][j] = adj[j][i] = 1
            else:
                adj[i][j] = adj[j][i] = 0
    
    return adj

def BronKerbosch1(R, P, X, cliques_max, adj_matrix):
    max_cliques_info = []
    if not P and not X:
        clique_info = (len(R), R)
        cliques_max.append(clique_info)

    for v in list(P):
        BronKerbosch1(R.union({v}), P.intersection(N(v, adj_matrix)), X.intersection(N(v, adj_matrix)), cliques_max, adj_matrix)
        P.remove(v)
        X.add(v)

def N(v, adj_matrix):
    neighbors = set()
    for i in range(len(adj_matrix[v])):
        if adj_matrix[v][i] == 1:
            neighbors.add(i)
    return neighbors

def avg(tab):
    sum = 0
    for e in tab:
        sum+=e
    return sum/len(tab)

res = []
for n in range(1,11):
    for p in range(11):
        resultat = [] 
        for i in range(100):
   
            graph = generegraphe(n, p/10)

            R = set()
            P = set(range(n))
            X = set()
            cliques_max = []
            BronKerbosch1(R, P, X, cliques_max, graph)

            cliques_max.sort(reverse=True)
            resultat.append(cliques_max[0][0])
        res.append([n,p/10,avg(resultat)])


print(res)