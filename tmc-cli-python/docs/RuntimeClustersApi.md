# swagger_client.RuntimeClustersApi

All URIs are relative to *https://localhost/tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remote_engine_to_cluster**](RuntimeClustersApi.md#add_remote_engine_to_cluster) | **PUT** /runtimes/remote-engine-clusters/{clusterId}/engines/{engineId} | Add Remote Engine to Remote Engine Cluster
[**create_remote_engine_cluster**](RuntimeClustersApi.md#create_remote_engine_cluster) | **POST** /runtimes/remote-engine-clusters | Create Remote Engine Cluster
[**delete_remote_engine_cluster**](RuntimeClustersApi.md#delete_remote_engine_cluster) | **DELETE** /runtimes/remote-engine-clusters/{clusterId} | Delete Remote Engine Cluster by id
[**get_engine_clusters_available**](RuntimeClustersApi.md#get_engine_clusters_available) | **GET** /runtimes/remote-engine-clusters | Get all (available) Remote Engine Clusters
[**get_remote_engine_cluster**](RuntimeClustersApi.md#get_remote_engine_cluster) | **GET** /runtimes/remote-engine-clusters/{clusterId} | Get Remote Engine Cluster by id
[**remove_remote_engine_from_cluster**](RuntimeClustersApi.md#remove_remote_engine_from_cluster) | **DELETE** /runtimes/remote-engine-clusters/{clusterId}/engines/{engineId} | Remove Remote Engine from Remote Engine Cluster


# **add_remote_engine_to_cluster**
> add_remote_engine_to_cluster(cluster_id, engine_id)

Add Remote Engine to Remote Engine Cluster

Add Remote Engine to Remote Engine Cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Access Token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: Basic Authentication
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RuntimeClustersApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | remote engine cluster id
engine_id = 'engine_id_example' # str | remote engine id

try:
    # Add Remote Engine to Remote Engine Cluster
    api_instance.add_remote_engine_to_cluster(cluster_id, engine_id)
except ApiException as e:
    print("Exception when calling RuntimeClustersApi->add_remote_engine_to_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| remote engine cluster id | 
 **engine_id** | **str**| remote engine id | 

### Return type

void (empty response body)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_remote_engine_cluster**
> EngineCluster create_remote_engine_cluster(body)

Create Remote Engine Cluster

Create Remote Engine Cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Access Token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: Basic Authentication
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RuntimeClustersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClusterRequest() # ClusterRequest | Remote Engine Cluster

try:
    # Create Remote Engine Cluster
    api_response = api_instance.create_remote_engine_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeClustersApi->create_remote_engine_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterRequest**](ClusterRequest.md)| Remote Engine Cluster | 

### Return type

[**EngineCluster**](EngineCluster.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_remote_engine_cluster**
> delete_remote_engine_cluster(cluster_id)

Delete Remote Engine Cluster by id

Delete Remote Engine Cluster by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Access Token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: Basic Authentication
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RuntimeClustersApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | remote engine cluster id

try:
    # Delete Remote Engine Cluster by id
    api_instance.delete_remote_engine_cluster(cluster_id)
except ApiException as e:
    print("Exception when calling RuntimeClustersApi->delete_remote_engine_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| remote engine cluster id | 

### Return type

void (empty response body)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_engine_clusters_available**
> BaseEngine get_engine_clusters_available(s=s)

Get all (available) Remote Engine Clusters

Get all (available) Remote Engine Clusters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Access Token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: Basic Authentication
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RuntimeClustersApi(swagger_client.ApiClient(configuration))
s = 's_example' # str | search query (FIQL format), e.g. \"workspace.environment.id==5cb47ca4b1b5247f6006529e\",\"name==NewCluster\" (optional)

try:
    # Get all (available) Remote Engine Clusters
    api_response = api_instance.get_engine_clusters_available(s=s)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeClustersApi->get_engine_clusters_available: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s** | **str**| search query (FIQL format), e.g. \&quot;workspace.environment.id&#x3D;&#x3D;5cb47ca4b1b5247f6006529e\&quot;,\&quot;name&#x3D;&#x3D;NewCluster\&quot; | [optional] 

### Return type

[**BaseEngine**](BaseEngine.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_engine_cluster**
> EngineCluster get_remote_engine_cluster(cluster_id)

Get Remote Engine Cluster by id

Get Remote Engine Cluster by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Access Token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: Basic Authentication
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RuntimeClustersApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | remote engine cluster id

try:
    # Get Remote Engine Cluster by id
    api_response = api_instance.get_remote_engine_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuntimeClustersApi->get_remote_engine_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| remote engine cluster id | 

### Return type

[**EngineCluster**](EngineCluster.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_remote_engine_from_cluster**
> remove_remote_engine_from_cluster(cluster_id, engine_id)

Remove Remote Engine from Remote Engine Cluster

Remove Remote Engine from Remote Engine Cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Access Token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: Basic Authentication
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RuntimeClustersApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | remote engine cluster id
engine_id = 'engine_id_example' # str | remote engine id

try:
    # Remove Remote Engine from Remote Engine Cluster
    api_instance.remove_remote_engine_from_cluster(cluster_id, engine_id)
except ApiException as e:
    print("Exception when calling RuntimeClustersApi->remove_remote_engine_from_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| remote engine cluster id | 
 **engine_id** | **str**| remote engine id | 

### Return type

void (empty response body)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

