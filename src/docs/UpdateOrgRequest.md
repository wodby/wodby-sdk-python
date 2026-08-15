# UpdateOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**default_time_zone** | **str** |  | [optional] 
**registry_integration_id** | **int** | Omit or use null to preserve the current default, use 0 for the built-in registry, or use an organization-owned registry integration ID. | [optional] 
**ci_integration_id** | **int** | Omit or use null to preserve the current default, use 0 for the built-in CI service, or use an organization-owned CI integration ID. | [optional] 

## Example

```python
from wodby.models.update_org_request import UpdateOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrgRequest from a JSON string
update_org_request_instance = UpdateOrgRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrgRequest.to_json())

# convert the object into a dict
update_org_request_dict = update_org_request_instance.to_dict()
# create an instance of UpdateOrgRequest from a dict
update_org_request_from_dict = UpdateOrgRequest.from_dict(update_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


