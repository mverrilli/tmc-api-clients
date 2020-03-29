# Trigger

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of schedule | 
**interval** | **int** | Interval between task/plan running in days/weeks/months, required only if type of schedule is not equal to &#39;ONCE&#39;) | [optional] 
**start_date** | **str** | Date when the task should start to run | 
**time_zone** | **str** | Time zone for task schedule | 
**at_times** | [**TimeSchedule**](TimeSchedule.md) |  | [optional] 
**at_days** | [**DaySchedule**](DaySchedule.md) |  | [optional] 
**webhook** | [**Webhook**](Webhook.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


