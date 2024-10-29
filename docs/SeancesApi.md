# swagger_client.SeancesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cours_id_seances_id_seance_delete**](SeancesApi.md#cours_id_seances_id_seance_delete) | **DELETE** /cours/{id}/seances/{idSeance} | Supprime une séance
[**cours_id_seances_id_seance_get**](SeancesApi.md#cours_id_seances_id_seance_get) | **GET** /cours/{id}/seances/{idSeance} | Retourne les infos sur la séance
[**cours_id_seances_id_seance_post**](SeancesApi.md#cours_id_seances_id_seance_post) | **POST** /cours/{id}/seances/{idSeance} | Crée une nouvelle séance


# **cours_id_seances_id_seance_delete**
> cours_id_seances_id_seance_delete(id, id_seance)

Supprime une séance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeancesApi()
id = 56 # int | 
id_seance = 56 # int | 

try:
    # Supprime une séance
    api_instance.cours_id_seances_id_seance_delete(id, id_seance)
except ApiException as e:
    print("Exception when calling SeancesApi->cours_id_seances_id_seance_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **id_seance** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cours_id_seances_id_seance_get**
> cours_id_seances_id_seance_get(id, id_seance)

Retourne les infos sur la séance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeancesApi()
id = 56 # int | 
id_seance = 56 # int | 

try:
    # Retourne les infos sur la séance
    api_instance.cours_id_seances_id_seance_get(id, id_seance)
except ApiException as e:
    print("Exception when calling SeancesApi->cours_id_seances_id_seance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **id_seance** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cours_id_seances_id_seance_post**
> cours_id_seances_id_seance_post(id, id_seance)

Crée une nouvelle séance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SeancesApi()
id = 56 # int | 
id_seance = 56 # int | 

try:
    # Crée une nouvelle séance
    api_instance.cours_id_seances_id_seance_post(id, id_seance)
except ApiException as e:
    print("Exception when calling SeancesApi->cours_id_seances_id_seance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **id_seance** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

