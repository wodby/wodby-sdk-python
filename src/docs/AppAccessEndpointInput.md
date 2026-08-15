# AppAccessEndpointInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_port_id** | **int** |  | 
**host** | **str** |  | [optional] 
**primary** | **bool** |  | 

## Example

```python
from wodby.models.app_access_endpoint_input import AppAccessEndpointInput

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccessEndpointInput from a JSON string
app_access_endpoint_input_instance = AppAccessEndpointInput.from_json(json)
# print the JSON string representation of the object
print(AppAccessEndpointInput.to_json())

# convert the object into a dict
app_access_endpoint_input_dict = app_access_endpoint_input_instance.to_dict()
# create an instance of AppAccessEndpointInput from a dict
app_access_endpoint_input_from_dict = AppAccessEndpointInput.from_dict(app_access_endpoint_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


