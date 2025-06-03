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
    print(f"Livre '{titre}' ####################ajouté avec succès au catalogue############################.")

def afficher_catalogue():
    """
    Affiche tous les livres actuellement dans le catalogue.
    """
    print("\n####################################Catalogue des livres############################################## ---")
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

def menu_principal():
    """
    Affiche le menu principal de l'application et gère les choix de l'utilisateur.
    """
    while True:
        print("\n--- Menu BiblioPy ---")
        print("1. Ajouter un livre")
        print("2. Afficher le catalogue")
        print("3. quitter")
        print("4. Archiver un livre")
        print("5. Rechercher un livre")
        print("6. Supprimer un livre")
        print("7. Mettre à jour un livre")
        print("8. Emprunter un livre")
        print("9. Retourner un livre")
        print("10. Afficher les livres empruntés")
        print("0. Quitter")

        choix = input("Votre choix : ").strip()

        if choix == '1':
            ajouter_livre()
        elif choix == '2':
            afficher_catalogue()
        elif choix == '3':
            #quitte()
        #elif choix == '4':
            #archiver_un_livre()
        #elif choix == '5':
            #Rechercher_un_livre()
        #elif choix == '6':
            ()
        #elif choix == '7':
            #archiver_un_livre()
        
        

            #print("Merci d'avoir utilisé BiblioPy. Au revoir !")
        elif choix =='4' :
            
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Point d'entrée de l'application
if __name__ == "__main__":
    menu_principal()
