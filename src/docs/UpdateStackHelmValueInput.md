# UpdateStackHelmValueInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**secret** | **bool** |  | 

## Example

```python
from wodby.models.update_stack_helm_value_input import UpdateStackHelmValueInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStackHelmValueInput from a JSON string
update_stack_helm_value_input_instance = UpdateStackHelmValueInput.from_json(json)
# print the JSON string representation of the object
print(UpdateStackHelmValueInput.to_json())

# convert the object into a dict
update_stack_helm_value_input_dict = update_stack_helm_value_input_instance.to_dict()
# create an instance of UpdateStackHelmValueInput from a dict
update_stack_helm_value_input_from_dict = UpdateStackHelmValueInput.from_dict(update_stack_helm_value_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


