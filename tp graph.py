G = dict()
G['a'] = ['b','c']
G['b'] = ['a','d','e']
G['c'] = ['a','d']
G['d'] = ['b','c','e']
G['e'] = ['b','d','f','g']
G['f'] = ['e','g']
G['g'] = ['e','f','h']
G['h'] = ['g']


liste=['a','b','c','d','e','f','g','h']
n=len(liste)
A=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if liste[j] in G[liste[i]]:
            A[i][j]=1

print(G.keys()) # affiche les clés
print(G.values()) # affiche les valeurs
print(len(G)) # affiche le nombre de clés
print(G['e'])



# G.keys() et G.values() sont itérables
# affiche les valeurs du dictionnaire
for el in G.values():
    print(el)
#affiche les clés et les valeurs des clés
for key in G.keys():
    print(key,G[key])