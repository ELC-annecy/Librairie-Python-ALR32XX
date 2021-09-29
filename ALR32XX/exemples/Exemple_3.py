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
import time
import ALR32XX.Library_ALR32XX as ALR

#Liste des variables
alim=ALR.ALR32XX('ALR3203')
i=1
j=1
tension=0
temps=0


#Création de la base de données
try:
    print(" ")
    conn = sqlite3.connect('MyBase.db')
    cur = conn.cursor()
    create_table = "CREATE TABLE Tableaux (id integer primary key autoincrement, valeur_tension float, valeur_temps float)"
    print("Création de MyBase.db ... ")
    print(" ")
    cur.execute(create_table)
    conn.commit()
    print("Yes MyBase.db est créée :D ")
    print(" ")
    cur.close()
    
except sqlite3.OperationalError:
    print("Oups !!! MyBase.db existe déjà :') ")
    print(" ")
    
finally:
    if  conn:
        #supprimer tous les éléments de la base de donnée
        supp="DELETE FROM Tableaux"
        cur=conn.cursor()
        cur.execute(supp)
        conn.commit()

        #Ecrire dans la base de donnée
        nbre_valeur=int(input("Choisir le nombre de valeur que vous voulez insérer dans MyBase= "))
        print(" ")
        while i <= nbre_valeur:
            valeur_tension=input("Valeur de tension= ")
            valeur_temps=input("Temps d'utilisation= ")
            try:
                conn=sqlite3.connect('MyBase.db')
                cur=conn.cursor()
                insert_into_Tableaux="INSERT INTO Tableaux (valeur_tension, valeur_temps) values (?, ?)"
                data_tuple=(valeur_tension, valeur_temps)
                cur.execute(insert_into_Tableaux, data_tuple)
                conn.commit()
                print("O.K :)")
                print(" ")
                cur.close()
                
            except sqlite3.Error as error:
                print(" Failed :(", error)
            i=i+1

        #Mettre à jour les informations de la base de données
        choix=input("Voulez-vous mettre à jour les valeur_temps et valeur_tension ? OUI/NON : ")
        print(" ")
        if choix=='OUI':
            nbre_chgment=int(input("Combien de changement voulez vous faire dans MyBase= "))
            print(" ")
            while j <= nbre_chgment:
                chgment_indice=input("Choix de l'indice= ")
                chgment_tension=input("Nouvelle valeur de tension= ")
                chgment_temps=input("Nouveau temps d'utilisation= ")
                try:
                    conn=sqlite3.connect('MyBase.db')
                    cur=conn.cursor()
                    changement="UPDATE Tableaux SET valeur_tension= ?, valeur_temps=? WHERE ID=? "
                    modif=(chgment_tension, chgment_temps, chgment_indice)
                    cur.execute(changement, modif)
                    conn.commit()
                    print(" ")
                    
                except sqlite3.Error as error:
                    print(" Echec :", error)
                    print(" ")
                j=j+1
                
        elif choix=='NON':
            print("Pas de changement !!!")
            print(" ")

        #Récupérer les informations de la base de données
        try:
            conn=sqlite3.connect('MyBase.db')
            cur=conn.cursor()
            recovers_from_Tableaux="SELECT * FROM Tableaux"
            cur.execute(recovers_from_Tableaux)
            lignes=cur.fetchall()
            while 1:
                for ligne in lignes:
                    tension=ligne[1]
                    temps=ligne[2]
                    #print("tension=", tension, "et temps=", temps)
                    alim.Ecrire_tension(tension)
                    time.sleep(temps)

        except sqlite3.Error as error:
            print("Echec : ", error) 
        
