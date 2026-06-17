# StackService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**main** | **bool** |  | 
**disabled** | **bool** |  | 
**required** | **bool** |  | 
**replicas** | **int** |  | 
**service_rev_id** | **int** |  | 
**service_rev_name** | **str** |  | 
**service_rev_title** | **str** |  | 
**service_rev_version** | **str** |  | 
**build_source_integration_id** | **int** |  | [optional] 
**build_source_remote_repo_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.stack_service import StackService

# TODO update the JSON string below
json = "{}"
# create an instance of StackService from a JSON string
stack_service_instance = StackService.from_json(json)
# print the JSON string representation of the object
print(StackService.to_json())

# convert the object into a dict
stack_service_dict = stack_service_instance.to_dict()
# create an instance of StackService from a dict
stack_service_from_dict = StackService.from_dict(stack_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


