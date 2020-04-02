# PlansExecutionsApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executePlan**](PlansExecutionsApi.md#executePlan) | **POST** /executions/plans | Execute Plan
[**getExecutionPlanStatus**](PlansExecutionsApi.md#getExecutionPlanStatus) | **GET** /executions/plans/{id} | Get Plan execution status


## **executePlan**

Execute Plan

Execute Plan

### Example
```bash
tmc-cli executePlan
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

## **getExecutionPlanStatus**

Get Plan execution status

Get Plan execution status

### Example
```bash
tmc-cli getExecutionPlanStatus id=value
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

