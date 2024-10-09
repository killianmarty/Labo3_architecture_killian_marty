# swagger_client.ContenuDeCoursApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cours_id_dossier_delete**](ContenuDeCoursApi.md#cours_id_dossier_delete) | **DELETE** /cours/{id}/dossier | Supprime un dossier du cours
[**cours_id_dossier_get**](ContenuDeCoursApi.md#cours_id_dossier_get) | **GET** /cours/{id}/dossier | Retourne un JSON du contenu du dossier
[**cours_id_dossier_post**](ContenuDeCoursApi.md#cours_id_dossier_post) | **POST** /cours/{id}/dossier | Crée un nouveau dossier pour le cours
[**cours_id_fichier_delete**](ContenuDeCoursApi.md#cours_id_fichier_delete) | **DELETE** /cours/{id}/fichier | Supprime un fichier du cours
[**cours_id_fichier_get**](ContenuDeCoursApi.md#cours_id_fichier_get) | **GET** /cours/{id}/fichier | Retourne un fichier selon le chemin spécifié
[**cours_id_fichier_post**](ContenuDeCoursApi.md#cours_id_fichier_post) | **POST** /cours/{id}/fichier | Télécharge un fichier pour le cours


# **cours_id_dossier_delete**
> cours_id_dossier_delete(id, dossier)

Supprime un dossier du cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContenuDeCoursApi()
id = 56 # int | 
dossier = 'dossier_example' # str | 

try:
    # Supprime un dossier du cours
    api_instance.cours_id_dossier_delete(id, dossier)
except ApiException as e:
    print("Exception when calling ContenuDeCoursApi->cours_id_dossier_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **dossier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cours_id_dossier_get**
> cours_id_dossier_get(id, dossier)

Retourne un JSON du contenu du dossier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContenuDeCoursApi()
id = 56 # int | 
dossier = 'dossier_example' # str | 

try:
    # Retourne un JSON du contenu du dossier
    api_instance.cours_id_dossier_get(id, dossier)
except ApiException as e:
    print("Exception when calling ContenuDeCoursApi->cours_id_dossier_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **dossier** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cours_id_dossier_post**
> cours_id_dossier_post(id)

Crée un nouveau dossier pour le cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContenuDeCoursApi()
id = 56 # int | 

try:
    # Crée un nouveau dossier pour le cours
    api_instance.cours_id_dossier_post(id)
except ApiException as e:
    print("Exception when calling ContenuDeCoursApi->cours_id_dossier_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cours_id_fichier_delete**
> cours_id_fichier_delete(id, chemin)

Supprime un fichier du cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContenuDeCoursApi()
id = 56 # int | 
chemin = 'chemin_example' # str | 

try:
    # Supprime un fichier du cours
    api_instance.cours_id_fichier_delete(id, chemin)
except ApiException as e:
    print("Exception when calling ContenuDeCoursApi->cours_id_fichier_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **chemin** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cours_id_fichier_get**
> cours_id_fichier_get(id, chemin)

Retourne un fichier selon le chemin spécifié

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContenuDeCoursApi()
id = 56 # int | 
chemin = 'chemin_example' # str | 

try:
    # Retourne un fichier selon le chemin spécifié
    api_instance.cours_id_fichier_get(id, chemin)
except ApiException as e:
    print("Exception when calling ContenuDeCoursApi->cours_id_fichier_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **chemin** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cours_id_fichier_post**
> cours_id_fichier_post(id)

Télécharge un fichier pour le cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContenuDeCoursApi()
id = 56 # int | 

try:
    # Télécharge un fichier pour le cours
    api_instance.cours_id_fichier_post(id)
except ApiException as e:
    print("Exception when calling ContenuDeCoursApi->cours_id_fichier_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

