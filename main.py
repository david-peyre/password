import hashlib
import json

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
def save_password(username, hashed_password):
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}

    passwords[username] = hashed_password

    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

# Affiche les mots de passe enregistrés
def display_passwords():
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}

    if passwords:
        print("Mots de passe enregistrés :")
        for username, hashed_password in passwords.items():
            print(f"Nom d'utilisateur : {username}, Mot de passe haché : {hashed_password}")
    else:
        print("Aucun mot de passe enregistré.")

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
            # Ajout d'un mot de passe
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")

            if password_secure(password):
                hashed_password = hash_password(password)
                save_password(username, hashed_password)
                print("Mot de passe ajouté avec succès!")
            else:
                print("Le mot de passe ne respecte pas les exigences de sécurité. Veuillez en choisir un nouveau :")

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
