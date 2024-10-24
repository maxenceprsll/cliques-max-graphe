def BronKerbosch1(R, P, X, cliques_max):
    max_cliques_info = []
    if not P and not X:
        clique_info = (len(R), R)
        cliques_max.append(clique_info)

    for v in list(P):
        BronKerbosch1(R.union({v}), P.intersection(N(v)), X.intersection(N(v)), cliques_max)
        P.remove(v)
        X.add(v)

def N(v):
    graph = {
        1: {2, 3, 4, 5, 6},
        2: {1, 7},
        3: {1, 4, 5},
        4: {1, 3, 6},
        5: {1, 3, 6, 7},
        6: {1, 4, 5, 7, 8, 9},
        7: {2, 5, 6, 8},
        8: {6, 7, 9},
        9: {6, 8}
    }
    return graph.get(v, set())

R = set()
P = {1, 2, 3, 4, 5, 6, 7, 8, 9}
X = set()
cliques_max = []
BronKerbosch1(R, P, X, cliques_max)

cliques_max.sort(reverse=True)

with open("cliques_maximales.txt", "w") as fichier:

    fichier.write(f"Taille maximum des cliques maximales: {cliques_max[0][0]}\n\n\n")
    for clique_info in cliques_max:
        taille_clique, clique = clique_info
        fichier.write(f"Taille de la clique maximale : {taille_clique}\n")
        fichier.write("Clique maximale : " + " ".join(map(str, clique)) + "\n\n")
