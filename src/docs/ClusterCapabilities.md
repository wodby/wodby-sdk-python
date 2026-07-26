# ClusterCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**envoy_gateway** | **bool** | Whether this cluster uses Envoy Gateway for application routing. | 
**redirect_routes** | **bool** | Whether this cluster supports routes with the REDIRECT action. | 

## Example

```python
from wodby.models.cluster_capabilities import ClusterCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCapabilities from a JSON string
cluster_capabilities_instance = ClusterCapabilities.from_json(json)
# print the JSON string representation of the object
print(ClusterCapabilities.to_json())

# convert the object into a dict
cluster_capabilities_dict = cluster_capabilities_instance.to_dict()
# create an instance of ClusterCapabilities from a dict
cluster_capabilities_from_dict = ClusterCapabilities.from_dict(cluster_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


