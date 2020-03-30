# PromotionExecutionInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | Job execution ID | 
**start_timestamp** | **datetime** | Start time of job execution | 
**finish_timestamp** | **datetime** | End time of job execution | [optional] 
**user_id** | **str** | User ID | 
**promotion_id** | **str** | Promotion Id | [optional] 
**keep_target_resources** | **bool** | keep target resources flag | [optional] 
**advanced** | [**AdvancedPromotionSpec**](AdvancedPromotionSpec.md) | advanced promotion specification | [optional] 
**defective** | **bool** | defective promotion flag | [optional] 
**status** | **str** | execution status | [optional] 
**status_message** | **str** | Execution status message | [optional] 
**workspaces** | [**list[WorkspacePromotionExecutionInfo]**](WorkspacePromotionExecutionInfo.md) | WorkspacePromotionExecutionInfo | [optional] 
**engines** | [**list[PromotionArtifactExecutionInfo]**](PromotionArtifactExecutionInfo.md) | Remote Engines PromotionExecutionInfo | [optional] 
**clusters** | [**list[PromotionArtifactExecutionInfo]**](PromotionArtifactExecutionInfo.md) | Remote Engine Clusters PromotionExecutionInfo | [optional] 
**pipeline_id** | **str** | Deprecated! Use Promotion Id instead | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


