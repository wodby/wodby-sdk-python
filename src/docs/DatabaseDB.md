# DatabaseDB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**database_id** | **int** |  | [optional] 
**name** | **str** |  | 
**collation** | **str** |  | 
**charset** | **str** |  | 
**status** | **str** |  | 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.database_db import DatabaseDB

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseDB from a JSON string
database_db_instance = DatabaseDB.from_json(json)
# print the JSON string representation of the object
print(DatabaseDB.to_json())

# convert the object into a dict
database_db_dict = database_db_instance.to_dict()
# create an instance of DatabaseDB from a dict
database_db_from_dict = DatabaseDB.from_dict(database_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


