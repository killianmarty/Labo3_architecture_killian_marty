# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContenuDeCoursApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
chemin = 'chemin_example' # str | 

try:
    # Supprime un dossier du cours
    api_instance.cours_id_dossier_delete(id, chemin)
except ApiException as e:
    print("Exception when calling ContenuDeCoursApi->cours_id_dossier_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContenuDeCoursApi* | [**cours_id_dossier_delete**](docs/ContenuDeCoursApi.md#cours_id_dossier_delete) | **DELETE** /cours/{id}/dossier | Supprime un dossier du cours
*ContenuDeCoursApi* | [**cours_id_dossier_get**](docs/ContenuDeCoursApi.md#cours_id_dossier_get) | **GET** /cours/{id}/dossier | Retourne un JSON du contenu du dossier
*ContenuDeCoursApi* | [**cours_id_dossier_post**](docs/ContenuDeCoursApi.md#cours_id_dossier_post) | **POST** /cours/{id}/dossier | Crée un nouveau dossier pour le cours
*ContenuDeCoursApi* | [**cours_id_fichier_delete**](docs/ContenuDeCoursApi.md#cours_id_fichier_delete) | **DELETE** /cours/{id}/fichier | Supprime un fichier du cours
*ContenuDeCoursApi* | [**cours_id_fichier_get**](docs/ContenuDeCoursApi.md#cours_id_fichier_get) | **GET** /cours/{id}/fichier | Retourne un fichier selon le chemin spécifié
*ContenuDeCoursApi* | [**cours_id_fichier_post**](docs/ContenuDeCoursApi.md#cours_id_fichier_post) | **POST** /cours/{id}/fichier | Télécharge un fichier pour le cours
*CoursApi* | [**cours_get**](docs/CoursApi.md#cours_get) | **GET** /cours | Retourne la liste des cours
*CoursApi* | [**cours_id_delete**](docs/CoursApi.md#cours_id_delete) | **DELETE** /cours/{id} | Supprime un cours
*CoursApi* | [**cours_id_get**](docs/CoursApi.md#cours_id_get) | **GET** /cours/{id} | Retourne les informations du cours
*CoursApi* | [**cours_id_post**](docs/CoursApi.md#cours_id_post) | **POST** /cours/{id} | Crée un nouveau cours
*RechercheDeCoursApi* | [**search_tag_get**](docs/RechercheDeCoursApi.md#search_tag_get) | **GET** /search/{tag} | Recherche de cours par tag
*SeancesApi* | [**cours_id_seances_get**](docs/SeancesApi.md#cours_id_seances_get) | **GET** /cours/{id}/seances | Retourne la liste des séances
*SeancesApi* | [**cours_id_seances_id_seance_delete**](docs/SeancesApi.md#cours_id_seances_id_seance_delete) | **DELETE** /cours/{id}/seances/{idSeance} | Supprime une séance
*SeancesApi* | [**cours_id_seances_id_seance_get**](docs/SeancesApi.md#cours_id_seances_id_seance_get) | **GET** /cours/{id}/seances/{idSeance} | Retourne les infos sur la séance
*SeancesApi* | [**cours_id_seances_id_seance_post**](docs/SeancesApi.md#cours_id_seances_id_seance_post) | **POST** /cours/{id}/seances/{idSeance} | Crée une nouvelle séance


## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

## petstore_auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://petstore.swagger.io/oauth/authorize
- **Scopes**: 
 - **read:pets**: read your pets
 - **write:pets**: modify pets in your account


## Author



