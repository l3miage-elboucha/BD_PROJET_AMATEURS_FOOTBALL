from utils import db
from prettytable import PrettyTable
import time

def select_tous_les_clubs(conn):
    """
    Affiche la liste de tous les clubs.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Clubs")
    liste=[]
    rows = cur.fetchall()
    mytable=PrettyTable(["Nom_Club", "Date_creation","Nombre_de_trophées","Manager"])
    for row in rows:
        a,b,c,d=row
        liste.append([a,b,c,d])
    for x in liste:
        mytable.add_row(x)
    print(mytable)

def select_tous_les_trophees(conn):
    

    """
    Affiche la liste de tous les trophees.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Trophees")
    liste = []

    rows = cur.fetchall()
    mytable=PrettyTable(["Nom_Trophée", "Prix en Million d'Euros","Type_trophée"])
    for row in rows:
        a,b,c = row
        liste.append([a,b,c])
    for x in liste:
        mytable.add_row(x)
    print(mytable)
        
def select_tous_les_managers(conn):
    """
    Affiche la liste de tous les managers.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Managers")
    liste = []

    rows = cur.fetchall()
    mytable=PrettyTable(["Nom_manager", "Prénom_manager","Salaire mensuel en Euros"])
    for row in rows:
        a,b,c = row
        liste.append([a,b,c])
    for x in liste:
        mytable.add_row(x)
    print(mytable)

def select_tous_les_joueurs(conn):
    """
    Affiche la liste de tous les joueurs.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Joueurs")
    liste = []

    rows = cur.fetchall()
    mytable=PrettyTable(["Numero Joueur", "Nom Club", "Nom Joueur", "Prenom Joueur", "Salaire Joueur"])
    for row in rows:
        a,b,c,d,e = row
        liste.append([a,b,c,d,e])
    for x in liste:
        mytable.add_row(x)
    print(mytable)

def select_tous_les_trophees_gagnes(conn):
    """
    Affiche la liste de tous les trophees gagnes.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Gagnes")
    liste = []

    rows = cur.fetchall()
    mytable=PrettyTable(["Nom Joueur", "Prenom Joueur", "Nom trophee", "Date Gagne"])
    for row in rows:
        a,b,c,d = row
        liste.append([a,b,c,d])
    for x in liste:
        mytable.add_row(x)
    print(mytable)    
    
def ajout_joueur(conn):
    cur = conn.cursor()
    print("\nCONTRAINTES: Veuillez entrez un couple (num_joueur, nom_club) n'existant pas dejà\n")
    c = input("\Entrez le nom du club: ")
    SEL = "SELECT numero_joueur FROM Joueurs WHERE nom_club = \"" + c + "\""
    print("\les numéros deja existants: \n")
    cur.execute(SEL)
    row = cur.fetchall()
    print(row)
    n = input("\nEntrez le numéro du joueur : ")
    no = input("\nEntrez le nom du joueur: ")
    p = input("\nEntrez le prénom du joueur: ")
    s = input("\nEntrez le salaire du joueur: ")
    DEL = "INSERT INTO Joueurs VALUES (" + n + "," + "\"" + c + "\"," + "\"" + no + "\"," + "\"" + p + "\","  + s + ")"
    cur.execute(DEL)
    print("\nJoueur bien ajouté ☻ !\n")
    time.sleep(2)
    
def suppression_joueur(conn):
    cur = conn.cursor()
    SEL = "SELECT nom_joueur,prenom_joueur FROM Gagnes"
    cur.execute(SEL)
    row = cur.fetchall()
    SEL = "SELECT nom_joueur,prenom_joueur FROM Joueurs"
    cur.execute(SEL)
    row2 = cur.fetchall()
    mytable=PrettyTable(["Nom Joueur", "Prenom Joueur"])
    liste = []
    for rows in row2:
        a,b = rows
        liste.append([a,b])
    for x in liste:
        mytable.add_row(x)
    print("\nLa liste des joueurs qui existent\n")
    time.sleep(1)
    print(mytable)
    no = input("\nEntrez le nom du joueur: ")
    p = input("\nEntrez le prénom du joueur: ")
    if (no,p) in row:
        cur.execute("DELETE FROM Gagnes WHERE nom_joueur =\""+no+"\" AND prenom_joueur =\"" + p + "\"")
    DEL = "DELETE FROM Joueurs WHERE nom_joueur = \"" + no + "\" AND prenom_joueur = \"" + p + "\""
    cur.execute(DEL)
    print("\nJoueur bien supprimé ☻ !\n")
    time.sleep(2)

def main():
    # Nom de la BD à créer
    db_file = "PROJET.db"
    
    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)
    zwaq = "    __________  ____  __________  ___    __    __ \n   / ____/ __ \/ __ \/_  __/ __ )/   |  / /   / / \n  / /_  / / / / / / / / / / __  / /| | / /   / /  \n / __/ / /_/ / /_/ / / / / /_/ / ___ |/ /___/ /___\n/_/    \____/\____/ /_/ /_____/_/  |_/_____/_____/\n"
    for i in zwaq:
        print(i,end="")
        time.sleep(0.0001)
    time.sleep(2)
    # Remplir la BD
    print("\n\n\n1. On crée la bd et on l'initialise avec des premières valeurs\n\n")
    db.mise_a_jour_bd(conn, "Creation_tables.sql")
    db.mise_a_jour_bd(conn, "Insertion_managers.sql")
    db.mise_a_jour_bd(conn, "Insertion_clubs.sql")
    db.mise_a_jour_bd(conn, "Insertion_joueurs.sql")
    db.mise_a_jour_bd(conn, "Insertion_trophees.sql")
    db.mise_a_jour_bd(conn, "Insertion_Gagne.sql")
    
    time.sleep(1)
    print("Entrez J pour afficher les joueurs\n")
    time.sleep(0.5)
    print("Entrez C pour afficher les clubs\n")
    time.sleep(0.5)
    print("Entrez T pour afficher les trophees\n")
    time.sleep(0.5)
    print("Entrez M pour afficher les managers\n")
    time.sleep(0.5)
    print("Entrez G pour afficher les trophees gagnes\n")
    time.sleep(0.5)
    print("Entrez D pour supprimer des joueurs\n")
    time.sleep(0.5)
    print("Entrez A pour ajouter des joueurs\n")
    time.sleep(0.5)
    print("Entrez Q pour quitter\n")
    time.sleep(0.5)
    a = input("Tapez votre choix:  \n")
    while a != 'Q':
        while a not in "JCTMGDA":
            print("Entrez J pour afficher les joueurs\n")
            print("Entrez C pour afficher les clubs\n")
            print("Entrez T pour afficher les trophees\n")
            print("Entrez M pour afficher les managers\n")
            print("Entrez G pour afficher les trophees gagnes\n")
            print("Entrez D pour supprimer des joueurs\n")
            print("Entrez A pour ajouter des joueurs\n")
            print("Entrez Q pour quitter\n")
            a = input("\Tapez un choix correct:  \n")
        if a == "C":
            print("\nListe de tous les clubs\n")
            select_tous_les_clubs(conn)
            time.sleep(5)
        if a == "M":
            print("\nListe de tous les managers\n")
            select_tous_les_managers(conn)
            time.sleep(5)
        if a == "T":
            print("\nListe de tous les trophées\n")
            select_tous_les_trophees(conn)
            time.sleep(5)
        if a == "J":
            print("\nListe de tous les joueurs\n")
            select_tous_les_joueurs(conn)
            time.sleep(5)
        if a == "G":
            print("\nListe de tous les trophees gagnes")
            select_tous_les_trophees_gagnes(conn)
            time.sleep(5)
        if a == "A":
            print("\nAjout d'un joueur\n")
            ajout_joueur(conn)
        if a == "D":
            print("\nSuppression d'un joueur\n")
            suppression_joueur(conn)
        print("Entrez J pour afficher les joueurs\n")
        print("Entrez C pour afficher les clubs\n")
        print("Entrez T pour afficher les trophees\n")
        print("Entrez M pour afficher les managers\n")
        print("Entrez G pour afficher les trophees gagnes\n")
        print("Entrez D pour supprimer des joueurs\n")
        print("Entrez A pour ajouter des joueurs\n")
        print("Entrez Q pour quitter\n")
        a = input("\nTapez votre choix:  \n")
                
                



def quitter(tab, menu):
    if tab == 'Q':
        menu = 88
    else:
        menu += 1
    

