# DatabaseVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from wodby.models.database_version import DatabaseVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseVersion from a JSON string
database_version_instance = DatabaseVersion.from_json(json)
# print the JSON string representation of the object
print(DatabaseVersion.to_json())

# convert the object into a dict
database_version_dict = database_version_instance.to_dict()
# create an instance of DatabaseVersion from a dict
database_version_from_dict = DatabaseVersion.from_dict(database_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


