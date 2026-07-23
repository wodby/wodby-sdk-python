# ServiceManifestUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Optional service revision version; defaults to the current service version. | [optional] 
**manifest_yaml** | **str** | Complete Wodby service.yml manifest content. | 
**files** | **Dict[str, str]** | Optional referenced file contents keyed by manifest-relative path, for example Dockerfile or configs/app.conf. | [optional] 

## Example

```python
from wodby.models.service_manifest_update_input import ServiceManifestUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceManifestUpdateInput from a JSON string
service_manifest_update_input_instance = ServiceManifestUpdateInput.from_json(json)
# print the JSON string representation of the object
print(ServiceManifestUpdateInput.to_json())

# convert the object into a dict
service_manifest_update_input_dict = service_manifest_update_input_instance.to_dict()
# create an instance of ServiceManifestUpdateInput from a dict
service_manifest_update_input_from_dict = ServiceManifestUpdateInput.from_dict(service_manifest_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


