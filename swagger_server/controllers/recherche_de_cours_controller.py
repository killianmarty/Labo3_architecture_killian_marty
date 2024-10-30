import connexion
import six

from swagger_server import util
import json

def search_get(tag):  # noqa: E501
    """Recherche de cours par tag

     # noqa: E501

    :param tag: 
    :type tag: str

    :rtype: None
    """
    def load_courses():
        with open('swagger_server/cours.json', 'r') as file:
            return json.load(file)

    courses = load_courses()

    result = []
    for course in courses:
        if tag in course['tags']:
           result.append(course)

    return result
