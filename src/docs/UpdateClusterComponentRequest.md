# UpdateClusterComponentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The update&#39;s name, as listed for the cluster. | 

## Example

```python
from wodby.models.update_cluster_component_request import UpdateClusterComponentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterComponentRequest from a JSON string
update_cluster_component_request_instance = UpdateClusterComponentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateClusterComponentRequest.to_json())

# convert the object into a dict
update_cluster_component_request_dict = update_cluster_component_request_instance.to_dict()
# create an instance of UpdateClusterComponentRequest from a dict
update_cluster_component_request_from_dict = UpdateClusterComponentRequest.from_dict(update_cluster_component_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


