import hashlib
import json
import random
import string

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

    # Vérifie si le mot de passe n'est pas déjà enregistré
    if username in passwords:
        print("Nom d'utilisateur déjà existant. Veuillez choisir un autre nom.")
        return

    passwords[username] = hashed_password

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

# Génère un mot de passe aléatoire
def generate_random_password():
    length = random.randint(8, 12)
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    return ''.join(random.choice(characters) for i in range(length))

# Fonction principale
def main():
    while True:
        print("Que désirez-vous faire :")
        print()
        print("1. Ajouter un mot de passe")
        print("2. Générer un mot de passe aléatoire")
        print("3. Afficher les mots de passe")
        print("4. Quitter")
        print()

        # Demande à l'utilisateur de choisir une option
        choice = input("Choisissez une option (1, 2, 3 ou 4) : ")

        if choice == '1':
            # Ajout d'un mot de passe
            username = input("Nom d'utilisateur : ")

            # Vérifie si le nom d'utilisateur existe déjà
            with open('passwords.json', 'r') as file:
                passwords = json.load(file)
                if username in passwords:
                    print("Nom d'utilisateur déjà existant. Veuillez choisir un autre nom.")
                    continue

            # Demande à l'utilisateur s'il veut entrer manuellement le mot de passe
            manual_entry = input("Voulez-vous entrer manuellement le mot de passe ? (o/n) : ").lower()

            if manual_entry == 'o':
                password = input("Mot de passe : ")
            else:
                # Génère un mot de passe aléatoire qui respecte les exigences
                password = generate_random_password()

                print(f"Mot de passe généré : {password}")

            if password_secure(password):
                hashed_password = hash_password(password)
                save_password(username, hashed_password)
                print("Mot de passe ajouté avec succès!")