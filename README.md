# Librairie-Python-ALR32XX

Documentation complète de la librairie : https://elc-construction-electronique.gitbook.io/librairie-python-alr32xx/


<p div="Description"> 
Librairie <a href="https://www.python.org/downloads/" title="Lien d téléchargement Python"> Python</a> pour piloter les alimentations programmables <strong>ALR3220, ALR3203, ALR3206D/T</strong> par une liaison série (USB, RS232, RS485). 
</p>



<h2>Installation du module</h2>

Le module ALR32XX necessite d'avoir installé Python et la librairie PySerial : <a href="https://pythonhosted.org/pyserial/pyserial.html">pip install pyserial</a>. La procédure d'installation est detaillée dans le gitbook à la page <a href="https://elc-construction-electronique.gitbook.io/librairie-python-alr32xx/utilisation-de-la-librairie-python/installation-de-la-librairie">Installation de la librairie</a>.


<h2>Utilisation du module</h2>







Formatage de votre README
Les fichiers README suivent généralement un format afin d'orienter immédiatement les développeurs vers les aspects les plus importants de votre projet.

Nom du projet : le nom de votre projet est la première chose que les gens verront en faisant défiler le fichier README, et il est inclus lors de la création de votre fichier README.

Description : Une description de votre projet suit. Une bonne description est claire, courte et précise. Décrivez l'importance de votre projet et ce qu'il fait.

Table des matières : En option, incluez une table des matières afin de permettre aux autres personnes de naviguer rapidement dans les README particulièrement longs ou détaillés.

Installation : L'installation est la section suivante d'un README efficace. Indiquez aux autres utilisateurs comment installer votre projet localement. En option, incluez un gif pour rendre le processus encore plus clair pour les autres personnes.

Utilisation : La section suivante est l'utilisation, dans laquelle vous indiquez aux autres personnes comment utiliser votre projet après l'avoir installé. C'est également un bon endroit pour inclure des captures d'écran de votre projet en action.

Contribution : Les projets plus importants ont souvent des sections sur la contribution à leur projet, dans lesquelles les instructions de contribution sont décrites. Parfois, il s'agit d'un fichier séparé. Si vous avez des préférences spécifiques en matière de contribution, expliquez-les afin que les autres développeurs sachent comment contribuer au mieux à votre travail. Pour en savoir plus sur la façon d'aider les autres à contribuer, consultez le guide sur la définition de directives pour les contributeurs de référentiel.

Crédits : Incluez une section pour les crédits afin de mettre en évidence et de lier les auteurs de votre projet.

Licence : Enfin, incluez une section pour la licence de votre projet. Pour plus d'informations sur le choix d'une licence, consultez le guide de licence de GitHub !
Votre fichier README ne doit contenir que les informations nécessaires aux développeurs pour commencer à utiliser votre projet et à y contribuer. Une documentation plus longue est mieux adaptée aux wikis, comme indiqué ci-dessous.















<body>
	<div>
		<p> <h3> <span class ="colored"> Texte introductif </h3></p>
		<p> Cette librairie en python a été réalisé pour permettre aux utilisateurs des alimentations ELC de piloter à distance <strong> les alimentations programmables ALR3203, ALR3220, ALR3206D et ALR3206T </strong>. Pourquoi avoir choisi python ? Tout simplement parce qu'il s'agit d'un langage open source et du langage le plus apprécié des developpeurs. Python est disponible et téléchargeable <strong> <a href="https://www.python.org/downloads/" title="Lien vers le téléchargement de Python"> ICI </a> </strong>. 
		</p>
		<p></p>
	</div>
	<div class="flexslider">
		<ul class="slides">
		<li><img src="https://github.com/ELC-annecy/Librairie-Python-ALR32XX/blob/main/Images/ALR3203.jpg" alt="ALR3203" width="150" height="200" /></li>
    		<li><img src="https://github.com/ELC-annecy/Librairie-Python-ALR32XX/blob/main/Images/ALR3220.jpg" alt="ALR3220" width="150" height="200" /></li>
    		<li><img src="https://github.com/ELC-annecy/Librairie-Python-ALR32XX/blob/main/Images/ALR3206D.jpg" alt="ALR3206D" width="150" height="200" /></li>
    		<li><img src="https://github.com/ELC-annecy/Librairie-Python-ALR32XX/blob/main/Images/ALR3206T.jpg" alt="ALR3206T" width="150" height="200" /></li>
    		</ul>
	</div>
	<div>
		<p> <h3> <span class ="colorblue"> Caractéristiques des alimentations </h3></p>
		<table>
			<tr>
				<th> ALR3206T </th>
				<th> ALR3206D </th>
				<th> ALR3220 </th>
				<th> ALR3203 </th>
			</tr>
			<tr>
				<td>
					<ul>
						<li> Alimentation 3 voies</li>
						<li>Puissance 400W max </li>
						<li>Tension 0-32V / courant 0-6A sur les voies 1 et 2 </li>
						<li>Tension 0-15V / courant 0-3A / puissance 15W sur la voie 3 </li>
						<li>Mode série (0-64V/0-6A) et mode parallèle (0-32V/0-12V) pour
les voies 1 et 2 </li>
						<li>Résolutions 10mV et 2mA sur les voies 1 et 2 </li>
						<li>Résolutions 10mV et 10mA sur la voie 3 </li>
						<li>Communication USB et RS485. Option RSETHER : adaptateur
ETHERNET </li>
						<li>Protection contre les courts-circuits, les échauffements
excessifs et les surintensités à l’entrée du secteur </li>
						<li> OVP/OCP pour éviter les surtensions et surintensités</li>
						<li>Rendement > 80% à puissance maximale </li>
						<li>Température de fonctionnement : +5 à +40°C </li>
						<li>Fonction en U et I (arbitraire, carré, rampe montante et
descendante, temps de montée et descente) </li>
						<li>Drivers et exécutable LabVIEW fournis </li>
						<li>Consommation 495W maxi </li>>
					</ul>
				</td>
				<td>
					<ul>
						<li> Alimentation 2 voies</li>
						<li>Puissance 385W max </li>
						<li>Tension 0-32V / courant 0-6A sur les voies 1 et 2 </li>
						<li>Mode série (0-64V/0-6A) et mode parallèle (0-32V/0-12V) </li>
						<li> Résolutions 10mV et 2mA sur les voies 1 et 2 </li>
						<li>Communication USB, RS232, RS485 et RS422 vers ETHERNET </li>
						<li> Protection contre les courts-circuits, les échauffements excessifs et les surintensités à l’entrée du secteur</li>
						<li>OVP/OCP pour éviter les surtensions et surintensités </li>
						<li>Rendement > 78% à puissance maximale </li>
						<li> Température de fonctionnement : +5 à +40°C</li>
						<li> Fonction en U et I (arbitraire, carré, rampe montante et
descendante, temps de montée et descente)</li>
						<li>Drivers et exécutable LabVIEW fournis </li>
						<li>Consommation 490W maxi </li>
					</ul>
				</td>
				<td>
					<ul>
						<li>Alimentation 1 voie </li>
						<li>Puissance 640W max</li>
						<li>Tension 0-32V / courant 0-20A </li>
						<li> Résolutions 10mV et 10mA</li>
						<li>Communication USB, RS232, RS485, (option LAN), 0-10V </li>
						<li>Protection contre les courts-circuits, les échauffements excessifs et les surintensités à l’entrée du secteur </li>
						<li> OVP/OCP pour éviter les surtensions et surintensités</li>
						<li> Rendement > 84% à puissance maximale</li>
						<li>Température de fonctionnement : +5 à +40°C </li>
						<li>Fonction en U et I (arbitraire, carré, rampe montante et descendante, temps de montée et descente) </li>
						<li>Drivers et exécutable LabVIEW fournis </li>
						<li>Consommation 770W maxi </li>
					</ul>
				</td>
				</td>
				<td>
					<ul>
						<li> Alimentation 1 voie </li>
						<li> Puissance 96W max </li>
						<li> Tension 0-32V / courant 0-6A </li>
						<li> Résolutions 10mV et 2mA </li>
						<li> Communication USB </li>
						<li> Protection contre les courts-circuits, les échauffements excessifs et les surintensités à l’entrée du secteur </li>
						<li> OVP/OCP pour éviter les surtensions et surintensités </li>
						<li> Rendement > 78% à puissance maximale </li>
						<li> Fonction en U et I (arbitraire, carré, rampe montante et descendante périodique, temps de montée/descente monocoup) </li>
						<li> Drivers et exécutable LabVIEW fournis </li>
						<li> Température de fonctionnement : +5 à +40°C </li>
						<li> Consommation 126W maxi </li>
						<li> Drivers et exécutable LabVIEW fournis </li>
					</ul>
				</td>			
			</tr>
		</table>
	<p></p>
	<p> <h3> <span class ="colorgreen"> Liste des fonctions </h3></p>
	<p>Pour utiliser la bibliothèque de fonctions, il faut installer le module <a href="https://pypi.org/project/pyserial/"> PySerial </a>. C'est lui qui permet d'établir la communication entre les alimentations et le PC. Voici la liste des fonctions de la bibliothèque <a href="https://github.com/ELC-annecy/Librairie-Python-ALR32XX/blob/main/ALR32XX.py"> ALR32XX </a>.
	</p>
	<ul>
		<li> __init__(self, c_nom=’ ‘) </li>
		<li>List_port (self)  </li>
		<li>Choix_port (self)  </li>
		<li> Deconnexion (self) </li>
		<li> IDN (self) </li>
		<li> Read_state_ALR (self, c_parametre=’OUT’)  </li>
		<li> OUT(self, c_mode=’ ‘, c_out=1) </li>
		<li> ALR (self, c_mode=’NORMAL‘) </li>
		<li> Remote(self, c_mode=’REMOTE’) </li>
		<li> STO(self, c_case_memory=1) </li>
		<li> RCL(self, c_case_memory=1) </li>
		<li> TRACK(self, c_mode=’ISOLE’) </li>
		<li> Mesure_tension(self, c_voie=1) </li>
		<li> Consigne_tension (self, c_voie=1) </li>
		<li> Mesure_courant (self, c_voie=1) </li>
		<li> Consigne_courant (self, c_voie=1) </li>
		<li> Ecrire_courant(self, c_valeur=0, c_voie=1) </li>
		<li> Ecrire_tension(self, c_valeur=0, c_voie=1)</li>
		<li> OCP(self, c_valeur=0, c_voie=1) </li>
		<li> OVP(self, c_valeur=0, c_voie=1)</li>
		<li> OVP_OCP(self, c_parametre='OVP', c_voie=1)</li>
	</ul>
	</div>
	<div>
		<p> <h3> <span class ="colorpink"> Exemples </h3></p>
		<p> Voici quelques exemples d'utlisation de la librairie </p>
		<p> <strong> <a href="https://github.com/ELC-annecy/Librairie-Python-ALR32XX/blob/main/Exemples/Exemple_1.py" title="Exemple 1"> Exemple 1 </a> </strong></p>
		<p> <strong> <a href="https://github.com/elc-construction-electronique/Librairie-Python-ALR32XX/blob/main/Exemples/Exemple_2.py" title="Exemple 2"> Exemple 2 </a> </strong></p>
		<p> <strong> <a href="https://github.com/elc-construction-electronique/Librairie-Python-ALR32XX/blob/main/Exemples/Exemple_3.py" title="Exemple 3"> Exemple 3 </a> </strong></p>
		<p> ... </p>
	</div>
	<div>
		<p> <h3> Crédits </h3> </p>
		<ul>
			<li> Alex MIOLLANY </li>
			<li> John-Yvan MOUBA </li>
		</ul>
	</div>
</body>
