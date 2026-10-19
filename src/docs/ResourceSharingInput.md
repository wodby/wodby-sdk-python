# ResourceSharingInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ownership_scope** | **str** | org to make the organization the owner, project to make one project the owner. | 
**owner_project_id** | **int** | Project that becomes the owner. Required when ownershipScope is project. | [optional] 
**shared_projects** | [**List[ProjectShareInput]**](ProjectShareInput.md) | The complete list of project shares. A project left out loses its share. The owning project always keeps write access. You need write access to every project whose share you add or remove. | 
**available_to_all_projects** | **bool** | Lets every project in the organization use the resource without a project share. Only organization-owned clusters, integrations, services and stacks can be available to all projects. Omit it to keep the current setting. | [optional] 

## Example

```python
from wodby.models.resource_sharing_input import ResourceSharingInput

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSharingInput from a JSON string
resource_sharing_input_instance = ResourceSharingInput.from_json(json)
# print the JSON string representation of the object
print(ResourceSharingInput.to_json())

# convert the object into a dict
resource_sharing_input_dict = resource_sharing_input_instance.to_dict()
# create an instance of ResourceSharingInput from a dict
resource_sharing_input_from_dict = ResourceSharingInput.from_dict(resource_sharing_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


