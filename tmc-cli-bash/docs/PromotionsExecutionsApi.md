# PromotionsExecutionsApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executePromotion**](PromotionsExecutionsApi.md#executePromotion) | **POST** /executions/promotions | Execute Promotion
[**getExecutionPromotionStatus**](PromotionsExecutionsApi.md#getExecutionPromotionStatus) | **GET** /executions/promotions/{id} | Get Promotion execution status


## **executePromotion**

Execute Promotion

Execute Promotion

### Example
```bash
tmc-cli executePromotion
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

## **getExecutionPromotionStatus**

Get Promotion execution status

Get Promotion execution status

### Example
```bash
tmc-cli getExecutionPromotionStatus id=value
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

