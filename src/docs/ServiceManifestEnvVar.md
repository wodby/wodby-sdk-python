# ServiceManifestEnvVar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**secret** | **bool** |  | 
**env** | **str** |  | [optional] 
**runtime** | **bool** |  | 
**build** | **bool** |  | 

## Example

```python
from wodby.models.service_manifest_env_var import ServiceManifestEnvVar

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceManifestEnvVar from a JSON string
service_manifest_env_var_instance = ServiceManifestEnvVar.from_json(json)
# print the JSON string representation of the object
print(ServiceManifestEnvVar.to_json())

# convert the object into a dict
service_manifest_env_var_dict = service_manifest_env_var_instance.to_dict()
# create an instance of ServiceManifestEnvVar from a dict
service_manifest_env_var_from_dict = ServiceManifestEnvVar.from_dict(service_manifest_env_var_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


