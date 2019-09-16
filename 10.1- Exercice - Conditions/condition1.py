# Problème : Etant donné deux variables c et d, on veut savoir si leur produit est négatif ou positif ou nul.
# Contrainte : Ne pas calculer le produit des deux nombres.
# Résultat attendu : Un message affichant "Produit positif" ou "Produit négatif" ou "Produit nul".
# Indications :  Vous pouvez changer les valeurs des variables pour vos tests.
c = -3
d = 12

txt_pos = "Produit positif"
txt_neg = "Produit négatif"
txt_nul = "Produit nul"

if c == 0 or d == 0:
    print(txt_nul)
else:
    if c < 0:
        if d < 0:
            print(txt_pos)
        else:
            print(txt_neg)
    else:
        print(txt_pos)
