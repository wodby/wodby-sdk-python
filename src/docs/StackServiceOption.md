# StackServiceOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**stack_service_id** | **int** |  | 
**version** | **str** |  | 
**default** | **bool** |  | 
**disabled** | **bool** |  | 

## Example

```python
from wodby.models.stack_service_option import StackServiceOption

# TODO update the JSON string below
json = "{}"
# create an instance of StackServiceOption from a JSON string
stack_service_option_instance = StackServiceOption.from_json(json)
# print the JSON string representation of the object
print(StackServiceOption.to_json())

# convert the object into a dict
stack_service_option_dict = stack_service_option_instance.to_dict()
# create an instance of StackServiceOption from a dict
stack_service_option_from_dict = StackServiceOption.from_dict(stack_service_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


