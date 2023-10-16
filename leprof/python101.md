# Python 101 
## Les classes

### Structure

```
import xxx
class NomDeMaClass:
	variable_de_classes = "valeur"
	def __init__(self, var1, var2):
		self.variable_dinstance1 = var1
		self.variable_dinstance2 = var2
		
	def methode_chg_var1(self, nouvelle_val_var1):
		self.variable_dinstance1 = nouvelle_val_var1
		
	def methode_affiche_valeurs(self):
		print(f"valeur de ma variable de classe  {NomDeMaClass.variable_de_classe}")
		print(f"valeur d'instance : valeur1->{self.variable_dinstance1}, valeur2->{self.variable_dinstance2}")
```

### Les imports de librairies
Comme pour tout script Python, les imports de librairie se font au tout début.

### Le nom de classe
La norme veut que le nom de la classe débute toujours par une Majuscule, c'est un héritage du language Pascal.

### Variables de classe

Une variable de classe se fait entre la déclaration de la class et l'init `def **init**(self):`.
Ces variables sont des attributs qui ont une valeur par défaut commune de départ pour tous les objets créés par l'intermédiaire de cette classe.
Cette variable n'est pour autant pas une constante et peut être modifié pour une instance en particulier et il n'y a que l'instance modifiée qui aura cette nouvelle valeur. Ce changement ne sera pas propagé à travers les instances existantes ni celles à venir.

```
class Requin:
	type_animal = "poisson"
```
Ici la class Requin a une variable de classe type_animal qui est "poisson". 

Nous pouvons instancier la classe dans un objet que nous appellerons requin_blanc et afficherons sa variable en utilisant la notation du point(.).

```
class Requin:
	type_animal = "poisson"
	location = "ocean"
	
requin_blanc = Shark()
print(requin_blanc.type_animal)
print(requin_blanc.location)
```

Si l'on exécute ce programme:

`$ python requin.py`

==Output==  

`poisson`  
`ocean`


On peut également ajouter plusieurs de ces variables.
```
class Requin:
	type_animal = "poisson"
	location = "ocean"
	
requin_blanc = Shark()
print(requin_blanc.type_animal)
print(requin_blanc.location)
```

### Variables d'instance

Ces variables sont positionnées uniquement au moment de la création d'une instance.

Elles sont positionnées au niveau de l'exécution de la méthode d'init et leurs déclarations au niveau du constructeur de la classe `__init__`.

```
class Requin:
	type_animal = "poisson"
	location = "ocean"
	
	def __init__(self, nom, nombre_de_dents):
		self.name = nom
		self.number_of_teeth = nombre_de_dents

requin_blanc = Requin(nom="requin blanc", nombre_de_dents=700)

print(f"Le {requin_blanc.name} a {requin_blanc.number_of_teeth} dents et habite 
dans {Requin.location} et mange des sacs en plastics." )
```

==Output==  
`Le requin blanc a 700 dents et habite dans ocean et mange des sacs en plastics.`

### Fonction vs méthode

À la différence d'une méthode, une fonction n'a pas besoin d'être instanciée pour être appelé.

```
class Requin:
	type_animal = "poisson"
	location = "ocean"
	
	def __init__(self, nom, nombre_de_dents):
		self.name = nom
		self.number_of_teeth = nombre_de_dents
		
	def get_type()->str:
		return type_animal
		
	def get_nb_of_teeth(self)->int:
		return self.number_of_teeth
```

Exemple :  

```
In [37]: Requin.get_type()
Out[37]: 'poisson'

In [38]: Requin.get_nb_of_teeth()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[38], line 1
----> 1 Requin.get_nb_of_teeth()

TypeError: Requin.get_nb_of_teeth() missing 1 required positional argument: 'self'

In [39]: requin_blanc = Requin("requin blanc", 700)

In [40]: requin_blanc.get_nb_of_teeth()
Out[40]: 700
```

## IDE
Interface Development Environment 

Spider : https://www.spyder-ide.org  
PyCharm : https://www.jetbrains.com/pycharm/  
VSCode : https://code.visualstudio.com  

## Librairies
Une librairie est un ensemble de module, classes, fonctions qui propose une fonctionnalité particulière.

Il existe des librairies accessible de base appelée "core libraries" qui viennent d'office avec Python et les librairies externes qui doivent être elles installées.

### PIP
(Package Installer for Python)
Permet d'installer une librairie et ses dépendances.

`pip install pandas`

### requirements.txt

Lors d'un développement, il est recommandé de lister dans ce fichier les librairies nécessaires et requises.  
On peut ensuite installer ces librairies en indiquant cette liste à PIP. 

`pip install -r requirements.txt`  

C'est également un fichier qui peut être requis lors d'un déploiement.  

### Environnement virtuel : VENV

Pour cloisonner le développement et l'exécution de chaque programme / projet, il est conseiller d'utiliser des environnements virtuels.

Sans quoi, les librairies installées seront partagées pour tout le système. Ce qui complique les choses lorsque les programmes requièrent par exemple des versions différentes d'une même librairies.  

Création d'un environnement virtuel.  
Commande à exécuter idéalement à la racine de son projet.  
```python -m venv venvdemonprojet```

Il faut ensuite activer son environnement.

```. ./venvdemonprojet/bin/activate```
Notez qu'il y a bien un . suivit d'un espace avant la commande d'activation, c'est normal et nécessaire.

Une fois activé, le prompt de la ligne de commande doit changer et indiquer l'environnement virtuel actif.

`(venvdemonprojet) mbpsimon:leprof nomix$ `

En général les IDE gèrent à leur façon les environnements virtuels, il faut s'en référer à leur documentation.

## Identifiant unique

Il est fortement déconseillé d'utiliser un Integer pour un identifiant unique qui pourrait entre autre servir de clé primaire. C'est souvent à l'usage qu'on s'en rend compte. 

UUID est un algorithme qui génère une valeur unique à chaque fois qu'il est appelé.

Une version courte existe : *shortuuid*

## Validation de données

Il est conseillé d'avoir un processus de validation de ses données. On peut créer par exemple une méthode validation() qui vérifie que les valeurs soumises aux attributs de notre objet respectent les limites fonctionnelles qui ont été établies.

Un excellent article sur medium à ce sujet : https://levelup.gitconnected.com/validator-pattern-do-you-know-how-to-validate-your-data-properly-50edc5b3c6c6

Dans un premier temps, on peut se limiter à une procédure de validation définit au sein de sa classe. 
Cette méthode passe en revue chaque variable, évalue si la valeur proposé est dans les limites souhaitées sinon une exception est levé. 

exemple si l'âge d'un personne est en négatif ou au delà de 130 ans, on peut considérer cette valeur comme aberrante et lever une exception.

`raise ValueError("Age is not valid")`

## Gestion des exceptions

Python permet de gérer une exception en utilisant ce qui est appelé un bloque try/except.

Si le code s'attend à une possibilité d'exception, le code où pourrait se produire cette exception est mis dans ce type de bloque. En fonction du type d'exception, il est possible d'exécution un code spécifique pour traiter cette exception.

```
try:
	x = 1 / 0
except ZeroDivisionError:
  x = 1 / 2
print(x)
0.5
```

## Tests unitaires
Une bonne manière de tester son code tout en le développant est d'écrire les tests unitaires au fur et à mesure. Ces tests pourront évoluer avec le temps et à l'usage du ou des programmes utilisant ce code, mais il est bien d'avoir à la base ces tests qui auront pour avantage d'éviter un grand nombre de régression.  

### unitest

C'est une librairie de tests unitaires parmi tant d'autre mais dont l'usage est largement répandu.
Le principe est de dériver cette class, d'écrire des cas de tests pour valider les limites fonctionnelles et d'y ajouter des "asserts" (affirmations) qui viennent confirmer le résultat attendu. 

Par exemple, si l'on veut vérifier qu'une fonction qui réalise la division de deux nombres passés en argument.  
On souhaite vérifier que :
cas nominal :
- le résultat d'une division est juste
- l'arrondie est celui attendu
cas d'exceptions : 
- lorsque le dénominateur est zéro
- valeur extrême
- valeur non numérique

```
import unittest
class TestDivZero(unittest.TestCase):
	def TestNominal(self):
		r = 1/2
		self.assertEqual(r, 0.5, msg="La valeur de 1 / 2 n'est pas celle attendue : 0.5")

if __name__ == '__main__':
    unittest.main()
```

Il existe un certain nombre d'assert possible qui sont décrit dans la documentation de la librairie unittest : https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual

## Normalisation de chaînes de caractères

La normalisation de chaîne de caractères consiste à ramener à sa forme la plus simple cette dernière.

Comme le prédicat d'égalité en informatique est très ferme, il est considéré par exemple que "françois" et "francois" sont différent ou encore que "Canada" et "canada" le sont également.

Dans la réalité, le besoin de faire abstraction à ce type de différence peut être nécessaire. Notamment pour s'affranchir des erreurs ou des particularités propre à chaque individu dans sa façon d'écrire. 

La normalisation de chaîne de caractères peut simplifier à des degrés différents selon les besoins/usages.

- remplace les caractères accentués par des caractères non accentués;
- met tous les caractères à la même case;
- supprime ou non les chiffre;
- supprime tous les caractères non alphabétique (quid des langues étrangères);
- supprime les espaces;
- supprime les "stop words"

etc..

## Utilisation de lambda

Python est très friand des oneliner. Le code que l'on peut écrire en une seule ligne.

Lambda est ce qu'on appel communément une fonction anonyme qui s'affranchie de la structure classique d'une fonction et qui ne peut être appelé qu'a l'endroit où elle est décrite.

Une fonction classique :

```
def quarre(x):
	return x**2
quarre(2)
4
```

Peut être réalisé en une seule ligne

```
l = lambda x: x**2
l(2)
4
```

Très utiliser avec Pandas pour modifier une colonne ou pour en créer une nouvelle.

```
df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
df
   A  B
0  4  9
1  4  9
2  4  9
df.apply(lambda x: np.sqrt(x))
     A    B
0  2.0  3.0
1  2.0  3.0
2  2.0  3.0
```

## Externalisation des paramètres

Enregistrer certaines valeurs de paramètres liées à l'exécution de votre code peut devenir un problème lorsque qu'il sera livré en production. Car pour l'adapter, il faudra modifier le code. Tout environnement de production qui souhaite maintenir une stabilité dans la continuité de ses services à une règle qui dit que lorsqu'on modifie le code d'un programme, il faut tout retester pour éviter les régressions.
Pour éviter ce type de modification de code, les variables de configuration sont placées en dehors du code, dans un fichier de configuration ou une variable d'environnement.

### Variable d'environnement
Une variable d'environnement est un variable de système d'exploitation qui se situe au niveau de la session. Une session est créée lorsqu'on lance un programme ou qu'on se connecte à un terminal. Dès lors, les variables d'environnement peuvent être positionnées elles ne seront pas persistante en mémoire qu'au delà de la session. Elles sont souvent enregistrées dans un fichier de configuration système.

Sous unix/linux/mac pour positionner une variable dans une session terminal.

```
export ENV="dev"
```

Sous windows
```
set ENV="dev"
```

### Fichier de configuration
Fichier de configuration *monprogramme.conf* :
```
[dev]
filename=monfichier-dev.json

[preprod]
filename=monfichier-preprod.json

[prod]
filename=monfichier-prod.json
```

Code du programme:
```
import configparser
import os

env=os.environ.get('ENV', 'dev')
self.config = configparser.ConfigParser()
self.config.read('monprogramme.conf')
self.filename = self.config[env]['filename']
```

## Logging & Timing

La verbosité de son programme est un aspect important car c'est souvent le seul canal d'information que nous avons de celui-ci.

### Logger
La librairie **logging** est la plus répandue et intégrée. 

```
import logging
logging.basicConfig(level=logging.INFO)
logging.info("debut du programme")
x=1
logging.warning("Attention, ce programme ne fait rien! #lazy")
logging.debug(f"x:{x}")
logging.info("fin du programme")

INFO:root:debut du programme
WARNING:root:Attention, ce programme ne fait rien! #lazy
INFO:root:fin du programme
```

### Timer

### Décorateur @

### Barre de progression

TQDM

### Data Matching

## NLP

### Détection de language

### Fuzzy search


