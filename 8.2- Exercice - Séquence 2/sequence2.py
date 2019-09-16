# Problème : Calculer le prix TTC d'un nombre d'articles ayant un prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75
tva = 0.077
total = nb_articles * prix_ht
total = total + (total * tva)

print("Le prix TTC est de ", round(total, 2), " CHF")
