import sqlite3
import json
from sqlite3 import Error




class DB_Processor():
    def __init__(self):
        # Connexion à la base de données SQLite - XAVIER
        connexion_sqlite = sqlite3.connect('Clients_Users.sqlite')
        self.connexion = connexion_sqlite
        self.curseur = self.connexion.cursor()
        self.create_table_user()
        #self.insert_user('JoDonut','John', 'Doe', 'mot_de_passe_de_john')
        #self.insert_user('Mister_KK','KK', 'pipi', 'mot_de_passe_de_KK')
    
    # Fonction pour créer la table Utilisateurs - XAVIER    
    def create_table_user(self):
        try:
            self.curseur.execute('''
            CREATE TABLE IF NOT EXISTS Utilisateurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                nom TEXT,
                prenom TEXT,
                mot_de_passe TEXT
            )
        ''')
            self.connexion.commit()
            print("Table Utilisateurs créée avec succès.")
        except Error as e:
            print(e)
            
    # Fonction pour insérer un nouvel utilisateur - XAVIER
    def insert_user(self,username, nom_utilisateur, prenom_utilisateur, mot_de_passe):
        try:
            self.curseur.execute('''
                INSERT INTO Utilisateurs (username, nom, prenom, mot_de_passe) VALUES (?,?, ?, ?)
            ''', (username,nom_utilisateur, prenom_utilisateur, mot_de_passe))
            self.connexion.commit()
            print(f"Utilisateur {prenom_utilisateur} {nom_utilisateur} : @{username} inséré avec succès.")
        except Error as e:
            print(e)
            
    #Fonction pour chercher et afficher tous les utilisateurs dans la base de données - HENINTSOA        
    def fetch_users(self):
        try:
            self.curseur.execute('SELECT * FROM Utilisateurs')
            users = self.curseur.fetchall()
            
            if len(users) >0:
                print("All users : ")
                for user in users:
                    print(f"Username : {user[1]} - Nom : {user[2]} - Prenom : {user[3]} - MDP : {user[4]}")
            else:
                print("No users found")
        except Error as e:
            print(e)

    def fetch_user(self, username):
        try:
            self.curseur.execute('SELECT * FROM Utilisateurs WHERE username = ?',(username))
            user = self.curseur.fetchone()
            
            if user:
                print("user found: ")
                print(f"Username : {user[1]} - Nom : {user[2]} - Prenom : {user[3]} - MDP : {user[4]}")
            else:
                print("No users found")
        except Error as e:
            print(e)


    
    
class User():
    def __init__(self,username, db_Processor: DB_Processor):
        db_Processor.curseur.execute("SELECT * FROM Utilisateurs WHERE username = ?",(username,))
        user = db_Processor.curseur.fetchone
        self.username = username
        self.nom = user[2]
        self.prenom = user[3]
        self.mdp = user[4]
        


db_user = DB_Processor()
db_user.fetch_users()
db_user.connexion.commit()
db_user.connexion.close()