"""
    ************************************************************************
    *  fichier  : ALR32XX.py                                               *
    *  Fonction : Classe principale                                        *
    *  Produit  : ALR32XX                                                  *
    *  Device   :                                                          *
    *                                                                      *
    *  Copyright     : ELC, tous droits reservés                           *
    *  Auteur        : JY MOUBA                                            *
    *  Date creation : 16 septembre 2021                                        *
    *  Version MAJ   : 01                                                  *
    *                                                                      *
    *  Historique :                                                        *
    *                                                                      *
    *  Version     Date       Auteur         Objet                         *
    *  ------------------------------------------------------------------- *
    *    1.0    16/09/2021    Y.M     Édition originale                    *
    ************************************************************************
"""



#Importation des bibliothèques
from ALR32XX import*

#Importation de la classe plus choix de l'appareil
X=ALR32XX('ALR3206T')

#Réglage des OVP
X.OVP(32, 1)
time.sleep(1)
X.OVP(22, 2)
time.sleep(1)
X.OVP(12, 3)
time.sleep(1)

#Ecriture de quelques valeur de tension
X.Ecrire_tension(30, 1)
time.sleep(1)
X.Ecrire_tension(10.5, 2)
time.sleep(1)
X.Ecrire_tension(3.4, 3)
time.sleep(1)

#Lecture des valeurs de tension
val1=X.Mesure_tension(1)
print(val1)
time.sleep(1)
val2=X.Mesure_tension(2)
print(val2)
time.sleep(1)

#Utilisaation d'autres fonctions de la librairie
val3=X.IDN()
time.sleep(1)
print(val3)
X.ALR('PARALLELE')
time.sleep(1)
val4=X.Read_state_ALR ('MODE')
if '2' in val4 :
    print("On est bien en mode parallèle")
else:
    print("On est dans unautre mode")
