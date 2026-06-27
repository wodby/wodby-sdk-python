# UpdateDatabaseUserDBsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_db_ids** | **List[int]** |  | 

## Example

```python
from wodby.models.update_database_user_dbs_input import UpdateDatabaseUserDBsInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDatabaseUserDBsInput from a JSON string
update_database_user_dbs_input_instance = UpdateDatabaseUserDBsInput.from_json(json)
# print the JSON string representation of the object
print(UpdateDatabaseUserDBsInput.to_json())

# convert the object into a dict
update_database_user_dbs_input_dict = update_database_user_dbs_input_instance.to_dict()
# create an instance of UpdateDatabaseUserDBsInput from a dict
update_database_user_dbs_input_from_dict = UpdateDatabaseUserDBsInput.from_dict(update_database_user_dbs_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


