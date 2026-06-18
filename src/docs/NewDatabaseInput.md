# NewDatabaseInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**project_id** | **int** |  | [optional] 
**env_id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**integration_kind_id** | **int** |  | 
**type** | **str** |  | 
**version** | **str** |  | 
**machine_type** | **str** |  | 
**storage_size** | **int** |  | [optional] 
**password** | **str** |  | [optional] 
**storage_autoscaling** | **bool** |  | [optional] 
**high_availability** | **bool** |  | [optional] 
**region** | **str** |  | [optional] 
**zone** | **str** |  | [optional] 
**resided_cluster_id** | **int** |  | [optional] 
**iops** | **int** |  | [optional] 

## Example

```python
from wodby.models.new_database_input import NewDatabaseInput

# TODO update the JSON string below
json = "{}"
# create an instance of NewDatabaseInput from a JSON string
new_database_input_instance = NewDatabaseInput.from_json(json)
# print the JSON string representation of the object
print(NewDatabaseInput.to_json())

# convert the object into a dict
new_database_input_dict = new_database_input_instance.to_dict()
# create an instance of NewDatabaseInput from a dict
new_database_input_from_dict = NewDatabaseInput.from_dict(new_database_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


