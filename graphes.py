# Activité 1
graphe = {
  "A": ["B", "C"],
  "B": ["A", "D", "E"],
  "C": ["A", "F"],
  "D": ["B"],
  "E": ["B", "F"],
  "F": ["C", "E"]
}

print("Représentation du graphe :")
for sommet, voisins in graphe.items():
  print(f"{sommet} -> {voisins}")

# Activité 2
def dfs(graphe, noeud, visite=None):
  if visite is None:
    visite = set()
  visite.add(noeud)
  print(noeud)
  for voisin in graphe[noeud]:
    if voisin not in visite:
      dfs(graphe, voisin, visite)
  return visite

graphe = {
  'A': ['B', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'F'],
  'D': ['B'],
  'E': ['B', 'F'],
  'F': ['C', 'E']
}

visite = dfs(graphe, 'A')
