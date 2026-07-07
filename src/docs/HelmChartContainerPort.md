# HelmChartContainerPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**number** | **int** |  | 
**protocol** | **str** |  | 

## Example

```python
from wodby.models.helm_chart_container_port import HelmChartContainerPort

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartContainerPort from a JSON string
helm_chart_container_port_instance = HelmChartContainerPort.from_json(json)
# print the JSON string representation of the object
print(HelmChartContainerPort.to_json())

# convert the object into a dict
helm_chart_container_port_dict = helm_chart_container_port_instance.to_dict()
# create an instance of HelmChartContainerPort from a dict
helm_chart_container_port_from_dict = HelmChartContainerPort.from_dict(helm_chart_container_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


