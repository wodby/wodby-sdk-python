# AppServicePodCondition

A pod condition that isn't met.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The condition, such as PodScheduled, Initialized, ContainersReady or Ready. | 
**status** | **str** | False or Unknown. | 
**reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**last_transition_time** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.app_service_pod_condition import AppServicePodCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AppServicePodCondition from a JSON string
app_service_pod_condition_instance = AppServicePodCondition.from_json(json)
# print the JSON string representation of the object
print(AppServicePodCondition.to_json())

# convert the object into a dict
app_service_pod_condition_dict = app_service_pod_condition_instance.to_dict()
# create an instance of AppServicePodCondition from a dict
app_service_pod_condition_from_dict = AppServicePodCondition.from_dict(app_service_pod_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


