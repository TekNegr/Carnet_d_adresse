import tkinter as tk
from tkinter import ttk

def afficher_details(contact):
    details_label.config(text=f"Nom: {contact}\nNuméro de téléphone: 123-456-7890\nEmail: {contact.lower()}@exemple.com")

def changer_photo():
    photo_label.config(text="Nouvelle photo de profil")

fenetre = tk.Tk()
#fenetre.geometry("800x500")
fenetre.title("Carnet d'adresses")


background_color = "#C7D4D5"  # Couleur gris clair pour l'arrière-plan
fenetre.configure(bg=background_color)

# Barre latérale des contacts avec cadre bleu clair
contacts_frame = tk.Frame(fenetre, bg="#74E1EE", width=200)  # Couleur bleu clair pour la barre latérale
contacts_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")  

contacts_list = ["Contact 1", "Contact 2", "Contact 3", "Contact 4"]

for contact in contacts_list:
    contact_button = tk.Button(contacts_frame, text=contact, command=lambda c=contact: afficher_details(c), height=3, width=20, bg="#2980b9", fg="white")  # Couleur bleu foncé pour les boutons de contact
    contact_button.pack(fill=tk.Y, pady=5)  

# Zone centrale pour la photo de profil avec cadre vert clair
photo_frame = tk.Frame(fenetre, bg="#BFFFC3")  
photo_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")  

# Utilisation d'un canevas pour représenter le carré vide
photo_canvas = tk.Canvas(photo_frame, width=150, height=150, bg="white", borderwidth=2, relief="solid")
photo_canvas.pack()

changer_photo_button = tk.Button(photo_frame, text="Changer la photo", command=changer_photo, bg="#27ae60", fg="white")  # Couleur verte foncée pour le bouton
changer_photo_button.pack(pady=5)

# Zone inférieure pour les détails du contact avec cadre rose clair
details_frame = tk.Frame(fenetre, bg="#e74c3c")  
details_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew", padx=10)  

details_label = tk.Label(details_frame, text="", bg="#e74c3c", fg="white")  
details_label.pack()

# Configuration de la gestion de la grille pour centrer les colonnes et les lignes
fenetre.grid_columnconfigure(0, weight=0)  
fenetre.grid_columnconfigure(1, weight=1)
fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_rowconfigure(1, weight=1)

fenetre.mainloop()