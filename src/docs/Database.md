# Database


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**kind** | **str** |  | 
**status** | **str** |  | 
**version** | **str** |  | 
**region** | **str** |  | [optional] 
**zone** | **str** |  | [optional] 
**integration_id** | **int** |  | [optional] 
**app_service_id** | **int** |  | [optional] 
**env_id** | **int** | Legacy internal environment entity ID. Use envType. | 
**env_type** | **str** |  | 
**org_id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.database import Database

# TODO update the JSON string below
json = "{}"
# create an instance of Database from a JSON string
database_instance = Database.from_json(json)
# print the JSON string representation of the object
print(Database.to_json())

# convert the object into a dict
database_dict = database_instance.to_dict()
# create an instance of Database from a dict
database_from_dict = Database.from_dict(database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


