# HelmChartAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart** | [**HelmChartMetadata**](HelmChartMetadata.md) |  | 
**release** | **str** |  | 
**namespace** | **str** |  | 
**resource_count** | **int** |  | 
**workloads** | [**List[HelmChartWorkload]**](HelmChartWorkload.md) |  | [optional] 
**services** | [**List[HelmChartService]**](HelmChartService.md) |  | [optional] 
**volume_claims** | [**List[HelmChartVolumeClaim]**](HelmChartVolumeClaim.md) |  | [optional] 
**crds** | [**List[HelmChartResource]**](HelmChartResource.md) |  | [optional] 
**cluster_resources** | [**List[HelmChartResource]**](HelmChartResource.md) |  | [optional] 
**hooks** | [**List[HelmChartResource]**](HelmChartResource.md) |  | [optional] 
**unsupported_kinds** | **List[str]** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from wodby.models.helm_chart_analysis import HelmChartAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartAnalysis from a JSON string
helm_chart_analysis_instance = HelmChartAnalysis.from_json(json)
# print the JSON string representation of the object
print(HelmChartAnalysis.to_json())

# convert the object into a dict
helm_chart_analysis_dict = helm_chart_analysis_instance.to_dict()
# create an instance of HelmChartAnalysis from a dict
helm_chart_analysis_from_dict = HelmChartAnalysis.from_dict(helm_chart_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


