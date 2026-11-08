# ServiceManifestExport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**secret** | **bool** |  | 

## Example

```python
from wodby.models.service_manifest_export import ServiceManifestExport

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceManifestExport from a JSON string
service_manifest_export_instance = ServiceManifestExport.from_json(json)
# print the JSON string representation of the object
print(ServiceManifestExport.to_json())

# convert the object into a dict
service_manifest_export_dict = service_manifest_export_instance.to_dict()
# create an instance of ServiceManifestExport from a dict
service_manifest_export_from_dict = ServiceManifestExport.from_dict(service_manifest_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


