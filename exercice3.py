
from random import random
import itertools

def generegraphe(n, p):
    adj = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1,n):
            if random() < p:
                adj[i][j] = adj[j][i] = 1
            else:
                adj[i][j] = adj[j][i] = 0
    
    return adj


def BronKerbosch(R, P, X, cliques_max, adj_matrix):
    max_cliques_info = []
    if not P and not X:
        clique_info = (len(R), R)
        cliques_max.append(clique_info)

    for v in list(P):
        BronKerbosch(R.union({v}), P.intersection(N(v, adj_matrix)), X.intersection(N(v, adj_matrix)), cliques_max, adj_matrix)
        P.remove(v)
        X.add(v)


def N(v, adj_matrix):
    neighbors = set()
    for i in range(len(adj_matrix[v])):
        if adj_matrix[v][i] == 1:
            neighbors.add(i)
    return neighbors

def arcs_inexistants(adj_matrix):
    arcs = []
    for i in range(len(adj_matrix)):
        for j in range(i+1, len(adj_matrix)):
            if adj_matrix[i][j] == 0:
                arcs.append((i, j))
    return arcs

def ajouter_arcs_tester_clique_max(adj_matrix, arcs_inexistants, k, cliques_max):
    taille_clique_max,b = cliques_max[0]
    #nb_aretes_ajoutees = 0

    adj_matrixnew = [[0]*len(adj_matrix) for _ in range(len(adj_matrix))]
    couples = list(itertools.combinations(arcs_inexistants, k))

    for combinaison in couples:
        # Ajout des arcs de la combinaison au graph
        for u, v in combinaison:
            adj_matrix[u][v] = adj_matrix[v][u] = 1
            #nb_aretes_ajoutees += 1

        # Calcul des cliques maximales après avoir ajouté des arcs
        R = set()
        P = set(range(len(adj_matrix)))
        X = set()
        cliques_max_combinaison = []
        BronKerbosch(R, P, X, cliques_max_combinaison, adj_matrix)
        cliques_max_combinaison.sort(reverse=True)

        # MAJ de la taille de la clique maximale si besoiin
        taille_clique_max_combinaison,b = cliques_max_combinaison[0]
        if taille_clique_max_combinaison > taille_clique_max:
            
            taille_clique_max = taille_clique_max_combinaison
            cliques_max = cliques_max_combinaison

        # On supprime les arcs de la combinaison du graphe
        for u, v in combinaison:
            adj_matrix[u][v] = adj_matrix[v][u] = 0
            #nb_aretes_ajoutees -= 1
    # Mise à jour du graph en remettant les arcs
    for clique in cliques_max:
        clique_liste = list(clique[1])
        for i in range(len(clique_liste)):
            for j in range(i+1, len(clique_liste)):
                adj_matrixnew[clique_liste[i]][clique_liste[j]] = adj_matrixnew[clique_liste[j]][clique_liste[i]] = 1
    
    

    return adj_matrixnew, taille_clique_max, cliques_max


def aff_graphe(graph):
    for n in range(len(graph)):
        print("le voisin de ",n,"est :",end="")
        for e in range(len(graph[n])):
            if(graph[n][e]):
                print(e," ",end="")
        print()


def graphe_complet(graph):
  n = len(graph)
  for i in range(n):
    for j in range(i + 1, n):
      graph[i][j] = 1
      graph[j][i] = 1
  return graph


####



# Afficher les nouvelles cliques maximales
def affichage(n,p):
    graph = generegraphe(n,p)
    print("\nGraphe genere avce n =",n,"et p =",p," nous donne :\n")
    aff_graphe(graph)
    R = set()
    P = set(range(n))
    X = set()
    cliques_max = []
    BronKerbosch(R, P, X, cliques_max, graph)
    cliques_max.sort(reverse=True)

    print("\nNous avons donc un graphe qui a une matrix :",graph)
    print("\nSes cliques sont : ",cliques_max)
    print("Sa clique maximun est de valeur :",cliques_max[0][0],"\n")

    tailleclique = cliques_max[0][0]
    kmax = len(arcs_inexistants(graph))


    for k in range(1,kmax): 

        adj_matrixnew, taille_clique_maxnew, cliques_maxnew = ajouter_arcs_tester_clique_max(graph, arcs_inexistants(graph), k, cliques_max)
        if cliques_maxnew[0][0] > tailleclique : 
            # Affichage :
            print("Le k vaut :",k)
            print("\nSon graph est maintenant : ",adj_matrixnew,"\n")
            aff_graphe(adj_matrixnew)
            print("\nSes cliques sont maintenant : ",cliques_maxnew)
            print("Sa clique maximun est maintenant de valeur: ",cliques_maxnew[0][0],"\n")
            tailleclique = cliques_maxnew[0][0]

        else : 
            print("Notre K vaut :",k,"mais celui-ci n'augmente pas la taille de la clique max")
    
    graphe_comp = graphe_complet(graph)
    R = set()
    P = set(range(n))
    X = set()
    cliques_max = []
    BronKerbosch(R, P, X, cliques_max, graph)
    cliques_max.sort(reverse=True)

    # Affichage graph complet : 
    print("Le k vaut :",kmax,"(Sa valeur maximun car ce graphe ci dessous est complet)")
    print("\nSon graph est maintenant : ",graphe_comp,"\n")
    aff_graphe(graphe_comp)
    print("\nSes cliques sont maintenant : ",cliques_max)
    print("Sa clique maximun est maintenant de valeur: ",cliques_max[0][0],"\n")


n=12
p=0.5

affichage(n,p)


