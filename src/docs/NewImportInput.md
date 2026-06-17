# NewImportInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_id** | **int** |  | [optional] 
**database_dbid** | **int** |  | [optional] 
**var_import** | [**ImportInput**](ImportInput.md) |  | 

## Example

```python
from wodby.models.new_import_input import NewImportInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewImportInput from a JSON string
new_import_input_instance = NewImportInput.from_json(json)
# print the JSON string representation of the object
print(NewImportInput.to_json())

# convert the object into a dict
new_import_input_dict = new_import_input_instance.to_dict()
# create an instance of NewImportInput from a dict
new_import_input_from_dict = NewImportInput.from_dict(new_import_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


