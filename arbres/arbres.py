# Activité 1
class Noeud:
    def __init__(self, valeur):
        self.gauche = None
        self.droit = None
        self.valeur = valeur

def parcours_prefixe(noeud):
    if noeud:
        print(noeud.valeur, end=' ')
        parcours_prefixe(noeud.gauche)
        parcours_prefixe(noeud.droit)


racine = Noeud(1)
racine.gauche = Noeud(2)
racine.droit = Noeud(3)
racine.gauche.gauche = Noeud(4)
racine.gauche.droit = Noeud(5)

print("Parcours préfixé de l'arbre:")
parcours_prefixe(racine)
