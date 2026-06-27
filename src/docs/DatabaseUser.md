# DatabaseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**database_id** | **int** |  | [optional] 
**name** | **str** |  | 
**password_secret_id** | **int** |  | 
**hostname** | **str** |  | [optional] 
**status** | **str** |  | 
**dbs** | [**List[DatabaseDB]**](DatabaseDB.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from wodby.models.database_user import DatabaseUser

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseUser from a JSON string
database_user_instance = DatabaseUser.from_json(json)
# print the JSON string representation of the object
print(DatabaseUser.to_json())

# convert the object into a dict
database_user_dict = database_user_instance.to_dict()
# create an instance of DatabaseUser from a dict
database_user_from_dict = DatabaseUser.from_dict(database_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


