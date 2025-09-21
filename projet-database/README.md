# Projet Database (Flask + MongoDB)

Mini-API REST en **Python (Flask)** connectée à **MongoDB** permettant de faire des opérations CRUD (Create, Read, Update, Delete) sur une collection `users`.

---

## 🚀 Prérequis

- Python 3.13.7 (installé via [pyenv](https://github.com/pyenv-win/pyenv-win))
- [MongoDB](https://www.mongodb.com/try/download/community) installé **ou** via Docker
- Git

---

## ⚙️ Installation

### 1. Cloner le projet
```bash
git clone https://github.com/<ton-utilisateur>/<ton-repo>.git
cd projet-database
```



### 2. Installer Python, activer un venv, installer les packages


```
pyenv install 3.13.7
pyenv global 3.13.7
python -m venv .venv
.venv\Scripts\Activate

```

### 3. Installer les pdépendances

```
pip install -r requirements.txt
```

### 4. Lancement du programme

Assurez-vous que MongoDB tourne sur `mongodb://localhost:27017/`.

Tu démarres MongoDB avec :

```
docker compose up -d
```

Vérifie que MongoDB tourne :

```
docker ps
```

Ton API Flask pourra ensuite se connecter à :
`
mongodb://localhost:27017/
`

Puis lancez l’API :

```
python app.py
```


Par défaut, Flask démarre sur :
👉 http://127.0.0.1:5000

### 5. Exemples d'operations CRUD avec curl

Ajouter un utilisateur (CREATE), retournera un ID, par exemple `66f5c123abc456def7890123`
```
curl -X POST http://127.0.0.1:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name":"Alice","email":"alice@example.com"}'
```     

Lister tous les utilisateurs (READ)
``` 
curl http://127.0.0.1:5000/users
``` 

Récupérer un utilisateur par ID (READ)
``` 
curl http://127.0.0.1:5000/users/<ID>

curl http://127.0.0.1:5000/users/66f5c123abc456def7890123
``` 

Mettre à jour un utilisateur (UPDATE)
```
curl -X PUT http://127.0.0.1:5000/users/66f5c123abc456def7890123 \
     -H "Content-Type: application/json" \
     -d '{"name":"Alice Updated","email":"alice_new@example.com"}'

```

Supprimer un utilisateur (DELETE)
```
curl -X DELETE http://127.0.0.1:5000/users/66f5c123abc456def7890123
```