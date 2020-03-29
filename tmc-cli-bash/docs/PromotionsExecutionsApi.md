# PromotionsExecutionsApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute**](PromotionsExecutionsApi.md#execute) | **POST** /executions/promotions | Execute Promotion
[**getExecutionStatus**](PromotionsExecutionsApi.md#getExecutionStatus) | **GET** /executions/promotions/{id} | Get Promotion execution status


## **execute**

Execute Promotion

Execute Promotion

### Example
```bash
tmc-cli execute
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PromotionExecutableTask**](PromotionExecutableTask.md) | ExecutableTask |

### Return type

[**ExecutionIdentifier**](ExecutionIdentifier.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getExecutionStatus**

Get Promotion execution status

Get Promotion execution status

### Example
```bash
tmc-cli getExecutionStatus id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | execution ID |

### Return type

[**PromotionExecutionInfo**](PromotionExecutionInfo.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

