import connexion
import six

from swagger_server import util
import json


def search_tag_get(tag, mode=None):  # noqa: E501
    """Recherche de cours par tag

     # noqa: E501

    :param tag: 
    :type tag: str
    :param mode: 
    :type mode: str

    :rtype: None
    """
    def load_courses():
        with open('../cours.json', 'r') as file:
            return json.load(file)

    courses = load_courses()

    result = []
    for course in courses:
        if tag in course['tags']:
           result.append(course["id"])

    return result
