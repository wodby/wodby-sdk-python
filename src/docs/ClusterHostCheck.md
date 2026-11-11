# ClusterHostCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Identifies the check, such as ipv4_options_filter or mptcp_disabled. More checks may be added. | 
**title** | **str** |  | 
**advisory** | **str** | The security advisory the check protects against, such as CVE-2026-98432. Group checks by this field. | 
**advisory_title** | **str** | Describes the advisory, such as Linux kernel TCP bug. | 
**node** | **str** | The node that reported the check; empty when no node has reported. | 
**state** | **str** | Whether the protection is in place. unknown means the server hasn&#39;t reported the check, or its last report is more than two days old. | 
**message** | **str** | What the state means and what to do about it. | 
**kernel** | **str** | The kernel release the server ran at the check; empty when it hasn&#39;t reported. | 
**checked_at** | **datetime** | When the server ran the check. Absent when it hasn&#39;t reported. | [optional] 
**observed_at** | **datetime** | When Wodby read the report. Absent when the server hasn&#39;t reported. | [optional] 

## Example

```python
from wodby.models.cluster_host_check import ClusterHostCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterHostCheck from a JSON string
cluster_host_check_instance = ClusterHostCheck.from_json(json)
# print the JSON string representation of the object
print(ClusterHostCheck.to_json())

# convert the object into a dict
cluster_host_check_dict = cluster_host_check_instance.to_dict()
# create an instance of ClusterHostCheck from a dict
cluster_host_check_from_dict = ClusterHostCheck.from_dict(cluster_host_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


