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
    *    1.0    21/09/2021    Y.M     Édition originale                    *
    ************************************************************************
"""

"""
    - numpy: package fondamental pour le calcul scientifique en Python. 
    Il s'agit d'une bibliothèque Python qui fournit un objet tableau multidimensionnel, 
    divers objets dérivés (tels que des tableaux et des matrices masqués) et un assortiment 
    de routines pour des opérations rapides sur des tableaux, notamment mathématiques, logiques, 
    manipulation de forme, tri, sélection, E/S , transformées de Fourier discrètes, algèbre linéaire de base, 
    opérations statistiques de base, simulation aléatoire et bien plus encore.
    lien=https://numpy.org/doc/stable/user/whatisnumpy.html

    - matplotlib: c'est une librairie qui permet de tracer des graphes
    lien=https://matplotlib.org/ 
"""

#Importation des bibliothèques
import time
import sys
import math
import matplotlib.pyplot as plt
import ALR32XX.Library_ALR32XX as ALR


#Définition des varibales
alim=ALR.ALR32XX('ALR3203')
X=[ ]
Y1=[ ]
Y2=[ ]

print(" ")
print("Envoie des valeurs ... ")
for i in range (0,  360):
    X.append(i)
    #On envoie le sinus
    temp=math.sin(i*3.14/180)
    temp_=(temp*16)+16
    alim.Ecrire_tension(temp_)
    Y1.append(temp)
    #On récupère le courant
    valeur=alim.Mesure_courant()
    Y2.append(valeur)

#On affiche le signal courant et la tension
plt.plot(X, Y1,"b:o", label="tension U")
plt.plot(X, Y2, label="courant I")
plt.title("Fonction sinus")
plt.xlabel("t(s)")
plt.ylabel("f(t)")
plt.legend()
plt.show()
        
