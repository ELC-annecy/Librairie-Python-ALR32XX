"""
    ************************************************************************
    *  fichier  : ALR32XX.py                                               *
    *  Fonction : Classe principale                                        *
    *  Produit  : ALR32XX                                                  *
    *  Device   :                                                          *
    *                                                                      *
    *  Copyright     : ELC, tous droits reservés                           *
    *  Auteur        : JY MOUBA                                            *
    *  Date creation : 01 aout 2021                                        *
    *  Version MAJ   : 01                                                  *
    *                                                                      *
    *  Historique :                                                        *
    *                                                                      *
    *  Version     Date       Auteur         Objet                         *
    *  ------------------------------------------------------------------- *
    *    1.0    22/09/2021    Y.M     Édition originale                    *
    ************************************************************************
"""

#importation des bibliothèques
import sqlite3
import sys

#Commande pour permettre à python de lire le contenu de la libraiire ALR32XX.
sys.path.insert(0, "C:\\Users\\stagiaire2\\Desktop\\GitHub\\Librairie-Python-ALR32XX") #Lieu où se trouve la libririre ALR32XX

#Importation de la bibliothèque ALR32XX
from ALR32XX import*

#Création de la base de données
i=1
try:
    conn = sqlite3.connect('MyBase.db')
    cur = conn.cursor()
    create_table = "CREATE TABLE Tableaux (id integer primary key autoincrement, valeur_tension float, valeur_temps float)"
    print("Connected to MyBase...")
    print(" ")
    cur.execute(create_table)
    conn.commit()
    print("MyBase table created...")
    print(" ")
    cur.close()
        
except sqlite3.Error as error:
    print("Error while connecting to MyBase: ", error)
    print(" ")
    
finally:
    if  conn:
        #Remplir la base de donnée
        nbre_valeur=int(input("Choisir le nombre de valeur que vous voulez insérer dans MyBase: "))
        print(" ")
        while i <= nbre_valeur:
            valeur_tension=input("Valeur de tension: ")
            valeur_temps=input("Temps nécessaire: ")
            try:
                conn=sqlite3.connect('MyBase.db')
                cur=conn.cursor()
                insert_into_table="insert into Tableaux( valeur_tension, valeur_temps) values (?, ?)"
                data_tuple=(valeur_tension, valeur_temps)
                cur.execute(insert_into_table, data_tuple)
                conn.commit()
                print("O.K :D")
                print(" ")
                cur.close()
            except sqlite3.Error as error:
                print("Failed to insert Python variable into MyBase table", error)
            i=i+1

        #Ecrire dans la base de donnée

