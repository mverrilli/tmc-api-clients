# swagger_client.PromotionsExecutablesApi

All URIs are relative to *https://localhost/tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_executable_details**](PromotionsExecutablesApi.md#get_executable_details) | **GET** /executables/promotions/{id} | Get Promotion details
[**get_executables_available**](PromotionsExecutablesApi.md#get_executables_available) | **GET** /executables/promotions | Get available Promotions


# **get_executable_details**
> PromotionExecutableDetails get_executable_details(id)

Get Promotion details

Get Promotion details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic Authentication
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.PromotionsExecutablesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | executable ID

try:
    # Get Promotion details
    api_response = api_instance.get_executable_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromotionsExecutablesApi->get_executable_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| executable ID | 

### Return type

[**PromotionExecutableDetails**](PromotionExecutableDetails.md)

### Authorization

[Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_executables_available**
> list[PromotionExecutableInfo] get_executables_available(s=s)

Get available Promotions

Get available Promotions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Access Token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: Basic Authentication
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.PromotionsExecutablesApi(swagger_client.ApiClient(configuration))
s = 's_example' # str | search query (FIQL format), e.g. \"name==dev to prod*\" (optional)

try:
    # Get available Promotions
    api_response = api_instance.get_executables_available(s=s)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromotionsExecutablesApi->get_executables_available: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s** | **str**| search query (FIQL format), e.g. \&quot;name&#x3D;&#x3D;dev to prod*\&quot; | [optional] 

### Return type

[**list[PromotionExecutableInfo]**](PromotionExecutableInfo.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

