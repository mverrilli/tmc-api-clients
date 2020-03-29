# ConfigurationApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConnection**](ConfigurationApi.md#getConnection) | **GET** /connections/{id} | Get Connection by id
[**getResource**](ConfigurationApi.md#getResource) | **GET** /resources/{id} | Get Resource by id


## **getConnection**

Get Connection by id

Get Connection by id

### Example
```bash
tmc-cli getConnection id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | Connection id |

### Return type

[**RunConnection**](RunConnection.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getResource**

Get Resource by id

Get Resource by id

### Example
```bash
tmc-cli getResource id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | Resource id |

### Return type

[**Resource**](Resource.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

