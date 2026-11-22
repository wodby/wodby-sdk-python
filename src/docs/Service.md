# Service


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**external** | **bool** |  | 
**public** | **bool** |  | 
**rev_id** | **int** |  | 
**latest_rev_number** | **int** |  | 
**org_id** | **int** |  | 
**ownership_scope** | **str** | org when the organization owns the resource, project when one project owns it. | 
**owner_project_id** | **int** |  | [optional] 
**available_to_all_projects** | **bool** | True when every project in the organization can use the resource without a project share. | 
**settings** | [**ServiceSettings**](ServiceSettings.md) |  | [optional] 
**vulnerabilities** | [**ServiceVulnerabilityHealth**](ServiceVulnerabilityHealth.md) |  | [optional] 
**archived_at** | **datetime** | When the service was archived. Absent while the service is in use. | [optional] 
**archive_reason** | **str** | Why the service is archived: manual when someone archived it, removed_from_git when a Git update no longer found it in its repository. A removed_from_git service is unarchived and updated when it returns to the repository. Absent while the service is in use. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


