# ServiceManifest

Typed fields of a service revision's manifest. raw holds the complete manifest as JSON, including the sections that have no typed field here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **str** |  | 
**scalable** | **bool** |  | 
**basic_auth** | **bool** | Whether the service asks for its public HTTP endpoints to be protected with basic auth by default. | 
**labels** | **List[str]** |  | [optional] 
**cross_app** | **bool** | Whether links of services in other app environments, of the same app or another one, may point at this service. | 
**exports** | [**List[ServiceManifestExport]**](ServiceManifestExport.md) | Values the services linking to this one read as {{link.exports.&lt;name&gt;}}. | 
**integrations** | [**List[ServiceIntegrationRequirement]**](ServiceIntegrationRequirement.md) |  | [optional] 
**links** | [**List[ServiceManifestLink]**](ServiceManifestLink.md) |  | [optional] 
**link_groups** | [**List[ServiceManifestLinkGroup]**](ServiceManifestLinkGroup.md) | Links that are alternatives to one another. An enabled app service needs at least min of them configured. | [optional] 

## Example

```python
from wodby.models.service_manifest import ServiceManifest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceManifest from a JSON string
service_manifest_instance = ServiceManifest.from_json(json)
# print the JSON string representation of the object
print(ServiceManifest.to_json())

# convert the object into a dict
service_manifest_dict = service_manifest_instance.to_dict()
# create an instance of ServiceManifest from a dict
service_manifest_from_dict = ServiceManifest.from_dict(service_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


