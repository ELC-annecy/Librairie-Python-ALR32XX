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
    *    1.2.1  08/10/2021    A.M     Correction et mise en ligne          *
    *    1.3    30/06/2022    A.M     Ajout de la fonciton send_command    *
    *    1.3.1  15/02/2023    N.L     Correction Bug connection manuelle   *
    *                                 Traduction en anglais des messages   *
    ************************************************************************
"""


# Importation of libraries
import time
from serial import*
from io import*
import serial.tools.list_ports



class ALR32XX:

    """ Python library to drive the ALR3220, ALR3203, ALR3206D/T programmable power supplies via a serial link (USB, RS232, RS485). """


    global alim
    alim=serial.Serial()
    
    
    def __init__(self, c_nom=' '): # Initializes the ALR32XX class by choosing the device name.
        print("Connection to the power supply ...")
        print("")
        self.nom=c_nom
        self.port=self. __Connect_auto_toPort(self.nom)
        #self.port=self. __Connect_manuel_toPort()
        try :
            print("Port = "+self.port)
            print("Nom = "+ self.nom)
            print("Connection = OK") 
        except:
            print("ERROR: Alimentation not found")
        
     
            
    def __param (self, c_parametre=' ', c_valeur=0): # Allows you to choose between different possible parameters
        # volt=1000*millivolt
        valeur=str(c_valeur)
        liste=['VOLT', 'CURR', 'OVP', 'OCP', 'OUT', 'VOLT1', 'CURR1', 'OVP1', 'OCP1', 'OUT1', 
        'VOLT2', 'CURR2', 'OVP2', 'OCP2', 'OUT2', 'VOLT3', 'CURR3', 'OVP3', 'OUT3', 'IDN', 'RCL', 'STO', 'REM', 'TRACK', 'MODE']
        for i in liste:
            if c_parametre in liste:
                return (c_parametre, valeur)
            else:
                return("There is no such parameter in the list")


    def __command (self, c_parametre=' ', c_X=' ', c_nombre=0): # This function allows us to create our command string  
        X=c_X
        nombre=c_nombre
        parametre=c_parametre
        if X=='WR': # Valid for all parameters except CURR3
            if parametre!='CURR3':
                # Write the necessary instruction
                #print("Writing operation")
                param,value=self.__param(parametre,nombre)
                chaine='0 '+param+' '+X+' '+str(value)+'\r'
                return (chaine)
            else:
                return ("Unable to perform this operation")
        elif X=='RD': # Valid for all parameters except : RCL, STO
            if parametre!='RCL' or parametre!='STO':
                # Write the necessary instruction
                #print("Reading operation")
                param, value=self.__param(parametre,0)
                chaine='0 '+param+' '+X+'\r'
                return (chaine)
            else:
                return ("Unable to perform this operation")
        elif X=='MES': # Valid only for parameters VOLT & CURR
            if parametre=='VOLT' or parametre=='CURR' or parametre=='VOLT1' or parametre=='VOLT2' or parametre=='CURR1' or parametre=='CURR2' or parametre=='CURR3':
                # Write the necessary instruction
                param, value=self.__param(parametre,0)
                chaine='0 '+param+' '+X+'\r'
                return (chaine)
            else:
                return ("Unable to perform this operation")
        else:
            return (print("Unknown operation"))


    def __write_command_toByte (self, parametre=' ', commande=' ', valeur=0): # This function converts our string into an array of bytes
        # Definition of the chain to be sent
        chaine=self.__command (str(parametre), str(commande), str(valeur))
        reponse=bytearray(chaine.encode('ASCII'))
        return (reponse)


    def __Connect_auto_toPort(self, c_name=' '):# This function automatically connects to the power supply port during the initialization phase of the instance
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


    def __Connect_manuel_toPort(self): # This function allows you to manually connect to the power port during the initialization phase of the instance
        # Manual Connection
        ports = serial.tools.list_ports.comports(include_links=False) # Command to search for ports
        ligne = 1
        len_ports = len(ports)
        if len_ports != 0:  # At least one active port has been found.
            for q in ports:
                print(str(ligne)+" : "+str(q))
                ligne=ligne+1
            print ("")

            portChoisi=int(input("Choose among the different ports found : "))

            if(portChoisi < 1 or portChoisi > len_ports):
                raise Exception("Index out of range")
            
            # The communication is established
            psu_device = str(ports[portChoisi-1].device)
            try:
                alim.__init__((psu_device), baudrate=9600 , bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=float(1))
                if alim.isOpen()==True:
                    return (psu_device)
            except IOError: # If the port is already open, then it is closed and reopened
                alim.close()
                alim.open()
                return (psu_device)
                    

    def __send (self, c_command): # This function establishes the connection with the computer and the ALR32XX and sends the commands  
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


    def send_command(self,commande):
        reponse=bytearray(commande.encode('ASCII'))
        reponse=self.__send(reponse)
        return reponse


    def List_ports (self): # This function lists the different ports present on the Computer
        ports = serial.tools.list_ports.comports(include_links=False) # Command to search for ports
        if len (ports) != 0:  # At least one active port has been found.
            for p in ports:
                print(p)
        else: # No active port was found
            print ("No active port was found")


    def Choix_port (self): # This function allows you to manually connect to the power supply port and returns the selected port
        # Manual Connection
        ports = serial.tools.list_ports.comports(include_links=False) # Command to search for ports
        ligne=1
        if len (ports) != 0:  # At least one active port has been found.
            for p in ports:
                print(str(ligne)+" : " + str(p))
                ligne=ligne+1
            print ("")
            
            portChoisi=int(input("Choose among the different ports found : "))

            if(portChoisi < 1 or portChoisi > len_ports):
                raise Exception("Index out of range")

            # The communication is established
            psu_device = str(ports[portChoisi-1].device)
            try:
                alim.__init__((psu_device), baudrate=9600 , bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=float(1))
                if alim.isOpen()==True:
                    print ("Connexion O.K")
                    return (psu_device)
            except IOError: # If the port is already open, then it is closed and reopened
                alim.close()
                alim.open()
                print ("Connexion O.K")
                return (psu_device)
           
        else: # No active port was found
            print ("No active port was found")
                                     

    def Deconnexion (self):# Switches the power supply to local mode and then disables the port
        chaine=self.__write_command_toByte('REM', 'WR', 0)
        self.__send(chaine)
        alim.close()
        print('Port is OFF')


    def IDN (self): # Returns the IDN of the power supply
        chaine=self.__write_command_toByte('IDN', 'RD')
        reponse=self.__send(chaine)
        if self.nom in reponse:
            return (str(reponse[5:len(reponse)]))
        else :
            print(reponse)


    def Read_state_ALR (self, c_parametre='OUT'): # Allows you to read the OUT, REM, TRACK, MODE status of the power supplies
        parametre=c_parametre
        liste1= ['REM','OUT'] 
        liste2= ['REM', 'TRACK', 'MODE','OUT']
        liste3=['REM', 'TRACK', 'MODE','OUT']
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


    def OUT (self, c_etat=0, c_out=1): # Choose the output status ( "ON" or "OFF")
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


    def MODE(self, c_mode): # Choose between "SERIES", "PARALLEL" and "TRACKING" mode of power supplies
        mode=c_mode
        if mode=='NORMAL'or mode==0:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                print("Operation not possible on ALR3203 and ALR3220")
            elif self.nom=='ALR3206D' or self.nom=='ALR3206T':
                chaine=self.__write_command_toByte('MODE', 'WR', 0)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
        elif mode=='SERIE'or mode==1:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                print("Operation not possible on ALR3203 and ALR3220")
            elif self.nom=='ALR3206D' or self.nom=='ALR3206T':
                chaine=self.__write_command_toByte('MODE', 'WR', 1)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
        elif mode=='PARALLELE'or mode==2:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                print("Operation not possible on ALR3203 and ALR3220")
            elif self.nom=='ALR3206D' or self.nom=='ALR3206T':
                chaine=self.__write_command_toByte('MODE', 'WR', 2)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
        elif mode=='TRACKING' or mode==3:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                print("Operation not possible on ALR3203 and ALR3220")
            elif self.nom=='ALR3206D' or self.nom=='ALR3206T':
                chaine=self.__write_command_toByte('MODE', 'WR', 3)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
        else :
            print("Unrecognised mode")


    def Remote(self, c_mode): # Choice between "REMOTE" and "LOCAL" mode
        mode=c_mode
        if mode=='REMOTE'or mode==1:
            chaine=self.__write_command_toByte('REM', 'WR', 1)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))
        elif mode=='LOCAL'or mode==0:
            chaine=self.__write_command_toByte('REM', 'WR', 0)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))


    def STO(self, c_case_memory=1): # Saves the configuration (1 to 15)
        case_memory=int(c_case_memory)
        if case_memory >=1 and case_memory <= 15:
            chaine=self.__write_command_toByte('STO', 'WR', case_memory)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))
        else:
            case_memory=input("Choose a memory cell between 1 and 15")
            chaine=self.__write_command_toByte('STO', 'WR', case_memory)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))


    def RCL(self, c_case_memory=1): # Recalls the saved configuration (1 to 15)

        case_memory=int(c_case_memory)
        if case_memory >=1 and case_memory <= 15:
            chaine=self.__write_command_toByte('RCL', 'WR', case_memory)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))
        else:
            case_memory=input("Choose a memory cell between 1 and 15")
            chaine=self.__write_command_toByte('RCL', 'WR', case_memory)
            reponse=self.__send(chaine)
            return (str(reponse[2:len(reponse)]))


    def TRACK(self, c_mode): # Enables the Isolated Tracking or Liked Tracking mode
        mode=c_mode
        if self.nom=='ALR3206D' or self.nom=='ALR3206T':
            self.MODE('TRACKING')
            if mode=='ISOLE'or mode==0:
                chaine=self.__write_command_toByte('TRACK', 'WR', 0)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
            elif mode=='COUPLE' or mode==1 :
                chaine=self.__write_command_toByte('TRACK', 'WR', 1)
                reponse=self.__send(chaine)
                return (str(reponse[2:len(reponse)]))
        else :
            print("Operation not possible on ALR3203 and ALR3220")


    def Mesure_tension(self, c_voie=1): # Used to measure the voltage on one of the power supply channels.
        voie=c_voie
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("Power supply has a single channel")
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
                print("Power supply has just two channels")
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
                print("Voltage measurement not possible on CH3")
        

    def Consigne_tension(self, c_voie=1): # Used to read the voltage setpoint on one of the power supply channels.
        voie=c_voie
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT', 'RD')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("Power supply has a single channel")
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
                print("Power supply has just two channels")
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


    def Mesure_courant(self, c_voie=1): # Used to measure the current on one of the power supply channels.
        voie=c_voie
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('CURR', 'MES')
                reponse=self.__send(chaine)
                return (float(reponse[5:len(reponse)])/1000)
            else :
                print("Power supply has a single channel")
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
                print("Power supply has just two channels")
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
                print("Power supply has a single channel")
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
                print("Power supply has just two channels")
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
                print("There is no current setpoint on CH3")


    def Ecrire_tension(self, c_valeur=0, c_voie=1): # Used to send a voltage value to the power supply
        temp=float(c_valeur)*1000
        voie=c_voie
        valeur=temp
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('VOLT', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            else :
                print("Power supply has a single channel")
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
                print("Power supply has just two channels")
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


    def Ecrire_courant(self, c_valeur=0, c_voie=1): # Used to send a current value to the power supply
        temp=float(c_valeur)*1000
        voie=c_voie
        valeur=temp
        if self.nom=='ALR3203' or self.nom=='ALR3220':
            if voie==1:
                chaine=self.__write_command_toByte('CURR', 'WR', valeur)
                reponse=self.__send(chaine)
                return (reponse[2:len(reponse)])
            else :
                print("Power supply has a single channel")
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
                print("Power supply has just two channels")
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
                print("There is no current setpoint on CH3")
    

    def OVP(self, c_valeur=0, c_voie=1): # Used to set the voltage limitation on one channel of the power supply
        temp=float(c_valeur)*1000
        voie=c_voie
        valeur=temp
        if valeur >=0 and valeur<=32200:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                if voie==1:
                    chaine=self.__write_command_toByte('OVP', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                else :
                    print("Power supply has a single channel")
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
                    print("Power supply has just two channels")
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
                        

    def OCP(self, c_valeur=0, c_voie=1): # Used to set the current limitation on one channel of the power supply
       temp=float(c_valeur)*1000
       voie=c_voie
       valeur=temp
       if valeur >=0 and valeur<=6100:
            if self.nom=='ALR3203' or self.nom=='ALR3220':
                if voie==1:
                    chaine=self.__write_command_toByte('OCP', 'WR', valeur)
                    reponse=self.__send(chaine)
                    return (reponse[2:len(reponse)])
                else :
                    print("Power supply has a single channel")
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
                    print("Power supply has just two channels")
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
                    print("There is no OCP on CH3")


    def OVP_OCP(self, c_parametre='OVP', c_voie=1): #Used to read the value of OVP and OCP.
            voie=c_voie
            parametre=c_parametre
            if parametre=='OVP':
                if self.nom=='ALR3203' or self.nom=='ALR3220':
                    if voie==1:
                        chaine=self.__write_command_toByte('OVP', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    else :
                        print("Power supply has a single channel")
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
                        print("Power supply has just two channels")
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
                        print("There is no OVP on CH3")
            elif parametre=='OCP':
                if self.nom=='ALR3203' or self.nom=='ALR3220':
                    if voie==1:
                        chaine=self.__write_command_toByte('OCP', 'RD')
                        reponse=self.__send(chaine)
                        return (float(reponse[5:len(reponse)])/1000)
                    else :
                        print("Power supply has a single channel")
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
                        print("Power supply has just two channels")
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
                        print("There is no OCP on CH3")


#main programme here
