# Activité 1
def afficher_tuple_max(liste_tuples):
    if not liste_tuples:
        print("La liste est vide.")
        return

    tuple_max = liste_tuples[0]

    for tuple in liste_tuples:
        if len(tuple) > len(tuple_max):
            tuple_max = tuple
    print("Le tuple avec le plus d'éléments est :", tuple_max)

liste_tuples = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10,)]
afficher_tuple_max(liste_tuples)

# Activité 2
def inverser_tuples(liste_tuples):
    return [tuple(reversed(t)) for t in liste_tuples]

liste_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
tuples_inverses = inverser_tuples(liste_tuples)
print(tuples_inverses)
