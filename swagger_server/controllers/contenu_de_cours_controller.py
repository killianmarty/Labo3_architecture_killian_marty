import connexion
import six

from swagger_server import util


def cours_id_dossier_delete(id, dossier):  # noqa: E501
    """Supprime un dossier du cours

     # noqa: E501

    :param id: 
    :type id: dict | bytes
    :param dossier: 
    :type dossier: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        dossier = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cours_id_dossier_get(id, dossier):  # noqa: E501
    """Retourne un JSON du contenu du dossier

     # noqa: E501

    :param id: 
    :type id: dict | bytes
    :param dossier: 
    :type dossier: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        dossier = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cours_id_dossier_post(id):  # noqa: E501
    """Crée un nouveau dossier pour le cours

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cours_id_fichier_delete(id, chemin):  # noqa: E501
    """Supprime un fichier du cours

     # noqa: E501

    :param id: 
    :type id: dict | bytes
    :param chemin: 
    :type chemin: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        chemin = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cours_id_fichier_get(id, chemin):  # noqa: E501
    """Retourne un fichier selon le chemin spécifié

     # noqa: E501

    :param id: 
    :type id: dict | bytes
    :param chemin: 
    :type chemin: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        chemin = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cours_id_fichier_post(id):  # noqa: E501
    """Télécharge un fichier pour le cours

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
