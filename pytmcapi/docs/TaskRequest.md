# TaskRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Task name | 
**description** | **str** | Task description | 
**environment_id** | **str** | Environment id of task to create | 
**workspace_id** | **str** | Workspace id of task to create | 
**artifact** | [**ArtifactRequest**](ArtifactRequest.md) | Artifact used in task | 
**tags** | **list[str]** | Task tags | [optional] 
**connections** | **dict(str, str)** | Task connections | [optional] 
**parameters** | **dict(str, str)** | Task parameters | [optional] 
**resources** | **dict(str, str)** | Task resources | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


