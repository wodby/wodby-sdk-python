# UpdateSecretValueInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**secret** | **bool** |  | 

## Example

```python
from wodby.models.update_secret_value_input import UpdateSecretValueInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSecretValueInput from a JSON string
update_secret_value_input_instance = UpdateSecretValueInput.from_json(json)
# print the JSON string representation of the object
print(UpdateSecretValueInput.to_json())

# convert the object into a dict
update_secret_value_input_dict = update_secret_value_input_instance.to_dict()
# create an instance of UpdateSecretValueInput from a dict
update_secret_value_input_from_dict = UpdateSecretValueInput.from_dict(update_secret_value_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


