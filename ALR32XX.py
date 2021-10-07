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
    *    1.0    08/09/2021    Y.M     Édition originale                    *
    ************************************************************************
"""


#Importation des bibliothèques
import time
from serial import*
from io import*
import serial.tools.list_ports



class ALR32XX:

    """ Librairie Python pour piloter les alimentations programmables ALR3220, ALR3203, ALR3206D/T par une liaison série (USB, RS232, RS485). """


    global alim
    alim=serial.Serial()
    
    
    def __init__(self, c_nom=' '): #Initialise la classe ALR32XX en choisissant le nom de l'appareil.
        print("Connexion à l'alimentation ...")
        print(" ")
        self.nom=c_nom
        self.port=self. __Connect_auto_toPort(self.nom)
        #self.port=self. __Connect_manuel_toPort()
        try :
            print("Port="+self.port)
            print("Nom="+ self.nom)
            print("Connexion=OK") 
        except:
            print("ERROR: Alimentation non trouvée")
        
     
            
    def __param (self, c_parametre=' ', c_valeur=0): #Permet de chosir parmi les différents paramètres possibles
        #volt=1000*millivolt
        valeur=str(c_valeur)
        liste=['VOLT', 'CURR', 'OVP', 'OCP', 'OUT', 'VOLT1', 'CURR1', 'OVP1', 'OCP1', 'OUT1', 
        'VOLT2', 'CURR2', 'OVP2', 'OCP2', 'OUT2', 'VOLT3', 'CURR3', 'OVP3', 'OUT3', 'IDN', 'RCL', 'STO', 'REM', 'TRACK', 'MODE']
        for i in liste:
            if c_parametre in liste:
                return (c_parametre, valeur)
            else:
                return("Il n'y a pas ce paramètre dans la liste")


    def __command (self, c_parametre=' ', c_X=' ', c_nombre=0): #Cette fonction nous permet de créer notre chaine de commande 
        X=c_X
        nombre=c_nombre
        parametre=c_parametre
        if X=='WR': #Valable pour tous les paramètres sauf CURR3
            if parametre!='CURR3':
                # Ecrire l'instruction nécessaire
                #print("Opération d'écriture")
                param,value=self.__param(parametre,nombre)
                chaine='0 '+param+' '+X+' '+str(value)+'\r'
                return (chaine)
            else:
                return ("Impossible d'effectuer cette operation")
        elif X=='RD': #Valide pour tous paramètres, sauf : RCL, STO
            if parametre!='RCL' or parametre!='STO':
                # Ecrire l'instruction nécessaire
                #print("Opération de lecture")
                param, value=self.__param(parametre,0)
                chaine='0 '+param+' '+X+'\r'
                return (chaine)
            else:
                return ("Impossible d'effectuer cette operation")
        elif X=='MES': #Valide uniquement pour paramètres VOLT & CURR
            if parametre=='VOLT' or parametre=='CURR' or parametre=='VOLT1' or parametre=='VOLT2' or parametre=='CURR1' or parametre=='CURR2' or parametre=='CURR3':
                # Ecrire l'instruction nécessaire
                param, value=self.__param(parametre,0)
                chaine='0 '+param+' '+X+'\r'
                return (chaine)
            else:
                return ("Impossible d'effectuer cette operation")
        else:
            return (print("Opération inconnue"))


    def __write_command_toByte (self, parametre=' ', commande=' ', valeur=0): #Cette fonction convertie notre chaine tableau de bytes 
        #Définition de la chaine à envoyé
        chaine=self.__command (str(parametre), str(commande), str(valeur))
        reponse=bytearray(chaine.encode('ASCII'))
        return (reponse)


    def __Connect_auto_toPort(self, c_name=' '):#Cette fonction permet de se connecter automatiquement au port de l'alimentation lors de la phase d'initialisation de la bibliothèque
        name=c_name
        ports=serial.tools.list_ports.comports(include_links=False)
        if len(ports)!=0:
            for p in ports:
                try:
                    alim.__init__(str(p.device), baudrate=9600 , bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=float(1))
                    if alim.isOpen()==True:
                        chaine=self.__write_command_toByte (parametre='IDN', commande='RD', valeur=0)
                        alim.write(chaine)
                        reponse=str(alim.read_until(b'\r'))
                        if name in reponse:
                            return (str(p.device))
                        else :
                            alim.close()
                except :
                    alim.close()


    def __Connect_manuel_toPort(self): #Cette fonction permet de se connecter manuellement au port de l'alimentation lors de la phase d'initialisation de la bibliothèque
        # Connexion Manuelle
        ports = serial.tools.list_ports.comports(include_links=False) #commande pour rechercher les ports
        ligne_=1
        if len (ports) != 0:  #On a trouvé au moins un port actif. La fonction "len()" renvoie le nombre des éléments (ou la longueur) dans un objet.
            for q in ports:
                print(str(ligne_)+" : " + str(q))
                ligne_=ligne_+1
            print (" ")
            _portChoisi=input("Chosir parmi les différents ports trouvés : ")
            #On établie la communication
            try:
                alim.__init__(str(ports[int(_portChoisi)-1].device), baudrate=9600 , bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=float(1))
                if alim.isOpen()==True:
                    return (str(q.device))
            except IOError: #Si le port est déja ouvert, alors fermeture puis ouverture
                alim.close()
                alim.open()
                return (str(q.device))
                    

    def __send (self, c_command): #Cette fonction établie la connexion avce le PC et l'ALR32XX puis envoie les commandes 
        command=c_command
        if alim.isOpen()==True:
            alim.write(command)
        else:
            alim.close()
            alim.open()
            alim.write(command)
        _bytes_lus=alim.read_until(b'\r')
        alim.close()
        return (str(_bytes_lus.decode('ASCII')))


    def List_ports (self): #cette fonction établie la liste des différents ports présents dans le PC
        ports = serial.tools.list_ports.comports(include_links=False) #commande pour rechercher les ports
        if len (ports) != 0:  #On a trouvé au moins un port actif. La fonction "len()" renvoie le nombre des éléments (ou la longueur) dans un objet.
            for p in ports:
                print(p)
        else: #On n'a pas trouvé de port actif
            print ("Aucun port actif n'a été trouvé")


    def Choix_port (self): #Cette fonction permet de se connecter manuellement au port de l'alimentation et retourne le port choisi
        # Connexion Manuelle
        ports = serial.tools.list_ports.comports(include_links=False) #commande pour rechercher les ports
        ligne=1
        if len (ports) != 0:  #On a trouvé au moins un port actif. La fonction "len()" renvoie le nombre des éléments (ou la longueur) dans un objet.
            for p in ports:
                print(str(ligne)+" : " + str(p))
                ligne=ligne+1
            print (" ")
            _portChoisi=input("Chosir parmi les différents ports trouvés : ")
            #On établie la communication
            try:
                alim.__init__(str(ports[int(_portChoisi)-1].device), baudrate=9600 , bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=float(1))
                if alim.isOpen()==True:
                    print ("Connexion O.K")
                    portChoisi=ports[int(_portChoisi)-1].device
                    return (str(portChoisi))
            except IOError: # Si le port est déja ouvert, alors fermeture puis ouverture
                alim.close()
                alim.open()
                print ("Connexion O.K")
                portChoisi=ports[int(_portChoisi)-1].device
                return (str(portChoisi))
        else: #On n'a pas trouvé de port actif
            print ("Aucun port actif n'a été trouvé")
                                     

    def Deconnexion (self):#Passe l'alimentation en local puis désactive le port
        chaine=self.__write_command_toByte('REM', 'WR', 0)
        self.__send(chaine)
        alim.close()
        print('Port is OFF')


    def IDN (self): #Renvoit l'IDN de l'alimentation
        chaine=self.__write_command_toByte('IDN', 'RD')
        print(chaine)
        reponse=self.__send(chaine)
        if self.nom in reponse:
            return (str(reponse[5:len(reponse)]))
        else :
            print(reponse)


    def Read_state_ALR (self, c_parametre='OUT'): #Permet de lire l'etat des modes OUT, REM, TRACK, MODE des alimentations 
        parametre=c_parametre
        liste1= ['REM'] 
        liste2= ['REM', 'TRACK', 'MODE']
        liste3=['REM', 'TRACK', 'MODE']
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            for i in liste1:
                if parametre in liste1:
                    chaine=self.__write_command_toByte(parametre, 'RD')
                    reponse=self.__send(chaine)
                    return(str(reponse[2:len(reponse)]))
        elif self.nom=='ALR3206D':
            for j in liste2:
                if parametre in liste2:
                    chaine=self.__write_command_toByte(parametre, 'RD')
                    reponse=self.__send(chaine)
                    return(str(reponse[2:len(reponse)]))
        elif self.nom=='ALR3206T':
            for k in liste3:
                if parametre in liste3:
                    chaine=self.__write_command_toByte(parametre, 'RD')
                    reponse=self.__send(chaine)
                    return(str(reponse[2:len(reponse)]))


    def OUT (self, c_etat, c_out=1): #Choisir l'état de la sortie ( "ON" ou "OFF")
        out=c_out
        etat=c_etat
        if etat=='ON' or etat==1:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                if out==1:
                    chaine=self.__write_command_toByte('OUT', 'WR', 1)
                    reponse=self.__send(chaine)
                    return (str(reponse[2:len(reponse)]))
                else :
                    print("L'alimentation possède une seule voie")
            elif self.nom=='ALR3206D':
                if out==1:
                    chaine=self.__write_command_toByte('OUT1', 'WR', 1)
                    reponse=self.__send(chaine)
                    return (str(reponse[2:len(reponse)]))
                elif out==2:
                    chaine=self.__write_command_toByte('OUT2', 'WR', 1)
                    reponse=self.__send(chaine)
                    return (str(reponse[2:len(reponse)]))
                else :
                    print("L'alimentation possède uniquement 2 voies")
            elif self.nom=='ALR3206T':
                if out==1:
                    chaine=self.__write_command_toByte('OUT1', 'WR', 1)
                    reponse=self.__send(chaine)
                    return (str(reponse[2:len(reponse)]))
                elif out==2:
                    chaine=self.__write_command_toByte('OUT2', 'WR', 1)
                    reponse=self.__send(chaine)
                    return (str(reponse[2:len(reponse)]))
                elif out==3:
                    chaine=self.__write_command_toByte('OUT3', 'WR', 1)
                    reponse=self.__send(chaine)
                    return (str(reponse[2:len(reponse)]))
                
        elif etat=='OFF' or etat==0:
                if self.nom=='ALR3203' or self.nom=='ALR3220':
                    if out==1:
                        chaine=self.__write_command_toByte('OUT', 'WR', 0)
                        reponse=self.__send(chaine)
                        return (str(reponse[2:len(reponse)]))
                    else :
                        print("L'alimentation possède une seule voie")
                elif self.nom=='ALR3206D':
                    if out==1:
                        chaine=self.__write_command_toByte('OUT1', 'WR', 0)
                        reponse=self.__send(chaine)
                        return (str(reponse[2:len(reponse)]))
                    elif out==2:
                        chaine=self.__write_command_toByte('OUT2', 'WR', 0)
                        reponse=self.__send(chaine)
                        return (str(reponse[2:len(reponse)]))
                    else :
                        print("L'alimentation possède uniquement 2 voies")
                elif self.nom=='ALR3206T':
                    if  out==1:
                        chaine=self.__write_command_toByte('OUT1', 'WR', 0)
                        reponse=self.__send(chaine)
                        return (str(reponse[2:len(reponse)]))
                    elif out==2:
                        chaine=self.__write_command_toByte('OUT2', 'WR', 0)
                        reponse=self.__send(chaine)
                        return (str(reponse[2:len(reponse)]))
                    elif out==3:
                        chaine=self.__write_command_toByte('OUT3', 'WR', 0)
                        reponse=self.__send(chaine)
                        return (str(reponse[2:len(reponse)]))


    def MODE(self, c_mode): #Choisir entre le mode "SERIE", "PARALLELE" et "TRACKING" des alimentations 
        mode=c_mode
        if mode=='NORMAL'or mode==0:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                print("Opération impossible sur l'ALR3203 et l'ALR3220")
            elif self.nom=='ALR3206D' or self.nom=='ALR3206T':
                chaine=self.__write_command_toByte('MODE', 'WR', 0)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
        elif mode=='SERIE'or mode==1:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                print("Opération impossible sur l'ALR3203 et l'ALR3220")
            elif self.nom=='ALR3206D' or self.nom=='ALR3206T':
                chaine=self.__write_command_toByte('MODE', 'WR', 1)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
        elif mode=='PARALLELE'or mode==2:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                print("Opération impossible sur l'ALR3203 et l'ALR3220")
            elif self.nom=='ALR3206D' or self.nom=='ALR3206T':
                chaine=self.__write_command_toByte('MODE', 'WR', 2)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
        elif mode=='TRACKING' or mode==3:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                print("Opération impossible sur l'ALR3203 et l'ALR3220")
            elif self.nom=='ALR3206D' or self.nom=='ALR3206T':
                chaine=self.__write_command_toByte('MODE', 'WR', 3)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
        else :
            print("Mode non reconnu")


    def Remote(self, c_mode): #Choix entre mode "REMOTE" et mode "LOCAL"
        mode=c_mode
        if mode=='REMOTE'or mode==1:
            chaine=self.__write_command_toByte('REM', 'WR', 1)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))
        elif mode=='LOCAL'or mode==0:
            chaine=self.__write_command_toByte('REM', 'WR', 0)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))


    def STO(self, c_case_memory=1): #Permet de sauvegarder la configuration (1 à 15)
        case_memory=c_case_memory
        if case_memory >=1 and case_memory <= 15:
            chaine=self.__write_command_toByte('STO', 'WR', case_memory)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))
        else:
            case_memory=input("Choisir une case mémoire entre 1 et 15")
            chaine=self.__write_command_toByte('STO', 'WR', case_memory)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))


    def RCL(self, c_case_memory=1): #Permet de rappeler la configuration enregistrée (1 à 15)

        case_memory=c_case_memory
        if case_memory >=1 and case_memory <= 15:
            chaine=self.__write_command_toByte('RCL', 'WR', case_memory)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))
        else:
            case_memory=input("Choisir une case memoire entre 1 et 15")
            chaine=self.__write_command_toByte('STO', 'WR', case_memory)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))


    def TRACK(self, c_mode): #Permet d’activer le mode Tracking isolé ou Tracking
        mode=c_mode
        if self.nom=='ALR3206D' or self.nom=='ALR3206T':
            self.ALR('TRACKING')
            if mode=='ISOLE'or mode==0:
                chaine=self.__write_command_toByte('TRACK', 'WR', 0)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
            elif mode=='COUPLE' or mode==1 :
                chaine=self.__write_command_toByte('TRACK', 'WR', 1)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
        else :
            print("Opération impossible sur l'ALR3203 et l'ALR3220")


    def Mesure_tension(self, c_voie=1): #Permet de mesurer la tension sur une des voies de l’alimentation.
        voie=c_voie
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("L'alimentation possède une seule voie")
        elif self.nom=='ALR3206D':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT1', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==2:
                chaine=self.__write_command_toByte('VOLT2', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("L'alimentation possède uniquement 2 voies")
        elif self.nom=='ALR3206T':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT1', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==2:
                chaine=self.__write_command_toByte('VOLT2', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==3:
                print("Mesure en tension impossible sur CH3")
        

    def Consigne_tension(self, c_voie=1): #Permet de lire la consigne en tension sur une des voies de l’alimentation.
        voie=c_voie
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("L'alimentation possède une seule voie")
        elif self.nom=='ALR3206D':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT1', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==2:
                chaine=self.__write_command_toByte('VOLT2', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("L'alimentation possède uniquement 2 voies")
        elif self.nom=='ALR3206T':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT1', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==2:
                chaine=self.__write_command_toByte('VOLT2', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==3:
                chaine=self.__write_command_toByte('VOLT3', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)


    def Mesure_courant(self, c_voie=1): #Permet de mesurer le courant sur une des voies de l’alimentation 
        voie=c_voie
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('CURR', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("L'alimentation possède une seule voie")
        elif self.nom=='ALR3206D':
            if voie==1:
                chaine=self.__write_command_toByte('CURR1', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==2:
                chaine=self.__write_command_toByte('CURR2', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("L'alimentation possède uniquement 2 voies")
        elif self.nom=='ALR3206T':
            if voie==1:
                chaine=self.__write_command_toByte('CURR1', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==2:
                chaine=self.__write_command_toByte('CURR2', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==3:
                chaine=self.__write_command_toByte('CURR3', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
                

    def Consigne_courant(self, c_voie=1): #Permet de lire la consigne en courant sur une des voies de l’alimentation.
        voie=c_voie
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('CURR', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("L'alimentation possède une seule voie")
        elif self.nom=='ALR3206D':
            if voie==1:
                chaine=self.__write_command_toByte('CURR1', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==2:
                chaine=self.__write_command_toByte('CURR2', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("L'alimentation possède uniquement 2 voies")
        elif self.nom=='ALR3206T':
            if voie==1:
                chaine=self.__write_command_toByte('CURR1', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==2:
                chaine=self.__write_command_toByte('CURR2', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            elif voie==3:
                print("Il n'y a pas de consigne en courant sur CH3")


    def Ecrire_tension(self, c_valeur=0, c_voie=1): #Permet d’envoyer une valeur de tension à l’alimentation
        temp=float(c_valeur)*1000
        voie=c_voie
        valeur=temp
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            else :
                print("L'alimentation possède une seule voie")
        elif self.nom=='ALR3206D':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT1', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            elif voie==2:
                chaine=self.__write_command_toByte('VOLT2', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            else :
                print("L'alimentation possède uniquement 2 voies")
        elif self.nom=='ALR3206T':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT1', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            elif voie==2:
                chaine=self.__write_command_toByte('VOLT2', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            elif voie==3:
                chaine=self.__write_command_toByte('VOLT3', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])


    def Ecrire_courant(self, c_valeur=0, c_voie=1): #Permet d’envoyer une valeur de courant à l’alimentation
        temp=float(c_valeur)*1000
        voie=c_voie
        valeur=temp
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('CURR', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            else :
                print("L'alimentation possède une seule voie")
        elif self.nom=='ALR3206D':
            if voie==1:
                chaine=self.__write_command_toByte('CURR1', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            elif voie==2:
                chaine=self.__write_command_toByte('CURR2', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            else :
                print("L'alimentation possède uniquement 2 voies")
        elif self.nom=='ALR3206T':
            if voie==1:
                chaine=self.__write_command_toByte('CURR1', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            elif voie==2:
                chaine=self.__write_command_toByte('CURR2', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            elif voie==3:
                print("Il n'y a pas de consigne en courant sur CH3")
    

    def OVP(self, c_valeur=0, c_voie=1): #Permet de régler la limitation de tension sur une voie de l'alimentation
        temp=float(c_valeur)*1000
        voie=c_voie
        valeur=temp
        while valeur >=0 and valeur<=32200:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                if voie==1:
                    chaine=self.__write_command_toByte('OVP', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                else :
                    print("L'alimentation possède une seule voie")
            elif self.nom=='ALR3206D':
                if voie==1:
                    chaine=self.__write_command_toByte('OVP1', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                elif voie==2:
                    chaine=self.__write_command_toByte('OVP2', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                else :
                    print("L'alimentation possède uniquement 2 voies")
            elif self.nom=='ALR3206T':
                if voie==1:
                    chaine=self.__write_command_toByte('OVP1', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                elif voie==2:
                    chaine=self.__write_command_toByte('OVP2', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                elif voie==3:
                    chaine=self.__write_command_toByte('OVP3', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                        

    def OCP(self, c_valeur=0, c_voie=1): #Permet de régler la limitation de courant sur une voie de l'alimentation
       temp=float(c_valeur)*1000
       voie=c_voie
       valeur=temp
       while valeur >=0 and valeur<=6100:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                if voie==1:
                    chaine=self.__write_command_toByte('OCP', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                else :
                    print("L'alimentation possède une seule voie")
            elif self.nom=='ALR3206D':
                if voie==1:
                    chaine=self.__write_command_toByte('OCP1', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                elif voie==2:
                    chaine=self.__write_command_toByte('OCP2', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                else :
                    print("L'alimentation possède uniquement 2 voies")
            elif self.nom=='ALR3206T':
                if voie==1:
                    chaine=self.__write_command_toByte('OCP1', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                elif voie==2:
                    chaine=self.__write_command_toByte('OCP2', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                elif voie==3:
                    print("Il n'y a pas d'OCP sur CH3")


    def OVP_OCP(self, c_parametre='OVP', c_voie=1): #Permet de lire la valeur d’OVP et d’OCP.
            voie=c_voie
            parametre=c_parametre
            if parametre=='OVP':
                if self.nom=='ALR3203' or self.nom=='ALR3220':
                    if voie==1:
                        chaine=self.__write_command_toByte('OVP', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    else :
                        print("L'alimentation possède une seule voie")
                elif self.nom=='ALR3206D':
                    if voie==1:
                        chaine=self.__write_command_toByte('OVP1', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    elif voie==2:
                        chaine=self.__write_command_toByte('OVP2', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    else :
                        print("L'alimentation possède uniquement 2 voies")
                elif self.nom=='ALR3206T':
                    if voie==1:
                        chaine=self.__write_command_toByte('OVP1', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    elif voie==2:
                        chaine=self.__write_command_toByte('OVP2', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    elif voie==3:
                        print("Il n'y a pas d'OVP sur CH3")
            elif parametre=='OCP':
                if self.nom=='ALR3203' or self.nom=='ALR3220':
                    if voie==1:
                        chaine=self.__write_command_toByte('OCP', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    else :
                        print("L'alimentation possède une seule voie")
                elif self.nom=='ALR3206D':
                    if voie==1:
                        chaine=self.__write_command_toByte('OCP1', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    elif voie==2:
                        chaine=self.__write_command_toByte('OCP2', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    else :
                        print("L'alimentation possède uniquement 2 voies")
                elif self.nom=='ALR3206T':
                    if voie==1:
                        chaine=self.__write_command_toByte('OCP1', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    elif voie==2:
                        chaine=self.__write_command_toByte('OCP2', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    elif voie==3:
                        print("Il n'y a pas d'OCP sur CH3")


#main programme
