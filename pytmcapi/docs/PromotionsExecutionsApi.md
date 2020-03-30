# swagger_client.PromotionsExecutionsApi

All URIs are relative to *https://localhost/tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute**](PromotionsExecutionsApi.md#execute) | **POST** /executions/promotions | Execute Promotion
[**get_execution_status**](PromotionsExecutionsApi.md#get_execution_status) | **GET** /executions/promotions/{id} | Get Promotion execution status


# **execute**
> ExecutionIdentifier execute(body)

Execute Promotion

Execute Promotion

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
api_instance = swagger_client.PromotionsExecutionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PromotionExecutableTask() # PromotionExecutableTask | ExecutableTask

try:
    # Execute Promotion
    api_response = api_instance.execute(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromotionsExecutionsApi->execute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PromotionExecutableTask**](PromotionExecutableTask.md)| ExecutableTask | 

### Return type

[**ExecutionIdentifier**](ExecutionIdentifier.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_status**
> PromotionExecutionInfo get_execution_status(id)

Get Promotion execution status

Get Promotion execution status

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
api_instance = swagger_client.PromotionsExecutionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | execution ID

try:
    # Get Promotion execution status
    api_response = api_instance.get_execution_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PromotionsExecutionsApi->get_execution_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| execution ID | 

### Return type

[**PromotionExecutionInfo**](PromotionExecutionInfo.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

