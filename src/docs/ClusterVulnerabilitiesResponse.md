# ClusterVulnerabilitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ClusterVulnerability]**](ClusterVulnerability.md) |  | 
**total_count** | **int** |  | 
**next_page** | **int** |  | [optional] 
**counts** | [**VulnerabilityCounts**](VulnerabilityCounts.md) |  | 
**sources** | [**List[ClusterVulnerabilitySource]**](ClusterVulnerabilitySource.md) |  | 

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


