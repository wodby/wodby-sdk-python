# UpdateKubernetesVersionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Target Kubernetes version from the cluster&#39;s upgrade plan. | 

## Example

```python
from wodby.models.update_kubernetes_version_input import UpdateKubernetesVersionInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKubernetesVersionInput from a JSON string
update_kubernetes_version_input_instance = UpdateKubernetesVersionInput.from_json(json)
# print the JSON string representation of the object
print(UpdateKubernetesVersionInput.to_json())

# convert the object into a dict
update_kubernetes_version_input_dict = update_kubernetes_version_input_instance.to_dict()
# create an instance of UpdateKubernetesVersionInput from a dict
update_kubernetes_version_input_from_dict = UpdateKubernetesVersionInput.from_dict(update_kubernetes_version_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


