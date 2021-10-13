# Librairie-Python-ALR32XX

<h3> <a href="#EN"> English version bellow</a> </h3>

<br/>
Documentation complète de la librairie : https://elc-construction-electronique.gitbook.io/librairie-python-alr32xx/ <br/>
Complete documentation of the library : https://elc-construction-electronique.gitbook.io/alr32xx-python-library-documentation-en/ <br/>
<br/>
<p id="FR"> 
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
Une fois l'installation terminée vous pouvez acceder à la bibliothèque par "from ALR32XX import *" (si vous installez par pip, "from ALR32XX.ALR32XX import *"). </br>
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



</br>
</br></br>
</br></br>
</br></br>
</br></br>
</br></br>
</br></br>
</br>











<h1 id="EN">English version</h1>
</br>
Complete documentation of the library : https://elc-construction-electronique.gitbook.io/alr32xx-python-library-documentation-en/<br/><br/>
<p> 
	<a href="https://www.python.org/downloads/" target="_blank" title="Python download link" > Python</a> library to drive the <strong>ALR3220, ALR3203, ALR3206D/T</strong> programmable power supplies via a serial link (USB, RS232, RS485). 


<h2>Module installation</h2>

The ALR32XX module requires Python and the PySerial library to be installed: <a href="https://pythonhosted.org/pyserial/pyserial.html" target="_blank">pip install pyserial</a>. The installation procedure is detailed in the gitbook at <a href="https://elc-construction-electronique.gitbook.io/alr32xx-python-library-documentation-en/utilisation-de-la-librairie-python/installation-de-la-librairie" target="_blank">Installing the library</a>.


The installation of the ALR32XX library is done in two ways: 
<ul>
	<li>Using the code in a project: 
		Download the .zip via the <a href="https://github.com/elc-construction-electronique/Librairie-Python-ALR32XX">github repository</a>. In this folder you will find the ALR32XX.py source code, a folder with usage examples and a folder with the library and power supplies documentations. 
	<li>Downloading the library via Pip:
		Our ALR32XX library can be accessed via <a href="https://pypi.org/project/ALR32XX/">PyPI</a>, making it downloadable via the command "pip install ALR32XX". </br>You can find information and the version of the library via the command "pip show ALR32XX" and, if needed, update it via "pip install ALR32XX --upgrade".</br> 
		<img src="Documentation/Images/install_cmd.PNG" alt="Installing the library by command line">

</ul> 
	
<h2>Using the module</h2>
<p>
Once the installation is finished you can access the library by "from ALR32XX import *". (if you install by pip, "from ALR32XX.ALR32XX import *"). </br>
Connect the power supply to the computer via USB, RS232 or RS485. You can check the connection in the device manager and on the power supply screen:</br>.
<img src=Documentation/Images/gest_periph.PNG alt="Checking the power connection">
</br>
The program works in the form of a class, it is necessary to declare an object which will correspond to the power supply. For example for an ALR3203, the declaration would be "name=ALR32XX('ALR3203')". The program will then try to automatically establish a communication with the power supply and return Port=COM3; Name=ALR3203; Connection=OK. </br>
If the attempt fails, you will be asked to connect the power supply manually via the Choix_port() function. This function will list your active ports and ask you to enter the number of the one to connect:</br>
<img src=Documentation/Images/connect_manuel.PNG alt="Manually connect to power">
</br>
Once the connection is successful, you can use the library. For example X.Mesure_tension() to measure the voltage of your ALR3203. A list of available functions is given in the <a href="https://github.com/elc-construction-electronique/Librairie-Python-ALR32XX/tree/main/Documentation">documentation</a> and on the <a href="https://elc-construction-electronique.gitbook.io/alr32xx-python-library-documentation-en/utilisation-de-la-librairie-python/installation-de-la-librairie">Gitbook</a>
</p>


<h2>Contact</h2>
If you have any problems using the library, please contact us at <a href="mailto: commercial@elc.fr">commercial@elc.fr</a> or +33 4 50 57 30 46.  </br>
</br>

<img src="Documentation/Images/ALR32XX.png" alt="Programmable power supply range">
