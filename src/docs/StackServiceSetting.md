# StackServiceSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wodby.models.stack_service_setting import StackServiceSetting

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceSetting from a JSON string
stack_service_setting_instance = StackServiceSetting.from_json(json)
# print the JSON string representation of the object
print(StackServiceSetting.to_json())

# convert the object into a dict
stack_service_setting_dict = stack_service_setting_instance.to_dict()
# create an instance of StackServiceSetting from a dict
stack_service_setting_from_dict = StackServiceSetting.from_dict(stack_service_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


