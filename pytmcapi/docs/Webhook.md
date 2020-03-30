# Webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Webhook name | 
**description** | **str** | Webhook description | [optional] 
**trigger_calls** | **int** | Endpoint call count to run task|plan  | [optional] 
**trigger_timeout** | **int** | Time after which the task will starts from the moment the endpoint is first called  | [optional] 
**run_as_user** | **str** | The user on behalf of whom the task will be launched | [optional] 
**new_url** | **bool** | Indicates whether to generate new url | [optional] 
**url** | **str** | Webhook url | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


