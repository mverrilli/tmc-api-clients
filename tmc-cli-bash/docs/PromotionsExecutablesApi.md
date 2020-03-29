# PromotionsExecutablesApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getExecutableDetails**](PromotionsExecutablesApi.md#getExecutableDetails) | **GET** /executables/promotions/{id} | Get Promotion details
[**getExecutablesAvailable**](PromotionsExecutablesApi.md#getExecutablesAvailable) | **GET** /executables/promotions | Get available Promotions


## **getExecutableDetails**

Get Promotion details

Get Promotion details

### Example
```bash
tmc-cli getExecutableDetails id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | executable ID |

### Return type

[**PromotionExecutableDetails**](PromotionExecutableDetails.md)

### Authorization

[Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getExecutablesAvailable**

Get available Promotions

Get available Promotions

### Example
```bash
tmc-cli getExecutablesAvailable  _s=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s** | **string** | search query (FIQL format), e.g. \"name==dev to prod*\" | [optional]

### Return type

[**array[PromotionExecutableInfo]**](PromotionExecutableInfo.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

