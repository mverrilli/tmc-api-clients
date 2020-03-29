# TasksApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureTaskExecution**](TasksApi.md#configureTaskExecution) | **PUT** /executables/tasks/{id}/run-config | Configure Task execution
[**createTask**](TasksApi.md#createTask) | **POST** /executables/tasks | Create Task
[**getAvailableTasks**](TasksApi.md#getAvailableTasks) | **GET** /executables/tasks | Get available Tasks
[**getTask**](TasksApi.md#getTask) | **GET** /executables/tasks/{id} | Get Task by id
[**getTaskConfiguration**](TasksApi.md#getTaskConfiguration) | **GET** /executables/tasks/{id}/run-config | Get Task configuration


## **configureTaskExecution**

Configure Task execution

Configure Task execution

### Example
```bash
tmc-cli configureTaskExecution id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | task id |
 **body** | [**RunConfig**](RunConfig.md) | RunConfig |

### Return type

[**RunConfig**](RunConfig.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **createTask**

Create Task

Create Task

### Example
```bash
tmc-cli createTask
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskRequest**](TaskRequest.md) | Task to create |

### Return type

[**Task**](Task.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getAvailableTasks**

Get available Tasks

Get available Tasks

### Example
```bash
tmc-cli getAvailableTasks  name=value  environmentId=value  workspaceId=value  limit=value  offset=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **string** | task name filter | [optional]
 **environmentId** | **string** | environment id | [optional]
 **workspaceId** | **string** | workspace id | [optional]
 **limit** | **integer** | limit | [optional]
 **offset** | **integer** | offset | [optional]

### Return type

[**Page**](Page.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getTask**

Get Task by id

Get Task by id

### Example
```bash
tmc-cli getTask id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | task id |

### Return type

[**Task**](Task.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getTaskConfiguration**

Get Task configuration

Get Task configuration

### Example
```bash
tmc-cli getTaskConfiguration id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | task id |

### Return type

[**RunConfig**](RunConfig.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

