# OrgUsageProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Null for usage of organization-owned resources and usage without a project. | 
**name** | **str** | The project name, empty for the organization row and deleted projects. | 
**title** | **str** |  | 
**deleted** | **bool** | The project no longer exists. Its recorded usage stays in the report. | 
**amount** | **float** | Total of the items at the public list price in USD. | 
**invoice_share** | **float** | Total of the items&#39; invoice shares in USD before tax, null while the invoiced amount is unknown. | 
**items** | [**List[OrgUsageItem]**](OrgUsageItem.md) |  | 

## Example

```python
from wodby.models.org_usage_project import OrgUsageProject

# TODO update the JSON string below
json = "{}"
# create an instance of OrgUsageProject from a JSON string
org_usage_project_instance = OrgUsageProject.from_json(json)
# print the JSON string representation of the object
print(OrgUsageProject.to_json())

# convert the object into a dict
org_usage_project_dict = org_usage_project_instance.to_dict()
# create an instance of OrgUsageProject from a dict
org_usage_project_from_dict = OrgUsageProject.from_dict(org_usage_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


