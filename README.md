## README – Setup Python avec pyenv, venv et requirements.txt

1️⃣ Installer Python avec pyenv-win

Installer pyenv-win (gestionnaire de versions Python pour Windows) :
https://github.com/pyenv-win/pyenv-win

Vérifier que pyenv est installé :

pyenv --version

2️⃣ Vérifier les versions de Python disponibles et installées

Lister les versions installées sur la machine :

pyenv versions


Vérifier la version active :

pyenv version

3️⃣ Installer une version de Python

Pour installer une version spécifique :

pyenv install 3.13.7


Vérifier l’installation :

python --version
pip --version

4️⃣ Définir la version de Python globalement

Version globale (utilisée par défaut sur toute la machine) :

pyenv global 3.13.7


Version locale (uniquement pour le projet courant) :

pyenv local 3.13.7


Cela crée un fichier .python-version dans le dossier du projet.

5️⃣ Créer un environnement virtuel (venv)

Depuis le dossier du projet :

python -m venv .venv


Activer l’environnement virtuel :

PowerShell :

.venv\Scripts\Activate.ps1


CMD classique :

.venv\Scripts\activate.bat


Git Bash / WSL :

source .venv/Scripts/activate


Quand le venv est activé, le prompt affichera (.venv).

6️⃣ Installer les packages depuis requirements.txt

Crée ton fichier requirements.txt (exemple minimal) :

requests==2.32.3
flask==3.0.3
rich==13.9.2
boto3==1.34.119
azure-identity==1.17.1
azure-mgmt-resource==23.1.0
kubernetes==30.1.0
black==24.8.0
pytest==8.3.2


Installer les packages dans le venv :

pip install -r requirements.txt


Mettre à jour le fichier requirements.txt si nécessaire :

pip freeze > requirements.txt

7️⃣ Vérifier les installations

Vérifier la version de Python :

python --version


Vérifier pip :

pip --version


Vérifier un package installé :

pip show black

8️⃣ Conseils pratiques

Toujours activer le venv avant de travailler sur le projet.

Pour partager le projet ou le déployer, les autres développeurs peuvent simplement exécuter :

pip install -r requirements.txt


Utiliser Black pour formatter le code automatiquement et pytest pour lancer les tests.

## Workflow conseillé pour chaque projet

```
python-mini-projets/
│
├─ projet-logs/
│   ├─ .venv/
│   ├─ main.py
│   └─ requirements.txt
│
├─ projet-cloud/
│   ├─ .venv/
│   ├─ main.py
│   └─ requirements.txt
│
├─ projet-api/
│   ├─ .venv/
│   ├─ main.py
│   └─ requirements.txt
│
└─ projet-dashboard/
    ├─ .venv/
    ├─ main.py
    └─ requirements.txt

```


Aller dans le dossier du projet :

cd projet-logs


Créer un venv :

python -m venv .venv


Activer le venv :

.venv\Scripts\Activate.ps1  # PowerShell


Installer les packages :

pip install -r requirements.txt


Lancer ton script Python :

python main.py


Si tu ajoutes de nouveaux packages :

pip install package_name
pip freeze > requirements.txt