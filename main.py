import hashlib
import json
import getpass
import os  # Module pour vérifier l'existence du fichier

def hash_password(password):
    # Fonction pour hacher le mot de passe avec SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def save_passwords(passwords):
    # Enregistre les mots de passe hachés dans un fichier JSON
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

def load_passwords():
    # Charge les mots de passe depuis le fichier JSON
    passwords = {}
    if os.path.exists('passwords.json'):
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    return passwords

def add_password():
    # Ajoute un nouveau mot de passe
    username = input("Nom d'utilisateur : ")
    password = getpass.getpass("Mot de passe : ")
    hashed_password = hash_password(password)

    passwords = load_passwords()
    passwords[username] = hashed_password

    save_passwords(passwords)
    print("Mot de passe ajouté avec succès!")

def display_passwords():
    # Affiche les noms d'utilisateur et les mots de passe hachés
    passwords = load_passwords()
    if passwords:
        print("Mots de passe enregistrés :")
        for username, hashed_password in passwords.items():
            print(f"Nom d'utilisateur: {username}, Mot de passe haché: {hashed_password}")
    else:
        print("Aucun mot de passe enregistré.")

if __name__ == "__main__":
    while True:
        print("Que désirez vous faire ?")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")

        choice = input("Choisissez une option (1, 2 ou 3) : ")

        if choice == '1':
            add_password()
        elif choice == '2':
            display_passwords()
        elif choice == '3':
            print("Programme terminé.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")
