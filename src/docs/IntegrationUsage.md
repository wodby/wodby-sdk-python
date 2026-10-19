# IntegrationUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**category** | **str** | current for what uses the integration now, historical for records such as builds and backups, cleanup for pending removal of resources it created. | 
**kind** | **str** |  | 
**detail** | **str** |  | [optional] 
**target** | [**IntegrationUsageTarget**](IntegrationUsageTarget.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.integration_usage import IntegrationUsage

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationUsage from a JSON string
integration_usage_instance = IntegrationUsage.from_json(json)
# print the JSON string representation of the object
print(IntegrationUsage.to_json())

# convert the object into a dict
integration_usage_dict = integration_usage_instance.to_dict()
# create an instance of IntegrationUsage from a dict
integration_usage_from_dict = IntegrationUsage.from_dict(integration_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


