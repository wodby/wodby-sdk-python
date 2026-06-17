# KubeVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from wodby.models.kube_version import KubeVersion

# TODO update the JSON string below
json = "{}"
# create an instance of KubeVersion from a JSON string
kube_version_instance = KubeVersion.from_json(json)
# print the JSON string representation of the object
print(KubeVersion.to_json())

# convert the object into a dict
kube_version_dict = kube_version_instance.to_dict()
# create an instance of KubeVersion from a dict
kube_version_from_dict = KubeVersion.from_dict(kube_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


