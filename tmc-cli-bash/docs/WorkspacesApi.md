# WorkspacesApi

All URIs are relative to */tmc/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getWorkspaces**](WorkspacesApi.md#getWorkspaces) | **GET** /workspaces | Get available Workspaces


## **getWorkspaces**

Get available Workspaces

Get available Workspaces

### Example
```bash
tmc-cli getWorkspaces  query=value
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **string** | search query (FIQL format), e.g. \"name==TestWorkspace\",\"environment.name==TestEnvironment\" | [optional]

### Return type

[**WorkspaceInfo**](WorkspaceInfo.md)

### Authorization

[Access Token](../README.md#Access Token), [Basic Authentication](../README.md#Basic Authentication)

### HTTP request headers

 - **Content-Type**: Not Applicable
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

