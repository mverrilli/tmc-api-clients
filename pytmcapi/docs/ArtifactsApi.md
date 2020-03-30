# swagger_client.ArtifactsApi

All URIs are relative to *https://localhost/tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_artifact**](ArtifactsApi.md#get_artifact) | **GET** /artifacts/{id} | Get Artifact by id
[**get_artifact_of_version**](ArtifactsApi.md#get_artifact_of_version) | **GET** /artifacts/{id}/versions/{version} | Get Artifact of a specified version


# **get_artifact**
> Artifact get_artifact(id)

Get Artifact by id

Get Artifact by id

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
api_instance = swagger_client.ArtifactsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | artifact id

try:
    # Get Artifact by id
    api_response = api_instance.get_artifact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->get_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| artifact id | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_of_version**
> ArtifactVersion get_artifact_of_version(id, version)

Get Artifact of a specified version

Get Artifact of a specified version

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
api_instance = swagger_client.ArtifactsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | artifact id
version = 'version_example' # str | artifact version

try:
    # Get Artifact of a specified version
    api_response = api_instance.get_artifact_of_version(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->get_artifact_of_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| artifact id | 
 **version** | **str**| artifact version | 

### Return type

[**ArtifactVersion**](ArtifactVersion.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

