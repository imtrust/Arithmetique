import networkx as nx


#création du graphe
g1 = nx.Graph()

#création des sommets
g1.add_node('a')
g1.add_node('b')
g1.add_node('c')
g1.add_node('d')
g1.add_node('e')
g1.add_node('f')
g1.add_node('g')
g1.add_node('h')


#Création des arêtes
g1.add_edge('a','b')
g1.add_edge('a','c')
g1.add_edge('b','d')
g1.add_edge('b','e')
g1.add_edge('c','d')
g1.add_edge('d','e')
g1.add_edge('e','g')
g1.add_edge('e','f')
g1.add_edge('g','f')
g1.add_edge('g','h')



import matplotlib.pyplot as plt


nx.draw(g1, with_labels=True, font_weight='bold', node_size=800, node_color='lightgrey')
plt.show()
    
    
import networkx as nx
import matplotlib.pyplot as plt
#création du graphe à partir de listes
liste1=['a','b','c','d','e','f','g','h']
g2 = nx.Graph()
g2.add_nodes_from(liste1)
liste2=[('a','b'),('a','c'),('b','d'),('b','e'),('c','d'),('d','e'),('e','g'),('e','f'),('g','f'),('g','h')]
g2.add_edges_from(liste2)
nx.draw(g2, with_labels=True, font_weight='bold', node_size=800, node_color='lightgrey')
plt.show()



B = nx.adjacency_matrix(g2)
print(B[(0,0)])
n=len(liste1)
A=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        A[i][j]= B[(i,j)]
print(A)