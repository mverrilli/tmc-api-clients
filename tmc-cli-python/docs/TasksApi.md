# swagger_client.TasksApi

All URIs are relative to *https://localhost/tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_task_execution**](TasksApi.md#configure_task_execution) | **PUT** /executables/tasks/{id}/run-config | Configure Task execution
[**create_task**](TasksApi.md#create_task) | **POST** /executables/tasks | Create Task
[**get_available_tasks**](TasksApi.md#get_available_tasks) | **GET** /executables/tasks | Get available Tasks
[**get_task**](TasksApi.md#get_task) | **GET** /executables/tasks/{id} | Get Task by id
[**get_task_configuration**](TasksApi.md#get_task_configuration) | **GET** /executables/tasks/{id}/run-config | Get Task configuration


# **configure_task_execution**
> RunConfig configure_task_execution(id, body)

Configure Task execution

Configure Task execution

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | task id
body = swagger_client.RunConfig() # RunConfig | RunConfig

try:
    # Configure Task execution
    api_response = api_instance.configure_task_execution(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->configure_task_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| task id | 
 **body** | [**RunConfig**](RunConfig.md)| RunConfig | 

### Return type

[**RunConfig**](RunConfig.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> Task create_task(body)

Create Task

Create Task

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
body = swagger_client.TaskRequest() # TaskRequest | Task to create

try:
    # Create Task
    api_response = api_instance.create_task(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskRequest**](TaskRequest.md)| Task to create | 

### Return type

[**Task**](Task.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_tasks**
> Page get_available_tasks(name=name, environment_id=environment_id, workspace_id=workspace_id, limit=limit, offset=offset)

Get available Tasks

Get available Tasks

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | task name filter (optional)
environment_id = 'environment_id_example' # str | environment id (optional)
workspace_id = 'workspace_id_example' # str | workspace id (optional)
limit = 56 # int | limit (optional)
offset = 56 # int | offset (optional)

try:
    # Get available Tasks
    api_response = api_instance.get_available_tasks(name=name, environment_id=environment_id, workspace_id=workspace_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_available_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| task name filter | [optional] 
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

# **get_task**
> Task get_task(id)

Get Task by id

Get Task by id

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | task id

try:
    # Get Task by id
    api_response = api_instance.get_task(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| task id | 

### Return type

[**Task**](Task.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_configuration**
> RunConfig get_task_configuration(id)

Get Task configuration

Get Task configuration

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | task id

try:
    # Get Task configuration
    api_response = api_instance.get_task_configuration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| task id | 

### Return type

[**RunConfig**](RunConfig.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

