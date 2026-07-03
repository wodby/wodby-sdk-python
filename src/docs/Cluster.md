# Cluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**status** | **str** |  | 
**serverless** | **bool** |  | 
**demo** | **bool** |  | 
**wodby** | **bool** |  | 
**k3s** | **bool** |  | 
**single_node** | **bool** |  | 
**version** | **str** |  | [optional] 
**infra_version** | **str** |  | 
**min_node_count** | **int** |  | [optional] 
**max_node_count** | **int** |  | [optional] 
**last_nodes_ready** | **int** |  | [optional] 
**last_nodes_total** | **int** |  | [optional] 
**region** | **str** |  | [optional] 
**zone** | **str** |  | [optional] 
**ips** | **List[str]** |  | [optional] 
**hostname** | **str** |  | [optional] 
**integration_id** | **int** |  | [optional] 
**org_id** | **int** |  | 
**settings** | [**ClusterSettings**](ClusterSettings.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print(Cluster.to_json())

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_from_dict = Cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


