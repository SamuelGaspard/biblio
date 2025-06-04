# BiblioPy - Gestionnaire de Bibliothèque Simplifié

# Structure de données pour stocker les livres en mémoire
# Chaque livre est un dictionnaire dans une liste
catalogue_livres = []

def ajouter_livre():
    """
    Permet à l'utilisateur d'ajouter un nouveau livre au catalogue.
    Les informations sont saisies via la console.
    """
    print("\n--- Ajouter un nouveau livre ---")
    titre = input("Titre du livre : ").strip()
    auteur = input("Auteur : ").strip()
    isbn = input("ISBN : ").strip()
    annee_publication = input("Année de publication : ").strip()

    # Simple validation pour s'assurer que les champs ne sont pas vides
    if not all([titre, auteur, isbn, annee_publication]):
        print("Erreur : Tous les champs sont obligatoires. Livre non ajouté.")
        return

    # Création d'un dictionnaire pour le nouveau livre
    nouveau_livre = {
        "titre": titre,
        "auteur": auteur,
        "isbn": isbn,
        "annee_publication": annee_publication,
        "statut": "disponible"  # Par défaut, un nouveau livre est disponible
    }
    catalogue_livres.append(nouveau_livre)
    print(f"Livre '{titre}' ajouté avec succès au catalogue.")

def afficher_catalogue():
    """
    Affiche tous les livres actuellement dans le catalogue.
    """
    print("\n--- Catalogue des livres ---")
    if not catalogue_livres:
        print("Le catalogue est vide pour le moment.")
        return

    for i, livre in enumerate(catalogue_livres):
        print(f"\nLivre #{i+1}:")
        print(f"  Titre: {livre['titre']}")
        print(f"  Auteur: {livre['auteur']}")
        print(f"  ISBN: {livre['isbn']}")
        print(f"  Année: {livre['annee_publication']}")
        print(f"  Statut: {livre['statut'].capitalize()}") # Met la première lettre en majuscule

#fonction pour archiver un livre
def archiver_livre(isbn):
    """
    Archive un livre en le retirant du catalogue.
    :param isbn: ISBN du livre à archiver
    """
    global catalogue_livres
    for livre in catalogue_livres:
        if livre['isbn'] == isbn:
            catalogue_livres.remove(livre)
            print(f"Livre '{livre['titre']}' archivé avec succès.")
            return
    print("Livre non trouvé dans le catalogue.")
def emprunter_livre(isbn):
    """
    Permet à un utilisateur d'emprunter un livre.
    :param isbn: ISBN du livre à emprunter
    """
    for livre in catalogue_livres:
        if livre['isbn'] == isbn:
            if livre['statut'] == 'disponible':
                livre['statut'] = 'emprunté'
                print(f"Livre '{livre['titre']}' emprunté avec succès.")
                return
            else:
                print(f"Le livre '{livre['titre']}' est déjà emprunté.")
                return
    print("Livre non trouvé dans le catalogue.")
def retournerlivre(isbn):
    """
    Permet à un utilisateur de retourner un livre emprunté.
    :param isbn: ISBN du livre à retourner
    """
    for livre in catalogue_livres:
        if livre['isbn'] == isbn:
            if livre['statut'] == 'emprunté':
                livre['statut'] = 'disponible'
                print(f"Livre '{livre['titre']}' retourné avec succès.")
                return
            else:
                print(f"Le livre '{livre['titre']}' n'est pas emprunté.")
                return
    print("Livre non trouvé dans le catalogue.")
def supprimer_livre(isbn):
    """
    Supprime un livre du catalogue.
    :param isbn: ISBN du livre à supprimer
    """
    global catalogue_livres
    for livre in catalogue_livres:
        if livre['isbn'] == isbn:
            catalogue_livres.remove(livre)
            print(f"Livre '{livre['titre']}' supprimé avec succès.")
            return
    print("Livre non trouvé dans le catalogue.")

def rechercher_livre(isbn):
    """
    Recherche un livre par son ISBN dans le catalogue.
    :param isbn: ISBN du livre à rechercher
    """
    for livre in catalogue_livres:
        if livre['isbn'] == isbn:
            print("\n--- Livre trouvé ---")
            print(f"Titre: {livre['titre']}")
            print(f"Auteur: {livre['auteur']}")
            print(f"ISBN: {livre['isbn']}")
            print(f"Année de publication: {livre['annee_publication']}")
            print(f"Statut: {livre['statut'].capitalize()}")
            return
    print("Livre non trouvé dans le catalogue.")
def retourner_livre(isbn):
    """
    Permet à un utilisateur de retourner un livre emprunté.
    :param isbn: ISBN du livre à retourner
    """
    for livre in catalogue_livres:
        if livre['isbn'] == isbn:
            if livre['statut'] == 'emprunté':
                livre['statut'] = 'disponible'
                print(f"Livre '{livre['titre']}' retourné avec succès.")
                return
            else:
                print(f"Le livre '{livre['titre']}' n'est pas emprunté.")
                return
    print("Livre non trouvé dans le catalogue.")

def menu_principal():
    """
    Affiche le menu principal de l'application et gère les choix de l'utilisateur.
    """
    while True:
        print("\n--- Menu BiblioPy ---")
        print("1. Ajouter un livre OK")
        print("2. Afficher le catalogue OK")
        print("3. Archiver un livre OK")
        print("4. rechercher un livre OK")
        print("5. retourner un livre OK")
        print("6. emprunter un livre OK")
        print("7. supprimer un livre OK")
        print("8. Quitter")
        choix = input("Votre choix : ").strip()

        if choix == '1':
            ajouter_livre()
        elif choix == '2':
            afficher_catalogue()
        elif choix == '3':
            isbn = input("Entrez l'ISBN du livre à archiver : ").strip()
            archiver_livre(isbn)
        elif choix == '4':
            isbn = input("Entrez l'ISBN du livre à rechercher : ").strip()
            rechercher_livre(isbn)
        elif choix == '5':
            isbn = input("Entrez l'ISBN du livre à retourner : ").strip()
            retournerlivre(isbn)
        elif choix == '6':
            isbn = input("Entrez l'ISBN du livre à emprunter : ").strip()
            emprunter_livre(isbn)
        elif choix == '7':
            isbn = input("Entrez l'ISBN du livre à supprimer : ").strip()
            supprimer_livre(isbn)
        elif choix == '8':
            print("Merci d'avoir utilisé BiblioPy. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Point d'entrée de l'application
if __name__ == "__main__":
    menu_principal()
