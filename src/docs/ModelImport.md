# ModelImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**source** | **str** |  | 
**status** | **str** |  | 
**filename** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**app_instance_id** | **int** |  | [optional] 
**app_service_id** | **int** |  | [optional] 
**database_id** | **int** |  | [optional] 
**database_db_id** | **int** |  | [optional] 
**app_service_deployment_id** | **int** |  | [optional] 
**task_id** | **int** |  | [optional] 
**backup_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from wodby.models.model_import import ModelImport

# TODO update the JSON string below
json = "{}"
# create an instance of ModelImport from a JSON string
model_import_instance = ModelImport.from_json(json)
# print the JSON string representation of the object
print(ModelImport.to_json())

# convert the object into a dict
model_import_dict = model_import_instance.to_dict()
# create an instance of ModelImport from a dict
model_import_from_dict = ModelImport.from_dict(model_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


