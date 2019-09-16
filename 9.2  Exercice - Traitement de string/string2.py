# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

textsplit = texte.split()

nb = 0

for i in textsplit:
    if i.find("exemple") >= 0:
        print(i)
        nb += 1

print("Nombres d'occurence du mot exemple : ", nb)
