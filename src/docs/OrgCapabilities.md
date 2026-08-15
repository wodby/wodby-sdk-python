# OrgCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_domains** | **bool** |  | 
**auto_backups** | **bool** |  | 
**users** | **bool** |  | 
**projects** | **bool** |  | 
**cron_schedules** | **bool** |  | 
**autoscale** | **bool** |  | 
**app_instance_pause** | **bool** |  | 
**web_shell** | **bool** |  | 
**wodby_cloud** | **bool** |  | 

## Example

```python
from wodby.models.org_capabilities import OrgCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCapabilities from a JSON string
org_capabilities_instance = OrgCapabilities.from_json(json)
# print the JSON string representation of the object
print(OrgCapabilities.to_json())

# convert the object into a dict
org_capabilities_dict = org_capabilities_instance.to_dict()
# create an instance of OrgCapabilities from a dict
org_capabilities_from_dict = OrgCapabilities.from_dict(org_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


