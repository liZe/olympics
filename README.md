# Olympics

Ce projet est un exemple d’application Python permettant de voir diverses
informations sur les Jeux Olympiques de Paris 2024.

Certaines données de la base de données viennent du dépôt
https://github.com/22Ranjan15/Paris-2024-Olympic_Dashboard

Il comprend 4 manières d’accéder aux données :

- une interface web dans `olympics/api.py`.
- une interface en ligne de commande dans `olympics/__main__.py`,
- une bibliothèque pour afficher des résultats dans le terminal dans `olympics/cli.py`,
- une bibliothèque bas-niveau pour accéder à la base de données dans `olympics/db.py`,

Cette application est écrite à des fins éducatives, et ne suit pas toutes les
bonnes pratiques du développement d’applications en Python.

Le sujet d’évaluation, comprenant des opérations à réaliser et des questions,
est inclus en bas de ce document.

Si vous avez des réponses à donner ou des remarques à faire, une section est
dédiée à cela en bas de ce document : écrivez ce que vous souhaitez, commitez
et pushez ce document README.md. N’écrivez pas de texte ailleurs que dans cette
section !

**Ce devoir est à rendre pour le 10 octobre à 22h. C’est un projet
individuel.**

Les rendus après cette date ne seront pas évalués. Pour des raisons d’équité,
aucune excuse concernant un oubli de commit ou de push ne sera toléré.

Les devoirs dont le contenu est trop proche, dont l’historique Git est douteux,
ou dont le code est si stupide qu’il ne peut pas avoir été écrit par un humain,
seront sanctionnés d’un D ou d’un E.


## Comment l’installer

1. Forkez le dépôt.

2. Passez le dépôt en privé.

   Sur la page de votre fork GitHub, dans l’onglet « Settings », la section
   « General », vous avez tout en bas l’option « Change repository
   visibility ».

3. Partagez votre dépôt en lecture avec moi.

   Sur la page de votre fork GitHub, dans l’onglet « Settings », la section
   « Collaborators and teams », vous avez un bouton « Add people ». Ajoutez
   l’utilisateur « liZe » (Guillaume Ayoub).

4. Clonez votre fork.

   `git clone git@github.com:YourNickName/olympics.git`

5. Allez dans votre dépôt cloné.

   `cd olympics`

6. Créez un environnement virtuel appelé `venv`.

   `python -m venv venv`

7. Activez votre environnement virtuel.

8. Installez les dépendances du projet.

   `pip install -e .`


## Comment l’utiliser

Pour utiliser l’application ou lancer les tests, veillez bien à être à la
racine du dépôt que vous avez cloné et à activer l’environnement virtuel.

### Pour utiliser l’API web

`fastapi dev olympics`

Vous avez alors accès à l’adresse `http://127.0.0.1:8000` et aux différentes
routes de l’application.

Une documentation automatique, avec une interface de test, est disponible à
l’adresse `http://127.0.0.1:8000/docs`.

Vous pouvez arrêter le serveur avec `Ctrl+C`.

### Pour utiliser la CLI

`python -m olympics --help`

Différentes commandes s’offrent à vous. Pour afficher le top 5 des médailles
individuelles, vous pouvez par exemple lancer :

`python -m olympics individual --top=5`

### Pour utiliser la bibliothèque

`python`

Dans l’interpréteur Python :

```python
>>> from olympics import cli
>>> help(cli)
```

Différentes fonctions sont disponibles. Pour afficher le top 3 des pays pour
les médailles collectives, vous pouvez par exemple lancer :

```python
>>> cli.top_collective(top=3)
```

Pour quitter l’interpréteur, utilisez `exit()`.

### Pour utiliser les fonctions bas-niveau de la base de données

`python`

Dans l’interpréteur Python :

```python
>>> from olympics import db
>>> help(db)
```

Différentes fonctions sont possibles. Pour récupérer une liste de tous les
athlètes et afficher les informations du premier, vous pouvez par exemple
lancer :

```python
>>> athletes = db.get_athletes()
>>> dict(athletes[0])
{'id': 1, 'name': 'Artur ALEKSANYAN', 'gender': 'male', 'country_id': 8}
```

Vous pouvez également lancer des requêtes SQL de cette manière :

```python
>>> cursor = db.get_connection().cursor()
>>> athletes = cursor.execute('SELECT id, name FROM athlete LIMIT 5').fetchall()
>>> dict(athletes[0])
{'id': 1, 'name': 'Artur ALEKSANYAN'}
```

Le schéma de la base de données est dans `database/model.sql`.

Pour quitter l’interpréteur, utilisez `exit()`.

### Lancer les tests

Quelques tests basiques sont disponibles dans le dossier `tests`.

Pour lancer les tests, lancez `python -m pytest`


## Sujet

Le but de cette évaluation est de tester, corriger et améliorer cette
application.

**Toutes les opérations sont à effectuer sur votre fork. Vérifiez d’avoir bien
tout commité et pushé à la fin de votre travail, en vérifiant les fichiers sur
GitHub. Ne faites pas de pull requests.**

**Faites au moins un commit par question, dans la mesure du possible.**

**Si vous n’arrivez pas à faire une question, ne perdez pas trop de temps,
passez à la suivante.**

La première étape est obligatoire. Si vous la faites parfaitement et que tout
est juste, vous validerez votre module. Par contre, si vous faites certaines
erreurs, vous risquez de ne pas valider.

C’est pour cela que vous avez trois étapes optionnelles. Vous pouvez en faire
une, deux, ou les trois, dans l’ordre que vous souhaitez. Si vous les réalisez
avec succès, vous pourrez améliorer le résultat de votre évaluation, pour
assurer la validation ou aller chercher le A (si vous écrivez du code vraiment
très, très intelligent).

Dans tous les cas, privilégiez l’intelligence à la quantité. Je préfère avoir
quelques tests pertinents que des centaines de tests répétitifs. Utilisez ce
que vous avez vu en cours, et la documentation des outils vus en cours.

Pensez que les tests sont idéalement indépendant des données : ces tests
devraient fonctionner même si l’on remplace la base avec des données d’une
autre année ! On utilise généralement un jeu de données pour les tests, mais ce
n’est pas le cas ici. Essayez, dans la mesure du possible, de ne pas trop vous
reposer sur les données de la base.

Ne me faites pas installer d’autres outils que les dépendances actuelles du
projet ou les bibliothèques que je vous demande d’installer pour cette
évaluation.

### Testez l’application à 100% (obligatoire)

Votre première mission est de tester l’application. Vous devrez au final avoir
100% de couverture pour les dossiers `olympics` et `tests`.

Lors de l’écriture de vos tests, vous devrez trouver un bug (au moins) caché
dans chacun des fichiers du dossier `olympics` (à part `__init__.py`). Pour
chacun de ces bugs, faites un commit comprenant à la fois la correction du bug
et un test de non-régression.

Les fonctions des modules Python sont faites pour être utilisées avec les bons
types de paramètres, et ne gèrent volontairement pas les appels avec des types
différents : ce ne sont donc pas des bugs. Par contre, les API web et en ligne
de commande doivent rejeter proprement les types inattendus : si l’application
lève une exception, on peut considérer cela comme un bug.

1. Installez la bibliothèque qu’il faut pour tester la couverture. Ajoutez
   cette bibliothèque aux dépendances déjà listées dans `pyproject.toml`.

2. Configurez pytest pour avoir la couverture uniquement sur les dossiers
   `olympics` et `tests`. Enregistrez cette configuration dans
   `pyproject.toml`.

3. Configurez pytest pour afficher le détail des lignes qui ne sont pas
   couvertes dans le terminal. Enregistrez cette configuration dans
   `pyproject.toml`.

4. Écrivez des tests pour `db.py`, dans le fichier `test_db.py`. Inspirez-vous
   du test déjà écrit.

5. Un bug est caché dans le fichier, faites un test de non-régression dédié et
   commitez-le avec la correction.

6. Recommencez les opérations 4 et 5 avec `api.py`.

7. Recommencez les opérations 4 et 5 avec `cli.py`. À quoi sert le paramètre
   « file » ? Comment cette technique s’appelle-t-elle ?

8. Recommencez les opérations 4 et 5 avec `__main__.py`. À quoi sert le
   commentaire « pragma: no cover » ? Grâce à votre expérience acquise avec la
   question précédente, utilisez la même technique pour améliorer l’efficacité
   de vos tests.

9. Vous devez avoir une couverture de 100%. Est-ce suffisant pour que
   l’ensemble du code fonctionne parfaitement ? Quels autres types de tests
   pourraient être idéalement réalisés ? (Ne les écrivez pas, décrivez-les
   simplement.)

10. Pourquoi vous a-t-il été demandé d’écrire les tests dans cet ordre-là ? À
    quoi cela sert-il de regrouper une correction de bug et un test de
    non-régression dans un commit commun, ne comprenant que cela ?

### Ajoutez une fonction en TDD (optionnel)

Ajoutez une fonction en suivant la méthode TDD. Vous pouvez créer un système de
recherche de pays par leur nom : rechercher « ugu » trouvera par exemple
« Portugal » et « Uganda ».

À chaque fois, écrivez un test qui ne passe pas, commitez-le, puis ajoutez le
code nécessaire pour faire passer ce test dans un autre commit.

Écrivez d’abord la fonction nécessaire dans `db.py`. Répétez les opérations
dans `api.py`, `cli.py` et `__main__.py`.

Veillez bien sûr à garder une couverture de tests de 100% !

### Configurez GitHub Actions sur votre dépôt (optionnel)

Activez GitHub Actions sur votre dépôt et configurez-le pour lancer les tests
sur plusieurs versions de Python, sur plusieurs plateformes, avec des choix
pertinents et justifiés. N’utilisez pas d’outils tiers, en particulier `tox`.

### Vérifiez la qualité du code (optionnel)

Mettez en place un outil de vérification de la qualité du code : installez,
configurez et utilisez `ruff`. Mettez en place dans votre dépôt Git des
méthodes pour s’assurer que le code suit toujours ces bonnes pratiques.


## Réponses et remarques

Si vous avez des réponses à écrire, des remarques à faire sur votre travail,
ajoutez-les à la fin de ce fichier.
.
Bug trouvé pour la db.py en utilisant la Cli.

Bug trouvé dans le code avec deux fois gold impactant le total dans le tableau.

Bug trouvé dans le code api.py, la fonction retourne les données des événements collectifs au lieu des événements individuels.

Bug trouvé dans le main.py ou un nombre "float" est présent alors qu'on essaie de le convertir en int dans le main.

7. Cette technique s'appelle la gestion de fichiers, ici le paramètre "file" permet de dirigier la sortie de la commande cli dans le console, mais elle peut aussi être diriger vers un fichier.

8. Le commentaire # pragma: no cover permet d'indiquer d’ignorer certaines lignes lors du calcul de la couverture de test. Ainsi même si ces lignes ne sont pas exécutées pendant les tests, elles ne seront pas comptabilisées comme des lignes non couvertes.

9. Même si j'obtiens une couverture de test à 100% ce n'est pas suffisant pour dire que le code est parfait car en effet il pourrait ne pas fonctionner selon certaines utilisations, il faudrait faire d'autres tests comme par exemple pour tester les performances , la sécurité du code ou d'autres de régression pour vérifier que les nouveautées n'introduisent pas de bug ou encore des tests à grande de charge pour voir si le système supporte un grand nombre de personnes ou alors des tests unitaires pour tester des fonctions isolées, pratiques pour un code chargé.

10. Les tests dans un certain ordre pour d’abord s’assurer que tout le code est couvert à 100%. Cela permet de vérifier que chaque partie du code est testée au moins une fois. Ensuite, en regroupant la correction d’un bug et le test qui vérifie que ce bug ne revient pas dans un même commit, on peut facilement voir quelle correction est associée à quel test. Cela aide à garder une trace claire des changements et à s’assurer que les bugs corrigés ne réapparaissent pas. En gros, c’est une façon de rendre le code plus fiable et bien documenté.


Avec cette dernière question je comprends mieux le test de non-régression et me rend compte que certains bug corrigés non pas eté commités avec un bon test de non régression pensant devoir tester avec le cmd.