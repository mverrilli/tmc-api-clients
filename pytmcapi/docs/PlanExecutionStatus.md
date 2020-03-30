# PlanExecutionStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | Job execution ID | 
**start_timestamp** | **datetime** | Start time of job execution | 
**finish_timestamp** | **datetime** | End time of job execution | [optional] 
**user_id** | **str** | User ID | 
**plan_id** | **str** | Plan ID | 
**execution_status** | **str** | Execution status | 
**planned_executable_count** | **int** | Number of planned executables | [optional] 
**done_executable_count** | **int** | Number of done executables | [optional] 
**done_executable_details** | [**list[JobExecutionStatus]**](JobExecutionStatus.md) | Exection activity info | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


