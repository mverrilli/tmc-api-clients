# swagger_client.PlansExecutablesApi

All URIs are relative to *https://localhost/tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_plan_execution**](PlansExecutablesApi.md#configure_plan_execution) | **PUT** /executables/plans/{id}/run-config | Configure Plan execution
[**create_plan**](PlansExecutablesApi.md#create_plan) | **POST** /executables/plans | Create Plan
[**get_available_plans**](PlansExecutablesApi.md#get_available_plans) | **GET** /executables/plans | Get available Plans
[**get_executable_details**](PlansExecutablesApi.md#get_executable_details) | **GET** /executables/plans/{id} | Get Plan details
[**get_plan_configuration**](PlansExecutablesApi.md#get_plan_configuration) | **GET** /executables/plans/{id}/run-config | Get Plan configuration


# **configure_plan_execution**
> RunConfig configure_plan_execution(id, body=body)

Configure Plan execution

Configure Plan execution

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
api_instance = swagger_client.PlansExecutablesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Plan id
body = swagger_client.RunConfig() # RunConfig | RunConfig (optional)

try:
    # Configure Plan execution
    api_response = api_instance.configure_plan_execution(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansExecutablesApi->configure_plan_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plan id | 
 **body** | [**RunConfig**](RunConfig.md)| RunConfig | [optional] 

### Return type

[**RunConfig**](RunConfig.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plan**
> Plan create_plan(body)

Create Plan

Create Plan

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
api_instance = swagger_client.PlansExecutablesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PlanRequest() # PlanRequest | Execution plan

try:
    # Create Plan
    api_response = api_instance.create_plan(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansExecutablesApi->create_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanRequest**](PlanRequest.md)| Execution plan | 

### Return type

[**Plan**](Plan.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_plans**
> Page get_available_plans(name=name, environment_id=environment_id, workspace_id=workspace_id, limit=limit, offset=offset)

Get available Plans

Get available Plans

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
api_instance = swagger_client.PlansExecutablesApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | plan name filter (optional)
environment_id = 'environment_id_example' # str | environment id (optional)
workspace_id = 'workspace_id_example' # str | workspace id (optional)
limit = 56 # int | limit (optional)
offset = 56 # int | offset (optional)

try:
    # Get available Plans
    api_response = api_instance.get_available_plans(name=name, environment_id=environment_id, workspace_id=workspace_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansExecutablesApi->get_available_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| plan name filter | [optional] 
 **environment_id** | **str**| environment id | [optional] 
 **workspace_id** | **str**| workspace id | [optional] 
 **limit** | **int**| limit | [optional] 
 **offset** | **int**| offset | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_executable_details**
> PlanExecutableDetails get_executable_details(id)

Get Plan details

Get Plan details

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
api_instance = swagger_client.PlansExecutablesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | executable ID

try:
    # Get Plan details
    api_response = api_instance.get_executable_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansExecutablesApi->get_executable_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| executable ID | 

### Return type

[**PlanExecutableDetails**](PlanExecutableDetails.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan_configuration**
> RunConfig get_plan_configuration(id)

Get Plan configuration

Get Plan configuration

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
api_instance = swagger_client.PlansExecutablesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | plan id

try:
    # Get Plan configuration
    api_response = api_instance.get_plan_configuration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansExecutablesApi->get_plan_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| plan id | 

### Return type

[**RunConfig**](RunConfig.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

