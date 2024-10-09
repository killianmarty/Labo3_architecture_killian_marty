# swagger_client.SeancesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cours_seances_id_delete**](SeancesApi.md#cours_seances_id_delete) | **DELETE** /cours/seances/{id} | Supprime une séance
[**cours_seances_id_get**](SeancesApi.md#cours_seances_id_get) | **GET** /cours/seances/{id} | Retourne les infos sur la séance
[**cours_seances_id_post**](SeancesApi.md#cours_seances_id_post) | **POST** /cours/seances/{id} | Crée une nouvelle séance


# **cours_seances_id_delete**
> cours_seances_id_delete(id)

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

try:
    # Supprime une séance
    api_instance.cours_seances_id_delete(id)
except ApiException as e:
    print("Exception when calling SeancesApi->cours_seances_id_delete: %s\n" % e)
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

# **cours_seances_id_get**
> cours_seances_id_get(id)

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

try:
    # Retourne les infos sur la séance
    api_instance.cours_seances_id_get(id)
except ApiException as e:
    print("Exception when calling SeancesApi->cours_seances_id_get: %s\n" % e)
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

# **cours_seances_id_post**
> cours_seances_id_post(id)

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

try:
    # Crée une nouvelle séance
    api_instance.cours_seances_id_post(id)
except ApiException as e:
    print("Exception when calling SeancesApi->cours_seances_id_post: %s\n" % e)
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

