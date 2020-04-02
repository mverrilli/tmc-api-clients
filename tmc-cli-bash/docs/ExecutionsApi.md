# ExecutionsApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executeTask**](ExecutionsApi.md#executeTask) | **POST** /executions | Execute Task
[**getExecutionTaskStatus**](ExecutionsApi.md#getExecutionTaskStatus) | **GET** /executions/{id} | Get Task execution status
[**stopExecution**](ExecutionsApi.md#stopExecution) | **DELETE** /executions/{id} | Terminate Task execution


## **executeTask**

Execute Task

Execute Task

### Example
```bash
tmc-cli executeTask
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExecutableTask**](ExecutableTask.md) | Executable identifier |

### Return type

[**ExecutionIdentifier**](ExecutionIdentifier.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getExecutionTaskStatus**

Get Task execution status

Get Task execution status

### Example
```bash
tmc-cli getExecutionTaskStatus id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | execution ID |

### Return type

[**JobExecutionStatus**](JobExecutionStatus.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **stopExecution**

Terminate Task execution

Terminate Task execution

### Example
```bash
tmc-cli stopExecution id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | execution ID |

### Return type

**string**

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

