# UpdateAppPortInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_port** | **int** | Public port on the cluster&#39;s address. | [optional] 

## Example

```python
from wodby.models.update_app_port_input import UpdateAppPortInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppPortInput from a JSON string
update_app_port_input_instance = UpdateAppPortInput.from_json(json)
# print the JSON string representation of the object
print(UpdateAppPortInput.to_json())

# convert the object into a dict
update_app_port_input_dict = update_app_port_input_instance.to_dict()
# create an instance of UpdateAppPortInput from a dict
update_app_port_input_from_dict = UpdateAppPortInput.from_dict(update_app_port_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


