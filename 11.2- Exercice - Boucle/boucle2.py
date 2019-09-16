# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

B = sorted(B)

print(B)

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

for i in range(0, len(B) - 1):
    for j in range(0, len(B) - 1):
        if B[i] < B[j]:
            print(B[i])
            print(B[j])
            B.insert(j-1, B[i])
            B.pop(i)

print(B)
