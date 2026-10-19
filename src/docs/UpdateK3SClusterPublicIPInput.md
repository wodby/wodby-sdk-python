# UpdateK3SClusterPublicIPInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_ip** | **str** |  | 

## Example

```python
from wodby.models.update_k3_s_cluster_public_ip_input import UpdateK3SClusterPublicIPInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateK3SClusterPublicIPInput from a JSON string
update_k3_s_cluster_public_ip_input_instance = UpdateK3SClusterPublicIPInput.from_json(json)
# print the JSON string representation of the object
print(UpdateK3SClusterPublicIPInput.to_json())

# convert the object into a dict
update_k3_s_cluster_public_ip_input_dict = update_k3_s_cluster_public_ip_input_instance.to_dict()
# create an instance of UpdateK3SClusterPublicIPInput from a dict
update_k3_s_cluster_public_ip_input_from_dict = UpdateK3SClusterPublicIPInput.from_dict(update_k3_s_cluster_public_ip_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


