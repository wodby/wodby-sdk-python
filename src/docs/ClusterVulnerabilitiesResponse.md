# ClusterVulnerabilitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ClusterVulnerability]**](ClusterVulnerability.md) |  | 
**total_count** | **int** |  | 
**next_page** | **int** |  | [optional] 
**counts** | [**VulnerabilityCounts**](VulnerabilityCounts.md) |  | 
**sources** | [**List[ClusterVulnerabilitySource]**](ClusterVulnerabilitySource.md) |  | 
**scanning** | **bool** | Whether a vulnerability check of the cluster is waiting or running. Until it ends, the list shows the results of the checks that finished before it. | 
**restart_required** | **int** | The cluster&#39;s critical and high vulnerabilities, not ignored, that a restart of its K3s servers fixes: the fix is installed and runs after the restart. Covers the whole cluster, whatever the filter. | 
**waiting_for_upstream** | **int** | The cluster&#39;s critical and high vulnerabilities, not ignored, that wait for a fix from an infrastructure image&#39;s maintainers. They aren&#39;t in counts. Covers the whole cluster, whatever the filter. | 

## Example

```python
from wodby.models.cluster_vulnerabilities_response import ClusterVulnerabilitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVulnerabilitiesResponse from a JSON string
cluster_vulnerabilities_response_instance = ClusterVulnerabilitiesResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterVulnerabilitiesResponse.to_json())

# convert the object into a dict
cluster_vulnerabilities_response_dict = cluster_vulnerabilities_response_instance.to_dict()
# create an instance of ClusterVulnerabilitiesResponse from a dict
cluster_vulnerabilities_response_from_dict = ClusterVulnerabilitiesResponse.from_dict(cluster_vulnerabilities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


