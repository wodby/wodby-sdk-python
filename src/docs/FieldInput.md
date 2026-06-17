# FieldInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from wodby.models.field_input import FieldInput

# TODO update the JSON string below
json = "{}"
# create an instance of FieldInput from a JSON string
field_input_instance = FieldInput.from_json(json)
# print the JSON string representation of the object
print(FieldInput.to_json())

# convert the object into a dict
field_input_dict = field_input_instance.to_dict()
# create an instance of FieldInput from a dict
field_input_from_dict = FieldInput.from_dict(field_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


