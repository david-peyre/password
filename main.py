import hashlib
import json
import random
import string
import re

# Vérifie la complexité du mot de passe
def password_secure(password):
    if (
        len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in '!@#$%^&*' for c in password)
    ):
        return True
    else:
        print("Le mot de passe ne respecte pas les exigences de sécurité. Veuillez en choisir un nouveau.")
        return False

# Hashage du mot de passe
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Enregistre le mot de passe dans un fichier JSON
def save_password(username, password):
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}

    # Vérifie si le nom d'utilisateur existe déjà
    if username in passwords:
        print("Nom d'utilisateur déjà existant. Veuillez choisir un autre nom.")
        return

    # Vérifie si le mot de passe existe déjà
    if password in passwords.values():
        print("Ce mot de passe est déjà enregistré. Veuillez choisir un autre mot de passe.")
        return

    passwords[username] = password

    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

# Affiche les mots de passe enregistrés
def display_passwords():
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
            if passwords:
                print("Mots de passe enregistrés :")
                for username, hashed_password in passwords.items():
                    print(f"Nom d'utilisateur : {username}, Mot de passe haché : {hashed_password}")
            else:
                print("Aucun mot de passe enregistré.")
    except FileNotFoundError:
        print("Aucun fichier de mots de passe trouvé.")
    except json.JSONDecodeError:
        print("Erreur de décodage JSON. Le fichier de mots de passe peut être corrompu.")

# Vérifie si un mot de passe est fort
def is_strong_password(password):
    # Vérifie si le mot de passe a au moins 8 caractères
    if len(password) < 8:
        return False

    # Vérifie si le mot de passe a au moins une lettre majuscule
    if not any(c.isupper() for c in password):
        return False

    # Vérifie si le mot de passe a au moins une lettre minuscule
    if not any(c.islower() for c in password):
        return False

    # Vérifie si le mot de passe a au moins un chiffre
    if not any(c.isdigit() for c in password):
        return False

    # Vérifie si le mot de passe a au moins un caractère spécial parmi !@#$%^&*
    if not any(c in '!@#$%^&*' for c in password):
        return False

    return True

# Génère un mot de passe aléatoire
def generate_random_password():
    while True:
        length = random.randint(8, 12)
        characters = string.ascii_letters + string.digits + '!@#$%^&*'
        password = ''.join(random.choice(characters) for i in range(length))

        if is_strong_password(password):
            return password

# Fonction principale
def main():
    while True:
        print("Que désirez-vous faire :")
        print()
        print("1. Ajouter un mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")
        print()

        # Demande à l'utilisateur de choisir une option
        choice = input("Choisissez une option (1, 2 ou 3) : ")

        if choice == '1':
            # Sous-menu pour ajouter un mot de passe
            print("Comment voulez-vous créer le mot de passe :")
            print("1. Créer manuellement")
            print("2. Générer aléatoirement")
            create_choice = input("Choisissez une option (1 ou 2) : ")

            if create_choice == '1':
                # Ajout d'un mot de passe manuellement
                username = input("Nom d'utilisateur : ")
                password = input("Mot de passe : ")
            elif create_choice == '2':
                # Génération d'un mot de passe aléatoire
                username = input("Nom d'utilisateur : ")
                password = generate_random_password()
                print(f"Mot de passe généré : {password}")
            else:
                print("Option invalide. Retour au menu principal.")
                continue

            if password_secure(password):
                hashed_password = hash_password(password)
                save_password(username, hashed_password)
                print("Mot de passe ajouté avec succès!")

        elif choice == '2':
            # Affichage des mots de passe
            display_passwords()

        elif choice == '3':
            # Quitter le programme
            print("Programme terminé.")
            break

        else:
            print("Option invalide, veuillez choisir une option valide.")

# Exécute le programme si le fichier est exécuté directement
if __name__ == "__main__":
    main()
