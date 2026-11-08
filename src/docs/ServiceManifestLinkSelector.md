# ServiceManifestLinkSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The service type a target must have, in upper case, such as DB or DATASTORE. | 
**option** | **str** | The service version a target must run, when the selector asks for one. | [optional] 
**labels** | **List[str]** | Labels a target service must all have. | [optional] 

## Example

```python
from wodby.models.service_manifest_link_selector import ServiceManifestLinkSelector

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceManifestLinkSelector from a JSON string
service_manifest_link_selector_instance = ServiceManifestLinkSelector.from_json(json)
# print the JSON string representation of the object
print(ServiceManifestLinkSelector.to_json())

# convert the object into a dict
service_manifest_link_selector_dict = service_manifest_link_selector_instance.to_dict()
# create an instance of ServiceManifestLinkSelector from a dict
service_manifest_link_selector_from_dict = ServiceManifestLinkSelector.from_dict(service_manifest_link_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


