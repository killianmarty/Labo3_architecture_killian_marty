# swagger_client.CoursApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cours_id_delete**](CoursApi.md#cours_id_delete) | **DELETE** /cours/{id} | Supprime un cours
[**cours_id_get**](CoursApi.md#cours_id_get) | **GET** /cours/{id} | Retourne les informations du cours
[**cours_id_post**](CoursApi.md#cours_id_post) | **POST** /cours/{id} | Crée un nouveau cours


# **cours_id_delete**
> cours_id_delete(id)

Supprime un cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
id = NULL # object | 

try:
    # Supprime un cours
    api_instance.cours_id_delete(id)
except ApiException as e:
    print("Exception when calling CoursApi->cours_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cours_id_get**
> cours_id_get(id)

Retourne les informations du cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
id = NULL # object | 

try:
    # Retourne les informations du cours
    api_instance.cours_id_get(id)
except ApiException as e:
    print("Exception when calling CoursApi->cours_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cours_id_post**
> cours_id_post(id)

Crée un nouveau cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
id = NULL # object | 

try:
    # Crée un nouveau cours
    api_instance.cours_id_post(id)
except ApiException as e:
    print("Exception when calling CoursApi->cours_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

