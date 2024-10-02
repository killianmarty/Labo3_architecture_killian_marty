# swagger_client.RechercheDeCoursApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_tag_get**](RechercheDeCoursApi.md#search_tag_get) | **GET** /search/{tag} | Recherche de cours par tag


# **search_tag_get**
> search_tag_get(tag, mode=mode)

Recherche de cours par tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RechercheDeCoursApi()
tag = NULL # object | 
mode = NULL # object |  (optional)

try:
    # Recherche de cours par tag
    api_instance.search_tag_get(tag, mode=mode)
except ApiException as e:
    print("Exception when calling RechercheDeCoursApi->search_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**object**](.md)|  | 
 **mode** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

