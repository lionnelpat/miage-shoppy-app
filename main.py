# =========================================================
# PROJET : PANIER DE BOUTIQUE E-COMMERCE (Restaurant)
# Correction simple - Licence 1 MIAGE
# =========================================================

TAUX_TVA = 0.18  # 18% de TVA

# -----------------------------------------------------
# Le menu du restaurant : une liste de dictionnaires
# Chaque plat est représenté par un dictionnaire
# -----------------------------------------------------
menu = [
    {"nom": "Thiebou Dieune", "prix": 2500},
    {"nom": "Yassa Poulet", "prix": 2000},
    {"nom": "Mafe", "prix": 1800},
    {"nom": "Domoda", "prix": 1700},
    {"nom": "Salade Cesar", "prix": 1500},
    {"nom": "Poulet DG", "prix": 4000 },
    {"nom": "Ndolé", "prix": 3000 }
]

# -----------------------------------------------------
# Le panier : une liste de dictionnaires
# Chaque élément du panier ressemble à :
# {"nom": "Mafe", "prix": 1800, "quantite": 2}
# -----------------------------------------------------
panier = []


# =========================================================
# FONCTION : Afficher le menu du jour
# =========================================================
def afficher_menu_du_jour():
    print("\n--- MENU DU JOUR ---")
    for i in range(len(menu)):
        plat = menu[i]
        print(f"{i + 1}. {plat['nom']} - {plat['prix']} FCFA")


# =========================================================
# OPTION 1 : Afficher le menu et ajouter un plat au panier
# =========================================================
def ajouter_plat():
    afficher_menu_du_jour()

    # --- Validation du choix du plat avec une boucle while ---
    choix_valide = False
    while not choix_valide:
        choix = input("\nEntrez le numéro du plat à ajouter : ")

        if choix.isdigit() and 1 <= int(choix) <= len(menu):
            choix = int(choix)
            choix_valide = True
        else:
            print("Numéro invalide. Veuillez réessayer.")

    plat_choisi = menu[choix - 1]

    # --- Validation de la quantité avec try/except ---
    quantite_valide = False
    while not quantite_valide:
        try:
            quantite = int(input("Entrez la quantité : "))
            if quantite <= 0:
                print("La quantité doit être supérieure à 0.")
            else:
                quantite_valide = True
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    # --- Vérifier si le plat existe déjà dans le panier ---
    plat_deja_present = False
    for article in panier:
        if article["nom"] == plat_choisi["nom"]:
            article["quantite"] = article["quantite"] + quantite
            plat_deja_present = True
            print(f"Quantité mise à jour pour {plat_choisi['nom']}.")
            break

    # --- Sinon, on l'ajoute comme nouvel article ---
    if not plat_deja_present:
        nouvel_article = {
            "nom": plat_choisi["nom"],
            "prix": plat_choisi["prix"],
            "quantite": quantite,
        }
        panier.append(nouvel_article)
        print(f"{plat_choisi['nom']} ajouté au panier.")


# =========================================================
# OPTION 2 : Supprimer un plat du panier
# =========================================================
def supprimer_plat():
    if len(panier) == 0:
        print("\nLe panier est vide.")
        return

    lister_panier()

    nom_valide = False
    while not nom_valide:
        nom_plat = input("\nEntrez le nom du plat à supprimer : ")

        plat_trouve = False
        for article in panier:
            if article["nom"].lower() == nom_plat.lower():
                panier.remove(article)
                print(f"{article['nom']} a été supprimé du panier.")
                plat_trouve = True
                nom_valide = True
                break

        if not plat_trouve:
            print("Ce plat n'existe pas dans le panier. Réessayez.")


# =========================================================
# OPTION 3 : Lister tous les plats du panier
# =========================================================
def lister_panier():
    if len(panier) == 0:
        print("\nLe panier est vide.")
        return

    print("\n--- CONTENU DU PANIER ---")
    for article in panier:
        print(f"{article['nom']} ({article['quantite']}) - {article['prix']} FCFA/u")


# =========================================================
# OPTION 4 : Vider le panier
# =========================================================
def vider_panier():
    panier.clear()
    print("\nLe panier a été vidé.")


# =========================================================
# OPTION 5 : Afficher la facture (HT, TVA, TTC)
# =========================================================
def afficher_facture():
    if len(panier) == 0:
        print("\nLe panier est vide. Aucune facture à afficher.")
        return

    montant_ht = 0
    print("\n--- FACTURE ---")
    for article in panier:
        sous_total = article["prix"] * article["quantite"]
        montant_ht = montant_ht + sous_total
        print(f"{article['nom']} x{article['quantite']} = {sous_total} FCFA")

    montant_tva = montant_ht * TAUX_TVA
    montant_ttc = montant_ht + montant_tva

    print(f"\nMontant HT  : {montant_ht} FCFA")
    print(f"TVA (18%)   : {montant_tva} FCFA")
    print(f"Montant TTC : {montant_ttc} FCFA")


# =========================================================
# PROGRAMME PRINCIPAL
# =========================================================
def afficher_menu_programme():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Afficher le menu du jour et ajouter un plat")
    print("2. Supprimer un plat du panier")
    print("3. Lister les plats du panier")
    print("4. Vider le panier")
    print("5. Afficher la facture")
    print("6. Quitter")


def main():
    programme_actif = True

    while programme_actif:
        afficher_menu_programme()
        choix = input("Votre choix (1-6) : ")

        if choix == "1":
            ajouter_plat()
        elif choix == "2":
            supprimer_plat()
        elif choix == "3":
            lister_panier()
        elif choix == "4":
            vider_panier()
        elif choix == "5":
            afficher_facture()
        elif choix == "6":
            print("\nMerci et à bientôt !")
            programme_actif = False
        else:
            print("\nOption invalide. Veuillez choisir un nombre entre 1 et 6.")


# Point d'entrée du programme
if __name__ == "__main__":
    main()