# DockerRegistryCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from wodby.models.docker_registry_credentials import DockerRegistryCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of DockerRegistryCredentials from a JSON string
docker_registry_credentials_instance = DockerRegistryCredentials.from_json(json)
# print the JSON string representation of the object
print(DockerRegistryCredentials.to_json())

# convert the object into a dict
docker_registry_credentials_dict = docker_registry_credentials_instance.to_dict()
# create an instance of DockerRegistryCredentials from a dict
docker_registry_credentials_from_dict = DockerRegistryCredentials.from_dict(docker_registry_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


