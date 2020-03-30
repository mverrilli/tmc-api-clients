# TimeSchedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of schedule at times | 
**times** | **list[str]** | Timestamps to run task/plan, required only if type of schedule at times equal to AT_SPECIFIC_TIMES | [optional] 
**time** | **str** | Timestamp to run task/plan, required only if type of schedule at times equal to AT_TIME | [optional] 
**start_time** | **str** | Interval start timestamp, required only if type of schedule at times equal to AT_INTERVALS | [optional] 
**end_time** | **str** | Interval end timestamp, required only if type of schedule at times equal to AT_INTERVALS | [optional] 
**interval** | **int** | Duration of interval in minutes, required only if type of schedule at times equal to AT_INTERVALS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


