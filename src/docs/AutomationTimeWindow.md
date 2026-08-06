# AutomationTimeWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** |  | 
**end** | **str** |  | 
**time_zone** | **str** |  | 
**days** | **List[str]** |  | 

## Example

```python
from wodby.models.automation_time_window import AutomationTimeWindow

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationTimeWindow from a JSON string
automation_time_window_instance = AutomationTimeWindow.from_json(json)
# print the JSON string representation of the object
print(AutomationTimeWindow.to_json())

# convert the object into a dict
automation_time_window_dict = automation_time_window_instance.to_dict()
# create an instance of AutomationTimeWindow from a dict
automation_time_window_from_dict = AutomationTimeWindow.from_dict(automation_time_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


