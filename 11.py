# Ce programme permet de demander à l'utilisateur de saisir un nom
# et de vérifier si ce nom existe dans une liste prédéfinie de noms.

# Liste des noms prédéfinis
noms = ["Ahmed", "Nadia", "Chouaib", "Adam", "Zainab", "Youness"]

# Demande à l'utilisateur de saisir un nom
name = input("Veuillez saisir un nom: ")
position=indice
# Vérifie si le nom saisi par l'utilisateur existe dans la liste 'noms'
if name in noms:
    # Affiche un message si le nom est trouvé dans la liste
    print(f"{name} existe dans la liste ")
else:
    # Affiche un message si le nom n'est pas trouvé dans la liste
    print(f"{name} n'existe pas dans la liste.")