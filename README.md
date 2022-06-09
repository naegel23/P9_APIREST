# P9_APIREST
APIREST est une application permettant de remonter et suivre des problèmes techniques (issue tracking system). Cette solution s’adresse à des entreprises clientes, en B2B.

L’application permet de :
1 - Suivi des problèmes pour les trois plateformes (site web, applications Android et iOS). 2 - Permettre essentiellement aux utilisateurs de créer divers projets, d'ajouter des utilisateurs à des projets spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en fonction de leurs priorités, de balises, etc.

Installation et exécution de l'application :
1 - Cloner le dépôt du projet à l'aide de la commande $ git clone https://github.com/naegel23/P9_APIREST (vous pouvez également télécharger le code en temps qu'archive zip)

2 - Rendez-vous depuis un terminal à la racine du projet api_rest

3 - Créer un environnement virtuel pour le projet avec  python3 -m venv env sous macos ou linux.

4 - Activez l'environnement virtuel avec  source env/bin/activate sous macos ou linux.

5 - Installez les dépendances du projet avec la commande $ pip install -r requirements.txt

6 - Créer la base de données avec la commande  python manage.py migrate SoftDesk

7 - Démarrer le serveur avec $ python manage.py runserver
