# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

maximum = 0
pos_i = 0
pos_j = 0

for i in range(0, len(tab)):
    for j in range(0, len(tab[i])):
        print(tab[i][j])
        if tab[i][j] > maximum:
            maximum = tab[i][j]
            pos_i = i
            pos_j = j

sortie = "La valeur maximum est : {} et elle se trouve à l'indice [{}][{}]".format(maximum, pos_i, pos_j)

print(sortie)
