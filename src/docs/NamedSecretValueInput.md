# NamedSecretValueInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**secret** | **bool** |  | 

## Example

```python
from wodby.models.named_secret_value_input import NamedSecretValueInput

# TODO update the JSON string below
json = "{}"
# create an instance of NamedSecretValueInput from a JSON string
named_secret_value_input_instance = NamedSecretValueInput.from_json(json)
# print the JSON string representation of the object
print(NamedSecretValueInput.to_json())

# convert the object into a dict
named_secret_value_input_dict = named_secret_value_input_instance.to_dict()
# create an instance of NamedSecretValueInput from a dict
named_secret_value_input_from_dict = NamedSecretValueInput.from_dict(named_secret_value_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


