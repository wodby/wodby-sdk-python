# ResourceSharing

Who owns a resource and which projects can use it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ownership_scope** | **str** | org when the organization owns the resource, project when one project owns it. | 
**owner_project_id** | **int** | Project that owns the resource when ownershipScope is project. | [optional] 
**available_to_all_projects** | **bool** | True when every project in the organization can use the resource without a project share. Only organization-owned clusters, integrations, services and stacks can be available to all projects; it is always false for other resources. | 
**shared_projects** | [**List[ResourceProjectShare]**](ResourceProjectShare.md) | Projects the resource is shared with that you can see. The owning project has the owner role. | 

## Example

```python
from wodby.models.resource_sharing import ResourceSharing

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSharing from a JSON string
resource_sharing_instance = ResourceSharing.from_json(json)
# print the JSON string representation of the object
print(ResourceSharing.to_json())

# convert the object into a dict
resource_sharing_dict = resource_sharing_instance.to_dict()
# create an instance of ResourceSharing from a dict
resource_sharing_from_dict = ResourceSharing.from_dict(resource_sharing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


