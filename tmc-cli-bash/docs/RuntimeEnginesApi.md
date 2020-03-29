# RuntimeEnginesApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRemoteEngine**](RuntimeEnginesApi.md#createRemoteEngine) | **POST** /runtimes/remote-engines | Create new Remote Engine
[**deleteRemoteEngine**](RuntimeEnginesApi.md#deleteRemoteEngine) | **DELETE** /runtimes/remote-engines/{id} | Delete Remote Engine by id
[**getRemoteEngine**](RuntimeEnginesApi.md#getRemoteEngine) | **GET** /runtimes/remote-engines/{id} | Get Remote Engine by id
[**getRemoteEngines**](RuntimeEnginesApi.md#getRemoteEngines) | **GET** /runtimes/remote-engines | Get all (available) Remote Engines
[**unpairRemoteEngine**](RuntimeEnginesApi.md#unpairRemoteEngine) | **DELETE** /runtimes/remote-engines/{id}/pairing | Unpair Remote Engine


## **createRemoteEngine**

Create new Remote Engine

Create new Remote Engine

### Example
```bash
tmc-cli createRemoteEngine
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EngineRequest**](EngineRequest.md) | remote engine |

### Return type

[**Engine**](Engine.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **deleteRemoteEngine**

Delete Remote Engine by id

Delete Remote Engine by id

### Example
```bash
tmc-cli deleteRemoteEngine id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | remote engine id |

### Return type

(empty response body)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getRemoteEngine**

Get Remote Engine by id

Get Remote Engine by id

### Example
```bash
tmc-cli getRemoteEngine id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | remote engine id |

### Return type

[**Engine**](Engine.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getRemoteEngines**

Get all (available) Remote Engines

Get all (available) Remote Engines

### Example
```bash
tmc-cli getRemoteEngines  query=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **string** | search query (FIQL format), e.g. \"environmentId==5cb47ca4b1b5247f6006529e\",\"status==PAIRED\" | [optional]

### Return type

[**Engine**](Engine.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **unpairRemoteEngine**

Unpair Remote Engine

Unpair Remote Engine

### Example
```bash
tmc-cli unpairRemoteEngine id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | remote engine id |

### Return type

**string**

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

