# ServiceManifestLinkGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | [optional] 
**links** | **List[str]** | Names of the links in the group. | 
**min** | **int** |  | 

## Example

```python
from wodby.models.service_manifest_link_group import ServiceManifestLinkGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceManifestLinkGroup from a JSON string
service_manifest_link_group_instance = ServiceManifestLinkGroup.from_json(json)
# print the JSON string representation of the object
print(ServiceManifestLinkGroup.to_json())

# convert the object into a dict
service_manifest_link_group_dict = service_manifest_link_group_instance.to_dict()
# create an instance of ServiceManifestLinkGroup from a dict
service_manifest_link_group_from_dict = ServiceManifestLinkGroup.from_dict(service_manifest_link_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


