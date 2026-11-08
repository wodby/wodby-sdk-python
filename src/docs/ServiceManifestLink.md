# ServiceManifestLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**required** | **bool** |  | 
**selectors** | [**List[ServiceManifestLinkSelector]**](ServiceManifestLinkSelector.md) | The services the link may point at. A target must match one selector. | [optional] 
**custom** | **bool** | Whether the link accepts a custom target, whose values a user enters instead of choosing a target service. | 
**cross_app** | **bool** | Whether the link may point at a service of another app environment that accepts it. Across environments the link reads only the target&#39;s exports. | 
**values** | [**List[ServiceManifestLinkValue]**](ServiceManifestLinkValue.md) | The values the link hands to the service, whatever it points at. | 

## Example

```python
from wodby.models.service_manifest_link import ServiceManifestLink

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceManifestLink from a JSON string
service_manifest_link_instance = ServiceManifestLink.from_json(json)
# print the JSON string representation of the object
print(ServiceManifestLink.to_json())

# convert the object into a dict
service_manifest_link_dict = service_manifest_link_instance.to_dict()
# create an instance of ServiceManifestLink from a dict
service_manifest_link_from_dict = ServiceManifestLink.from_dict(service_manifest_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


