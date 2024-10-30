import connexion
import six

from swagger_server import util
import json

def cours_id_seances_id_seance_delete(id, idSeance):  # noqa: E501
    """Supprime une séance

     # noqa: E501

    :param id: 
    :type id: int
    :param idSeance: 
    :type idSeance: int

    :rtype: None
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    for cours in data:
        if(cours["id"] == id):
            for seance in cours["seances"]:
                if(seance["id"] == idSeance):
                    cours["seances"].remove(seance)
                    with open('swagger_server/cours.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    return "Seance deleted"
    return "Seance not found", 400


def cours_id_seances_id_seance_get(id, idSeance):  # noqa: E501
    """Retourne les infos sur la séance

     # noqa: E501

    :param id: 
    :type id: int
    :param idSeance: 
    :type idSeance: int

    :rtype: None
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    for cours in data:
        if(cours["id"] == id):
            for seance in cours["seances"]:
                if(seance["id"] == idSeance):
                    return seance
    return "Seance not found", 400


def cours_id_seances_id_seance_post(id, idSeance):  # noqa: E501
    """Crée une nouvelle séance

     # noqa: E501

    :param id: 
    :type id: int
    :param idSeance: 
    :type idSeance: int

    :rtype: None
    """
    body = connexion.request.get_json()
    
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    
    obj = {
        "id": idSeance,
        "semaine": body["semaine"],
        "titre": body["titre"],
        "thematique": body["thematique"],
        "fichiers": body["fichiers"]
    }

    for cours in data:
        if cours["id"] == id:
            for seance in cours["seances"]:
                if seance["id"] == idSeance:
                    return "Seance already exists", 400
            cours["seances"].append(obj)
            with open('swagger_server/cours.json', 'w') as file:
                json.dump(data, file, indent=4)
            return "Seance created"
    return "Cours not found", 400
    
