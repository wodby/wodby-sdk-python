# ClusterCreationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**Cluster**](Cluster.md) |  | 
**task_id** | **int** | Task that provisions the cluster. | [optional] 

## Example

```python
from wodby.models.cluster_creation_result import ClusterCreationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreationResult from a JSON string
cluster_creation_result_instance = ClusterCreationResult.from_json(json)
# print the JSON string representation of the object
print(ClusterCreationResult.to_json())

# convert the object into a dict
cluster_creation_result_dict = cluster_creation_result_instance.to_dict()
# create an instance of ClusterCreationResult from a dict
cluster_creation_result_from_dict = ClusterCreationResult.from_dict(cluster_creation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


