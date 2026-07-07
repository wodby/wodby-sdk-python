# HelmChartWorkload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**name** | **str** |  | 
**labels** | **Dict[str, str]** |  | [optional] 
**selector** | **Dict[str, str]** |  | [optional] 
**pod_labels** | **Dict[str, str]** |  | [optional] 
**containers** | [**List[HelmChartContainer]**](HelmChartContainer.md) |  | [optional] 
**init_containers** | [**List[HelmChartContainer]**](HelmChartContainer.md) |  | [optional] 
**volumes** | [**List[HelmChartVolumeClaim]**](HelmChartVolumeClaim.md) |  | [optional] 

## Example

```python
from wodby.models.helm_chart_workload import HelmChartWorkload

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartWorkload from a JSON string
helm_chart_workload_instance = HelmChartWorkload.from_json(json)
# print the JSON string representation of the object
print(HelmChartWorkload.to_json())

# convert the object into a dict
helm_chart_workload_dict = helm_chart_workload_instance.to_dict()
# create an instance of HelmChartWorkload from a dict
helm_chart_workload_from_dict = HelmChartWorkload.from_dict(helm_chart_workload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


