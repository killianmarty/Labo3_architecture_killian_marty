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

**Précision: le serveur se lance automatiquement sur le port 3000, il faut donc veiller à ce que ce port soit ouvert.**

## Utilisation du load balancer NGINX

Un load balancer NGINX est également à disposition, voici les étapes pour l'utiliser :

1. Modifier la configuration du serveur pour précisier les adresses IP des instances du serveur.

Pour cela, modifier le fichier "nginx-windows/conf/ipadresses.conf". Voici un exemple de syntaxe dans ce fichier (le port utilisé part le serveur de l'API est 3000).

```
server localhost:3000;
server 172.151.23.10:3000;
```

2. Lancer NGINX

**Pour lancer NGINX, il est important de se situer dans le dossier "nginx-windows".**

```bash
start nginx.exe
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

## Utilisation du client

Lors du lancement du client, il sera demander d'indiquer le domaine ainsi que le port. Le format attendu est le suivant:

```
http://adresse_ip:port
```

Le programme proposera ensuite les appels à l'API réalisables.

