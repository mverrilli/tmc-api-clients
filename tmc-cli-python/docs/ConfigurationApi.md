# swagger_client.ConfigurationApi

All URIs are relative to *https://localhost/tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connection**](ConfigurationApi.md#get_connection) | **GET** /connections/{id} | Get Connection by id
[**get_resource**](ConfigurationApi.md#get_resource) | **GET** /resources/{id} | Get Resource by id


# **get_connection**
> RunConnection get_connection(id)

Get Connection by id

Get Connection by id

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
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Connection id

try:
    # Get Connection by id
    api_response = api_instance.get_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Connection id | 

### Return type

[**RunConnection**](RunConnection.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource**
> Resource get_resource(id)

Get Resource by id

Get Resource by id

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
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Resource id

try:
    # Get Resource by id
    api_response = api_instance.get_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Resource id | 

### Return type

[**Resource**](Resource.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

