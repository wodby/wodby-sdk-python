# ServiceManifestLinkValue

A value a service link hands to the service. A custom target of the link needs it unless it is optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | [optional] 
**secret** | **bool** |  | 
**optional** | **bool** |  | 

## Example

```python
from wodby.models.service_manifest_link_value import ServiceManifestLinkValue

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceManifestLinkValue from a JSON string
service_manifest_link_value_instance = ServiceManifestLinkValue.from_json(json)
# print the JSON string representation of the object
print(ServiceManifestLinkValue.to_json())

# convert the object into a dict
service_manifest_link_value_dict = service_manifest_link_value_instance.to_dict()
# create an instance of ServiceManifestLinkValue from a dict
service_manifest_link_value_from_dict = ServiceManifestLinkValue.from_dict(service_manifest_link_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


