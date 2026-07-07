# HelmChartContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**image** | **str** |  | [optional] 
**command** | **List[str]** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**ports** | [**List[HelmChartContainerPort]**](HelmChartContainerPort.md) |  | [optional] 
**env** | **List[str]** |  | [optional] 

## Example

```python
from wodby.models.helm_chart_container import HelmChartContainer

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartContainer from a JSON string
helm_chart_container_instance = HelmChartContainer.from_json(json)
# print the JSON string representation of the object
print(HelmChartContainer.to_json())

# convert the object into a dict
helm_chart_container_dict = helm_chart_container_instance.to_dict()
# create an instance of HelmChartContainer from a dict
helm_chart_container_from_dict = HelmChartContainer.from_dict(helm_chart_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


