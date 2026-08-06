# NewAppServiceLogStreamInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workload** | **str** |  | [optional] 
**container** | **str** |  | [optional] 
**pod** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_app_service_log_stream_input import NewAppServiceLogStreamInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewAppServiceLogStreamInput from a JSON string
new_app_service_log_stream_input_instance = NewAppServiceLogStreamInput.from_json(json)
# print the JSON string representation of the object
print(NewAppServiceLogStreamInput.to_json())

# convert the object into a dict
new_app_service_log_stream_input_dict = new_app_service_log_stream_input_instance.to_dict()
# create an instance of NewAppServiceLogStreamInput from a dict
new_app_service_log_stream_input_from_dict = NewAppServiceLogStreamInput.from_dict(new_app_service_log_stream_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


