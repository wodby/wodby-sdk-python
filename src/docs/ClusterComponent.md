# ClusterComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **str** | The image tag or reported version as published; empty for an image referenced only by digest. | 
**source** | **str** |  | 
**manager** | **str** | Who can update the component. wodby is installed by Wodby outside an app, such as Cilium on K3S; infra_app runs in an infrastructure app; k3s comes with the K3S release; provider is run by the managed Kubernetes provider; host is the operating system of a server you run; and other was installed outside Wodby or is not recognized. | 
**namespace** | **str** | Empty for node components, as are workloadKind, workload, container, image and imageDigest. | 
**workload_kind** | **str** |  | 
**workload** | **str** |  | 
**container** | **str** | Container names, separated by commas when a workload runs several from one image. | 
**image** | **str** |  | 
**image_digest** | **str** |  | 
**count** | **int** | Running pods, or nodes for a node component. | 
**observed_at** | **datetime** |  | 
**status** | **str** | Whether the component needs anything. update_available means Wodby can apply a newer version, and latestVersion and updatePath say which version and how. bundled follows the cluster&#39;s Kubernetes version, infra_app is reported by its infrastructure app, and unknown means the check could not run or Wodby has nothing to offer. | 
**latest_version** | **str** | The version an available update would apply. | [optional] 
**update_path** | **str** | The operation that updates the component. | [optional] 

## Example

```python
from wodby.models.cluster_component import ClusterComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComponent from a JSON string
cluster_component_instance = ClusterComponent.from_json(json)
# print the JSON string representation of the object
print(ClusterComponent.to_json())

# convert the object into a dict
cluster_component_dict = cluster_component_instance.to_dict()
# create an instance of ClusterComponent from a dict
cluster_component_from_dict = ClusterComponent.from_dict(cluster_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


