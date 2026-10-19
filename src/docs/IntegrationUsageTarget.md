# IntegrationUsageTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**title** | **str** |  | 
**icon** | **str** |  | [optional] 
**parent** | [**IntegrationUsageTarget**](IntegrationUsageTarget.md) | Resource that contains the target, such as the app environment of an app service. | [optional] 

## Example

```python
from wodby.models.integration_usage_target import IntegrationUsageTarget

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationUsageTarget from a JSON string
integration_usage_target_instance = IntegrationUsageTarget.from_json(json)
# print the JSON string representation of the object
print(IntegrationUsageTarget.to_json())

# convert the object into a dict
integration_usage_target_dict = integration_usage_target_instance.to_dict()
# create an instance of IntegrationUsageTarget from a dict
integration_usage_target_from_dict = IntegrationUsageTarget.from_dict(integration_usage_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


