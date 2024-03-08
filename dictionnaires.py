# Activité 1
def filtrer_etudiants(etudiants_notes):
    etudiants_sup_15 = {nom: note for nom, note in etudiants_notes.items() if note >= 15}

    return etudiants_sup_15

etudiants_notes = {
    'Alice': 14,
    'Bob': 15.5,
    'Charlie': 16,
    'David': 12,
    'Eva': 17
}

etudiants_sup_15 = filtrer_etudiants(etudiants_notes)
print("Étudiants avec une note moyenne supérieure ou égale à 15:")
for nom, note in etudiants_sup_15.items():
    print(f"{nom}: {note}")

# Activité 2

def produits_en_rupture(stock):
    produits_rupture = {id_produit: details for id_produit, details in stock.items() if details['quantite'] == 0}

    produits_tries = sorted(produits_rupture.items(), key=lambda x: (-x[1]['prix'], x[0]))

    return produits_tries

base_donnees_produits = {
    101: {'nom': 'ProduitA', 'prix': 25.50, 'quantite': 0},
    102: {'nom': 'ProduitB', 'prix': 45.00, 'quantite': 10},
    103: {'nom': 'ProduitC', 'prix': 25.50, 'quantite': 5},
    104: {'nom': 'ProduitD', 'prix': 15.00, 'quantite': 0},
    105: {'nom': 'ProduitE', 'prix': 99.99, 'quantite': 21},
}

produits_rupture_tries = produits_en_rupture(base_donnees_produits)
print("Liste des produits en rupture de stock, triés par prix décroissant:")
for produit in produits_rupture_tries:
    print(produit)
