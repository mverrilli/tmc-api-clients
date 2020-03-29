# RuntimeClustersApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addRemoteEngineToCluster**](RuntimeClustersApi.md#addRemoteEngineToCluster) | **PUT** /runtimes/remote-engine-clusters/{clusterId}/engines/{engineId} | Add Remote Engine to Remote Engine Cluster
[**createRemoteEngineCluster**](RuntimeClustersApi.md#createRemoteEngineCluster) | **POST** /runtimes/remote-engine-clusters | Create Remote Engine Cluster
[**deleteRemoteEngineCluster**](RuntimeClustersApi.md#deleteRemoteEngineCluster) | **DELETE** /runtimes/remote-engine-clusters/{clusterId} | Delete Remote Engine Cluster by id
[**getEngineClustersAvailable**](RuntimeClustersApi.md#getEngineClustersAvailable) | **GET** /runtimes/remote-engine-clusters | Get all (available) Remote Engine Clusters
[**getRemoteEngineCluster**](RuntimeClustersApi.md#getRemoteEngineCluster) | **GET** /runtimes/remote-engine-clusters/{clusterId} | Get Remote Engine Cluster by id
[**removeRemoteEngineFromCluster**](RuntimeClustersApi.md#removeRemoteEngineFromCluster) | **DELETE** /runtimes/remote-engine-clusters/{clusterId}/engines/{engineId} | Remove Remote Engine from Remote Engine Cluster


## **addRemoteEngineToCluster**

Add Remote Engine to Remote Engine Cluster

Add Remote Engine to Remote Engine Cluster

### Example
```bash
tmc-cli addRemoteEngineToCluster clusterId=value engineId=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **string** | remote engine cluster id |
 **engineId** | **string** | remote engine id |

### Return type

(empty response body)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: Not Applicable

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **createRemoteEngineCluster**

Create Remote Engine Cluster

Create Remote Engine Cluster

### Example
```bash
tmc-cli createRemoteEngineCluster
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterRequest**](ClusterRequest.md) | Remote Engine Cluster |

### Return type

[**EngineCluster**](EngineCluster.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **deleteRemoteEngineCluster**

Delete Remote Engine Cluster by id

Delete Remote Engine Cluster by id

### Example
```bash
tmc-cli deleteRemoteEngineCluster clusterId=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **string** | remote engine cluster id |

### Return type

(empty response body)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: Not Applicable

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getEngineClustersAvailable**

Get all (available) Remote Engine Clusters

Get all (available) Remote Engine Clusters

### Example
```bash
tmc-cli getEngineClustersAvailable  _s=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s** | **string** | search query (FIQL format), e.g. \"workspace.environment.id==5cb47ca4b1b5247f6006529e\",\"name==NewCluster\" | [optional]

### Return type

[**BaseEngine**](BaseEngine.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **getRemoteEngineCluster**

Get Remote Engine Cluster by id

Get Remote Engine Cluster by id

### Example
```bash
tmc-cli getRemoteEngineCluster clusterId=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **string** | remote engine cluster id |

### Return type

[**EngineCluster**](EngineCluster.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

## **removeRemoteEngineFromCluster**

Remove Remote Engine from Remote Engine Cluster

Remove Remote Engine from Remote Engine Cluster

### Example
```bash
tmc-cli removeRemoteEngineFromCluster clusterId=value engineId=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clusterId** | **string** | remote engine cluster id |
 **engineId** | **string** | remote engine id |

### Return type

(empty response body)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

