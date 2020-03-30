# swagger_client.WorkspacesApi

All URIs are relative to *https://localhost/tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workspaces**](WorkspacesApi.md#get_workspaces) | **GET** /workspaces | Get available Workspaces


# **get_workspaces**
> WorkspaceInfo get_workspaces(query=query)

Get available Workspaces

Get available Workspaces

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
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | search query (FIQL format), e.g. \"name==TestWorkspace\",\"environment.name==TestEnvironment\" (optional)

try:
    # Get available Workspaces
    api_response = api_instance.get_workspaces(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| search query (FIQL format), e.g. \&quot;name&#x3D;&#x3D;TestWorkspace\&quot;,\&quot;environment.name&#x3D;&#x3D;TestEnvironment\&quot; | [optional] 

### Return type

[**WorkspaceInfo**](WorkspaceInfo.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

