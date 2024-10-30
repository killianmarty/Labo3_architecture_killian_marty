import requests
import json

# URL de la requête
url = "http://172.16.14.35:8000/cours/2/fichier/11"

# Corps de la requête en JSON
data = {
    "titre": "fichier",
    "type": "pdf",
    "idParent": 100
}

# Envoi de la requête POST
response = requests.post(url, json=data)

# Vérification du statut de la réponse
if response.status_code == 200:
    print("Requête réussie :", response.json())
else:
    print("Erreur :", response.status_code, response.text)
