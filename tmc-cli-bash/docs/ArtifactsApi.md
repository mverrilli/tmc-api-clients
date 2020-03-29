# ArtifactsApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getArtifact**](ArtifactsApi.md#getArtifact) | **GET** /artifacts/{id} | Get Artifact by id
[**getArtifactOfVersion**](ArtifactsApi.md#getArtifactOfVersion) | **GET** /artifacts/{id}/versions/{version} | Get Artifact of a specified version


## **getArtifact**

Get Artifact by id

Get Artifact by id

### Example
```bash
tmc-cli getArtifact id=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | artifact id |

### Return type

[**Artifact**](Artifact.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getArtifactOfVersion**

Get Artifact of a specified version

Get Artifact of a specified version

### Example
```bash
tmc-cli getArtifactOfVersion id=value version=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string** | artifact id |
 **version** | **string** | artifact version |

### Return type

[**ArtifactVersion**](ArtifactVersion.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

