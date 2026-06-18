# ImportFromInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_db_id** | **int** |  | [optional] 
**app_service_id** | **int** |  | [optional] 
**backup_name** | **str** |  | [optional] 

## Example

```python
from wodby.models.import_from_input import ImportFromInput

# TODO update the JSON string below
json = "{}"
# create an instance of ImportFromInput from a JSON string
import_from_input_instance = ImportFromInput.from_json(json)
# print the JSON string representation of the object
print(ImportFromInput.to_json())

# convert the object into a dict
import_from_input_dict = import_from_input_instance.to_dict()
# create an instance of ImportFromInput from a dict
import_from_input_from_dict = ImportFromInput.from_dict(import_from_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


