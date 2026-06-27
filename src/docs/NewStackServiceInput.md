# NewStackServiceInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stack_id** | **int** |  | 
**service_id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**required** | **bool** |  | 
**replicas** | **int** |  | 

## Example

```python
from wodby.models.new_stack_service_input import NewStackServiceInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewStackServiceInput from a JSON string
new_stack_service_input_instance = NewStackServiceInput.from_json(json)
# print the JSON string representation of the object
print(NewStackServiceInput.to_json())

# convert the object into a dict
new_stack_service_input_dict = new_stack_service_input_instance.to_dict()
# create an instance of NewStackServiceInput from a dict
new_stack_service_input_from_dict = NewStackServiceInput.from_dict(new_stack_service_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


