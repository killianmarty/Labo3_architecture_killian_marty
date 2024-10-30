import connexion
import six

from swagger_server import util
import json
import copy

def cours_get():  # noqa: E501
    """Retourne la liste des cours

     # noqa: E501


    :rtype: None
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    result = []
    for cours in data:
        obj = {
            "id": cours["id"],
            "name": cours["name"],
            "discipline": cours["discipline"],
            "tags": cours["tags"]
        }
        result.append(obj)

    return result


def cours_id_delete(id):  # noqa: E501
    """Supprime un cours

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    
    for cours in data:
        if cours['id'] == id:
            data['cours'].remove(cours)
            with open('swagger_server/cours.json', 'w') as file:
                json.dump(data, file, indent=4)
            return "Cours supprimé"
    
    return "Cours non trouvé"


def cours_id_get(id, mode=None):  # noqa: E501
    """Retourne les informations du cours

     # noqa: E501

    :param id: 
    :type id: int
    :param mode: 
    :type mode: str

    :rtype: None
    """
    # Par défaut le mode est "semaine"

    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    
    for cours in data:
        if cours['id'] == id:
            tmp = copy.deepcopy(cours)
            tmp.pop("fichiers")
            tmp.pop("dossiers")
            tmp["seances"] = {}
            if(mode == "module"):
                for seance in cours["seances"]:
                    if(not seance["thematique"] in tmp["seances"]):
                        tmp["seances"][seance["thematique"]] = []
                    tmp["seances"][seance["thematique"]].append(seance)
            else:
                for seance in cours["seances"]:
                    if(not ("semaine " + str(seance["semaine"])) in tmp["seances"]):
                        tmp["seances"]["semaine " + str(seance["semaine"])] = []
                    tmp["seances"]["semaine " + str(seance["semaine"])].append(seance)

            return tmp
    
    return "Cours non trouvé"


def cours_id_post(id):  # noqa: E501
    """Crée un nouveau cours

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    new_cours = connexion.request.get_json()
    
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    
    data.append(new_cours)
    
    with open('swagger_server/cours.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    return "Cours ajouté"
