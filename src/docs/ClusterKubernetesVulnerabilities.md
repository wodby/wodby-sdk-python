# ClusterKubernetesVulnerabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The upstream patch version the vulnerabilities apply to, such as 1.33.5. | 
**vulnerabilities** | [**List[ClusterKubernetesVulnerability]**](ClusterKubernetesVulnerability.md) |  | 

## Example

```python
from wodby.models.cluster_kubernetes_vulnerabilities import ClusterKubernetesVulnerabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterKubernetesVulnerabilities from a JSON string
cluster_kubernetes_vulnerabilities_instance = ClusterKubernetesVulnerabilities.from_json(json)
# print the JSON string representation of the object
print(ClusterKubernetesVulnerabilities.to_json())

# convert the object into a dict
cluster_kubernetes_vulnerabilities_dict = cluster_kubernetes_vulnerabilities_instance.to_dict()
# create an instance of ClusterKubernetesVulnerabilities from a dict
cluster_kubernetes_vulnerabilities_from_dict = ClusterKubernetesVulnerabilities.from_dict(cluster_kubernetes_vulnerabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


