import connexion
import six

from swagger_server import util


def cours_seances_id_delete(id):  # noqa: E501
    """Supprime une séance

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cours_seances_id_get(id):  # noqa: E501
    """Retourne les infos sur la séance

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cours_seances_id_post(id):  # noqa: E501
    """Crée une nouvelle séance

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
