import requests
import json

# URL de la requête
url = "http://127.0.0.1:8000/cours/2/seances/10"

# Corps de la requête en JSON
data = {
    "id": 10,
    "semaine": 1,
    "titre": "Séance 1",
    "thematique": "Python",
    "fichiers": [3, 4]
}

# Envoi de la requête POST
response = requests.post(url, json=data)

# Vérification du statut de la réponse
if response.status_code == 200:
    print("Requête réussie :", response.json())
else:
    print("Erreur :", response.status_code, response.text)
