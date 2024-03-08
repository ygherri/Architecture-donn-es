
# Activité 4
def compter_palindromes(liste_mots):
    compteur = 0

    for mot in liste_mots:
        if mot == mot[::-1]:
            compteur += 1

    return compteur

liste_mots = ["radar", "python", "level", "world", "madam", "kayak"]
nombre_palindromes = compter_palindromes(liste_mots)
print("Nombre de palindromes dans la liste :", nombre_palindromes)
