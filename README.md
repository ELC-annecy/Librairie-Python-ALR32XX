# Librairie-Python-ALR32XX

Documentation complète de la librairie : https://elc-construction-electronique.gitbook.io/librairie-python-alr32xx/


<p div="Description"> 
Librairie <a href="https://www.python.org/downloads/" target="_blank" title="Lien d téléchargement Python" > Python</a> pour piloter les alimentations programmables <strong>ALR3220, ALR3203, ALR3206D/T</strong> par une liaison série (USB, RS232, RS485). 
</p>



<h2>Installation du module</h2>

Le module ALR32XX necessite d'avoir installé Python et la librairie PySerial : <a href="https://pythonhosted.org/pyserial/pyserial.html" target="_blank">pip install pyserial</a>. La procédure d'installation est detaillée dans le gitbook à la page <a href="https://elc-construction-electronique.gitbook.io/librairie-python-alr32xx/utilisation-de-la-librairie-python/installation-de-la-librairie" target="_blank">Installation de la librairie</a>.

L'installation de la librairie ALR32XX se fait alors de deux façons : 
<ul>
	<li>Utilisation du code dans un projet : 
		Telechargez le .zip via le <a href="https://github.com/elc-construction-electronique/Librairie-Python-ALR32XX">repository github</a>. Dans ce dossier vous trouverez le code source ALR32XX.py, un dossier avec des exemples d'utilisation et un dossier avec les documentations de la librairie et des alimentations. 
	<li>Téléchargement de la librairie via Pip :
		Notre librairie ALR32XX est accessible via <a href="https://pypi.org/project/ALR32XX/">PyPI</a>, la rendant téléchargeable par la commande "pip install ALR32XX". </br>Vous pouvez trouver des renseignements et la version de la librairie par la commande "pip show ALR32XX" et, si besoin, la mettre à jour par "pip install ALR32XX --upgrade".</br> 
		<img src="Documentation/Images/install_cmd.PNG" alt="Installation de la librairie par ligne de commande">
</ul> 
	
<h2>Utilisation du module</h2>
<p>
Une fois l'installation terminée vous pouvez acceder à la bibliothèque par "from ALR32XX import *". </br>
Reliez l'alimentation à l'ordinateur par USB, RS232 ou RS485. Vous pouvez verifier la connexion dans le gestionnaire de périphérique et sur l'ecran de l'alimentation :</br>
<img src=Documentation/Images/gest_periph.PNG alt="Vérification de la conexion de l'alimentation">
</br>
Le programme fonctionne sous la forme d'une classe, il faut declarer un objet qui correspondra à l'alimentation. Par exemple pour une ALR3203, la declaration se fera par "nom=ALR32XX('ALR3203')". Le programme tente alors d'établir automatiquement une communication avec l'alimentation et renvoie Port=COM3; Nom=ALR3203; Connexion=OK. </br>
Si la tentative échoue, il vous sera demandé de connecter l'alimentation manuellement par la fonction Choix_port(). Cette fonction va lister vos ports actifs et vous demandera d'entrer le numéro de celui qu'il faut connecter :</br>
<img src=Documentation/Images/connect_manuel.PNG alt="Connexion manuelle à l'alimentation">
</br>
Une fois la connexion réussie, vous pouvez utiliser la librairie. Par exemple X.Mesure_tension() pour mesurer la tension de votre ALR3203. Une liste des fonctions disponibles est donnée dans la <a href="https://github.com/elc-construction-electronique/Librairie-Python-ALR32XX/tree/main/Documentation">documentation</a> et sur le  <a href="https://elc-construction-electronique.gitbook.io/librairie-python-alr32xx/utilisation-de-la-librairie-python/installation-de-la-librairie">Gitbook</a>
</p>


<h2>Contact</h2>
En cas de problème lors de l'utilisation de la librairie, veuillez nous contacter à <a href="mailto: commercial@elc.fr">commercial@elc.fr</a> ou au +33 4 50 57 30 46.  
</br>
</br>

<img src="Documentation/Images/ALR32XX.png" alt="Gamme d'alimentations programmables">
