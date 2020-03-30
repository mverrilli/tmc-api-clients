# swagger_client.RuntimeEnginesApi

All URIs are relative to *https://localhost/tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_remote_engine**](RuntimeEnginesApi.md#create_remote_engine) | **POST** /runtimes/remote-engines | Create new Remote Engine
[**delete_remote_engine**](RuntimeEnginesApi.md#delete_remote_engine) | **DELETE** /runtimes/remote-engines/{id} | Delete Remote Engine by id
[**get_remote_engine**](RuntimeEnginesApi.md#get_remote_engine) | **GET** /runtimes/remote-engines/{id} | Get Remote Engine by id
[**get_remote_engines**](RuntimeEnginesApi.md#get_remote_engines) | **GET** /runtimes/remote-engines | Get all (available) Remote Engines
[**unpair_remote_engine**](RuntimeEnginesApi.md#unpair_remote_engine) | **DELETE** /runtimes/remote-engines/{id}/pairing | Unpair Remote Engine


# **create_remote_engine**
> Engine create_remote_engine(body)

Create new Remote Engine

Create new Remote Engine

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
api_instance = swagger_client.RuntimeEnginesApi(swagger_client.ApiClient(configuration))
body = swagger_client.EngineRequest() # EngineRequest | remote engine

try:
    # Create new Remote Engine
    api_response = api_instance.create_remote_engine(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnginesApi->create_remote_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EngineRequest**](EngineRequest.md)| remote engine | 

### Return type

[**Engine**](Engine.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_remote_engine**
> delete_remote_engine(id)

Delete Remote Engine by id

Delete Remote Engine by id

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
api_instance = swagger_client.RuntimeEnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | remote engine id

try:
    # Delete Remote Engine by id
    api_instance.delete_remote_engine(id)
except ApiException as e:
    print("Exception when calling RuntimeEnginesApi->delete_remote_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| remote engine id | 

### Return type

void (empty response body)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_engine**
> Engine get_remote_engine(id)

Get Remote Engine by id

Get Remote Engine by id

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
api_instance = swagger_client.RuntimeEnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | remote engine id

try:
    # Get Remote Engine by id
    api_response = api_instance.get_remote_engine(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnginesApi->get_remote_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| remote engine id | 

### Return type

[**Engine**](Engine.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_engines**
> Engine get_remote_engines(query=query)

Get all (available) Remote Engines

Get all (available) Remote Engines

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
api_instance = swagger_client.RuntimeEnginesApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | search query (FIQL format), e.g. \"environmentId==5cb47ca4b1b5247f6006529e\",\"status==PAIRED\" (optional)

try:
    # Get all (available) Remote Engines
    api_response = api_instance.get_remote_engines(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnginesApi->get_remote_engines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| search query (FIQL format), e.g. \&quot;environmentId&#x3D;&#x3D;5cb47ca4b1b5247f6006529e\&quot;,\&quot;status&#x3D;&#x3D;PAIRED\&quot; | [optional] 

### Return type

[**Engine**](Engine.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpair_remote_engine**
> str unpair_remote_engine(id)

Unpair Remote Engine

Unpair Remote Engine

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
api_instance = swagger_client.RuntimeEnginesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | remote engine id

try:
    # Unpair Remote Engine
    api_response = api_instance.unpair_remote_engine(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeEnginesApi->unpair_remote_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| remote engine id | 

### Return type

**str**

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

