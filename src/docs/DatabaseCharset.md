# DatabaseCharset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**default_collation** | **str** |  | 
**default** | **bool** |  | 

## Example

```python
from wodby.models.database_charset import DatabaseCharset

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseCharset from a JSON string
database_charset_instance = DatabaseCharset.from_json(json)
# print the JSON string representation of the object
print(DatabaseCharset.to_json())

# convert the object into a dict
database_charset_dict = database_charset_instance.to_dict()
# create an instance of DatabaseCharset from a dict
database_charset_from_dict = DatabaseCharset.from_dict(database_charset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


