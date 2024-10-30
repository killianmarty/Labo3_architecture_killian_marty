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
    # Load the existing data from the JSON file
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    # Find the course with the given id
    course = next((course for course in data['courses'] if course['id'] == id), None)

    if course:
        # Find the seance with the given idSeance
        seance = next((seance for seance in course['seances'] if seance['idSeance'] == idSeance), None)
        
        if seance:
            # Remove the seance from the course
            course['seances'].remove(seance)
            
            # Save the updated data back to the JSON file
            with open('swagger_server/cours.json', 'w') as file:
                json.dump(data, file, indent=4)
            return 'Seance deleted'
        else:
            return 'Seance not found', 404
    else:
        return 'Course not found', 404


def cours_id_seances_id_seance_get(id, idSeance):  # noqa: E501
    """Retourne les infos sur la séance

     # noqa: E501

    :param id: 
    :type id: int
    :param idSeance: 
    :type idSeance: int

    :rtype: None
    """
    # Load the existing data from the JSON file
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    # Find the course with the given id
    course = next((course for course in data['courses'] if course['id'] == id), None)

    if course:
        # Find the seance with the given idSeance
        seance = next((seance for seance in course['seances'] if seance['idSeance'] == idSeance), None)
        
        if seance:
            return seance
        else:
            return 'Seance not found', 404
    else:
        return 'Course not found', 404


def cours_id_seances_id_seance_post(id, idSeance):  # noqa: E501
    """Crée une nouvelle séance

     # noqa: E501

    :param id: 
    :type id: int
    :param idSeance: 
    :type idSeance: int

    :rtype: None
    """
    return 'do some magic!'
