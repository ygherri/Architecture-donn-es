# Activité 1 
ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

intersection1 = ensemble1.intersection(ensemble2)
print("Intersection (méthode):", intersection1)


intersection2 = ensemble1 & ensemble2
print("Intersection (opérateur):", intersection2)

# Activité 2

ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

difference_symetrique1 = ensemble1.symmetric_difference(ensemble2)
print("Différence symétrique (méthode) :", difference_symetrique1)

difference_symetrique2 = ensemble1 ^ ensemble2
print("Différence symétrique (opérateur) :", difference_symetrique2)
