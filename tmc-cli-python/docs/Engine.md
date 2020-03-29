# Engine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**name** | **str** | Resource name | 
**description** | **str** | Resource description | [optional] 
**workspace** | [**WorkspaceInfo**](WorkspaceInfo.md) | Resource workspace | [optional] 
**create_date** | **datetime** | Date of creation of the resource | 
**update_date** | **datetime** | Date of updating of the resource | [optional] 
**runtime_id** | **str** | Resource runtime id | 
**availability** | **str** | Availability status of engine|cluster | [optional] 
**environment_id** | **str** | Id of engine environment | 
**workspace_id** | **str** | Id of engine workspace | [optional] 
**run_profiles** | **list[str]** | Run profiles of engine | 
**status** | **str** | Engine status | 
**debug** | [**EngineDebug**](EngineDebug.md) | Remote Run/Debug configuration | [optional] 
**cluster_id** | **str** | cluster that this engine is part of | [optional] 
**pre_authorized_key** | **str** | Preauthorized key (only for not paired engine) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


