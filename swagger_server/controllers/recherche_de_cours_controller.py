import connexion
import six

from swagger_server import util


def search_tag_get(tag, mode=None):  # noqa: E501
    """Recherche de cours par tag

     # noqa: E501

    :param tag: 
    :type tag: dict | bytes
    :param mode: 
    :type mode: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tag = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        mode = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
