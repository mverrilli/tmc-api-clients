# PlansExecutionsApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute**](PlansExecutionsApi.md#execute) | **POST** /executions/plans | Execute Plan
[**getExecutionStatus**](PlansExecutionsApi.md#getExecutionStatus) | **GET** /executions/plans/{id} | Get Plan execution status


## **execute**

Execute Plan

Execute Plan

### Example
```bash
tmc-cli execute
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanExecutableTask**](PlanExecutableTask.md) | Executable identifier |

### Return type

[**ExecutionIdentifier**](ExecutionIdentifier.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getExecutionStatus**

Get Plan execution status

Get Plan execution status

### Example
```bash
tmc-cli getExecutionStatus id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | execution ID |

### Return type

[**PlanExecutionStatus**](PlanExecutionStatus.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

