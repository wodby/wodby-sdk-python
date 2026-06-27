# NewDatabaseDBInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_id** | **int** |  | 
**name** | **str** |  | 
**charset** | **str** |  | [optional] 
**collation** | **str** |  | [optional] 

## Example

```python
from wodby.models.new_database_db_input import NewDatabaseDBInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewDatabaseDBInput from a JSON string
new_database_db_input_instance = NewDatabaseDBInput.from_json(json)
# print the JSON string representation of the object
print(NewDatabaseDBInput.to_json())

# convert the object into a dict
new_database_db_input_dict = new_database_db_input_instance.to_dict()
# create an instance of NewDatabaseDBInput from a dict
new_database_db_input_from_dict = NewDatabaseDBInput.from_dict(new_database_db_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


