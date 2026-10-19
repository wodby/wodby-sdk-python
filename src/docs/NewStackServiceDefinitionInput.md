# NewStackServiceDefinitionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **int** |  | 
**name** | **str** | Stack-local service name. | 
**title** | **str** |  | 
**required** | **bool** |  | [optional] 
**replicas** | **int** |  | 
**main** | **bool** |  | [optional] 
**service_rev_pinned** | **bool** |  | [optional] 

## Example

```python
from wodby.models.new_stack_service_definition_input import NewStackServiceDefinitionInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewStackServiceDefinitionInput from a JSON string
new_stack_service_definition_input_instance = NewStackServiceDefinitionInput.from_json(json)
# print the JSON string representation of the object
print(NewStackServiceDefinitionInput.to_json())

# convert the object into a dict
new_stack_service_definition_input_dict = new_stack_service_definition_input_instance.to_dict()
# create an instance of NewStackServiceDefinitionInput from a dict
new_stack_service_definition_input_from_dict = NewStackServiceDefinitionInput.from_dict(new_stack_service_definition_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


