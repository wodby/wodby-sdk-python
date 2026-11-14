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
**basic_auth_override** | **str** | Whether the stack overrides the service&#39;s basic auth default. | 
**basic_auth_default** | **bool** | Whether new app services of this stack service get their own basic auth entry by default. Always false without a public HTTP endpoint. | 
**replicas** | **int** |  | 
**service_rev_pinned** | **bool** |  | 
**outdated** | **bool** |  | 
**icon** | **str** |  | [optional] 
**eol** | **bool** | True when the version of the stack service&#39;s default option has reached its end of life. | [optional] 
**derivative** | **str** | The service derivative the stack service runs. Null for the service itself. | [optional] 
**parent_stack_service_id** | **int** | The stack service this derivative stack service belongs to. Null for the service itself. | [optional] 
**service_rev_id** | **int** |  | 
**service_rev_name** | **str** |  | 
**service_rev_title** | **str** |  | 
**service_rev_version** | **str** |  | 
**build_source_integration_id** | **int** |  | [optional] 
**build_source_remote_repo_id** | **str** |  | [optional] 
**options** | [**List[StackServiceOption]**](StackServiceOption.md) |  | [optional] 
**settings** | [**List[StackServiceSetting]**](StackServiceSetting.md) |  | [optional] 
**containers** | [**List[StackServiceContainer]**](StackServiceContainer.md) |  | [optional] 
**deployment_configuration** | [**ServiceDeploymentConfiguration**](ServiceDeploymentConfiguration.md) |  | 
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


