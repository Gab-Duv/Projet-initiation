def calculatrice():
    print("Choisissez une opération :")
    print("1. addition")
    print("2. soustraction")
    print("3. multiplication")
    print("4. division")

    # Récupérer l'entrée de l'utilisateur
    choix = input("Entrez votre choix (1/2/3/4) : ")

    # Vérifier si le choix est valide
    if choix in ["1", "2", "3", "4"]:
        try:
            a = float(input("Entrez le premier nombre (a) : "))
            b = float(input("Entrez le second nombre (b) : "))

            if choix == "1":
                print("Résultat :", a + b)

            elif choix == "2":
                print("Résultat :", a - b)

            elif choix == "3":
                print("Résultat :", a * b)

            elif choix == "4":
                try:
                    print("Résultat :", a / b)
                except ZeroDivisionError:
                    print("La division par 0 est impossible.")

        except ValueError:
            print("Veuillez entrer des nombres valides.")
    else:
        print("Veuillez entrer un choix valide entre 1 et 4.")

calculatrice()