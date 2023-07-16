from datetime import date, timedelta


if __name__ == "__main__" :
    print("Bienvenue dans l'application Date Anniversaire")

    # Récupération de la date de naissance
    print("Veuillez indiquer la date de naissance de la personne voulue")
    while True :
        date_entree_string = input("La date de naissance au format ISO (AAAA-MM-JJ) : ")
        try :
            date_entree = date.fromisoformat(date_entree_string)
            break
        except :
            print("Une erreur est arrivée. Veuillez réessayer")

    # Récupération du nombre de jours
    print("Veuillez indiquer la le nombre de jours")
    while True :
        jours_string = input("Le nombre de jours : ")
        try :
            jours = int(jours_string)
            delta = timedelta(days=jours)
            break
        except :
            print("Une erreur est arrivée. Veuillez réessayer")

    # Calcul du jours
    date_finale = date_entree + delta

    # Affichage du résultat
    print("Le jour est le", date_finale.isoformat())