# ImportInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_name** | **str** |  | [optional] 
**source** | **str** |  | 
**url** | **str** |  | [optional] 
**backup_id** | **int** |  | [optional] 
**var_from** | [**ImportFromInput**](ImportFromInput.md) |  | [optional] 

## Example

```python
from wodby.models.import_input import ImportInput

# TODO update the JSON string below
json = "{}"
# create an instance of ImportInput from a JSON string
import_input_instance = ImportInput.from_json(json)
# print the JSON string representation of the object
print(ImportInput.to_json())

# convert the object into a dict
import_input_dict = import_input_instance.to_dict()
# create an instance of ImportInput from a dict
import_input_from_dict = ImportInput.from_dict(import_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


