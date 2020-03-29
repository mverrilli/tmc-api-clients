# PlansExecutablesApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurePlanExecution**](PlansExecutablesApi.md#configurePlanExecution) | **PUT** /executables/plans/{id}/run-config | Configure Plan execution
[**createPlan**](PlansExecutablesApi.md#createPlan) | **POST** /executables/plans | Create Plan
[**getAvailablePlans**](PlansExecutablesApi.md#getAvailablePlans) | **GET** /executables/plans | Get available Plans
[**getExecutableDetails**](PlansExecutablesApi.md#getExecutableDetails) | **GET** /executables/plans/{id} | Get Plan details
[**getPlanConfiguration**](PlansExecutablesApi.md#getPlanConfiguration) | **GET** /executables/plans/{id}/run-config | Get Plan configuration


## **configurePlanExecution**

Configure Plan execution

Configure Plan execution

### Example
```bash
tmc-cli configurePlanExecution id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | Plan id |
 **body** | [**RunConfig**](RunConfig.md) | RunConfig | [optional]

### Return type

[**RunConfig**](RunConfig.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **createPlan**

Create Plan

Create Plan

### Example
```bash
tmc-cli createPlan
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanRequest**](PlanRequest.md) | Execution plan |

### Return type

[**Plan**](Plan.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getAvailablePlans**

Get available Plans

Get available Plans

### Example
```bash
tmc-cli getAvailablePlans  name=value  environmentId=value  workspaceId=value  limit=value  offset=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **string** | plan name filter | [optional]
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

## **getExecutableDetails**

Get Plan details

Get Plan details

### Example
```bash
tmc-cli getExecutableDetails id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | executable ID |

### Return type

[**PlanExecutableDetails**](PlanExecutableDetails.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getPlanConfiguration**

Get Plan configuration

Get Plan configuration

### Example
```bash
tmc-cli getPlanConfiguration id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | plan id |

### Return type

[**RunConfig**](RunConfig.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

