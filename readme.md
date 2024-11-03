# API système de cours

Mayatta Ndiayre, Killian Marty

## Fonctionnement

Cette API a été générée par "swagger-codegen-cli" à partir du fichier "api.yaml".

Pour le serveur, nous avons implémenté en Python le corps des fonctions liées à chaque endpoint. Les données sont stockées dans le fichier json "swagger_server/cours.json".

Pour les clients Python/Java, nous avons utilisé les fonctions client générées, et avons implémenté le programme principal permettant d'utiliser ces fonctions.

## Installation

1. Cloner ce repository git:

```bash
git clone https://github.com/killianmarty/Labo3_architecture_killian_marty
cd Labo3_architecture_killian_marty
```

2. Créer un environnement virtuel Python et installer les dépendances:

```bash
python -m venv .
Scripts\activate
pip install -r requirements.txt
```

## Lancer le serveur

```bash
python -m swagger_server
```

## Lancer le client

### Python

```bash
python -m swagger_server
```

### Java

```bash
cd swagger_server_java
javac Main.java
java Main
```


