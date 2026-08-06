# AutomationTimeWindowInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Set to false to remove the configured time window. | 
**start** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] [default to 'UTC']
**days** | **List[str]** | Selected weekdays. Omit for every day. Overnight windows use the day on which the window starts. | [optional] 

## Example

```python
from wodby.models.automation_time_window_input import AutomationTimeWindowInput

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationTimeWindowInput from a JSON string
automation_time_window_input_instance = AutomationTimeWindowInput.from_json(json)
# print the JSON string representation of the object
print(AutomationTimeWindowInput.to_json())

# convert the object into a dict
automation_time_window_input_dict = automation_time_window_input_instance.to_dict()
# create an instance of AutomationTimeWindowInput from a dict
automation_time_window_input_from_dict = AutomationTimeWindowInput.from_dict(automation_time_window_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


