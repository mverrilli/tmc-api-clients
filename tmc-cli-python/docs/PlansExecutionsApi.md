# swagger_client.PlansExecutionsApi

All URIs are relative to *https://localhost/tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute**](PlansExecutionsApi.md#execute) | **POST** /executions/plans | Execute Plan
[**get_execution_status**](PlansExecutionsApi.md#get_execution_status) | **GET** /executions/plans/{id} | Get Plan execution status


# **execute**
> ExecutionIdentifier execute(body)

Execute Plan

Execute Plan

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
api_instance = swagger_client.PlansExecutionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PlanExecutableTask() # PlanExecutableTask | Executable identifier

try:
    # Execute Plan
    api_response = api_instance.execute(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansExecutionsApi->execute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanExecutableTask**](PlanExecutableTask.md)| Executable identifier | 

### Return type

[**ExecutionIdentifier**](ExecutionIdentifier.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_status**
> PlanExecutionStatus get_execution_status(id)

Get Plan execution status

Get Plan execution status

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
api_instance = swagger_client.PlansExecutionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | execution ID

try:
    # Get Plan execution status
    api_response = api_instance.get_execution_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansExecutionsApi->get_execution_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| execution ID | 

### Return type

[**PlanExecutionStatus**](PlanExecutionStatus.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

