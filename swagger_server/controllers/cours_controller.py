import connexion
import six

from swagger_server import util
import json

def cours_get():  # noqa: E501
    """Retourne la liste des cours

     # noqa: E501


    :rtype: None
    """
    with open('../cours.json', 'r') as file:
        data = json.load(file)

    return data


def cours_id_delete(id):  # noqa: E501
    """Supprime un cours

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    with open('../cours.json', 'r') as file:
        data = json.load(file)
    
    for cours in data['cours']:
        if cours['id'] == id:
            data['cours'].remove(cours)
            with open('../cours.json', 'w') as file:
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
    with open('../cours.json', 'r') as file:
        data = json.load(file)
    
    for cours in data['cours']:
        if cours['id'] == id:
            return cours
    
    return "Cours non trouvé"


def cours_id_post(id):  # noqa: E501
    """Crée un nouveau cours

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    new_cours = connexion.request.get_json()
    
    with open('../cours.json', 'r') as file:
        data = json.load(file)
    
    data['cours'].append(new_cours)
    
    with open('../cours.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    return "Cours ajouté"
