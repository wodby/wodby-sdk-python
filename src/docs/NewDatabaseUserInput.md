# NewDatabaseUserInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_id** | **int** |  | 
**name** | **str** |  | 
**password** | **str** |  | 
**hostname** | **str** |  | [optional] 
**database_db_ids** | **List[int]** |  | [optional] 

## Example

```python
from wodby.models.new_database_user_input import NewDatabaseUserInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewDatabaseUserInput from a JSON string
new_database_user_input_instance = NewDatabaseUserInput.from_json(json)
# print the JSON string representation of the object
print(NewDatabaseUserInput.to_json())

# convert the object into a dict
new_database_user_input_dict = new_database_user_input_instance.to_dict()
# create an instance of NewDatabaseUserInput from a dict
new_database_user_input_from_dict = NewDatabaseUserInput.from_dict(new_database_user_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


