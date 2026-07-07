# HelmChartServicePort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**number** | **int** |  | 
**target_port** | [**HelmChartServicePortTargetPort**](HelmChartServicePortTargetPort.md) |  | [optional] 
**protocol** | **str** |  | 

## Example

```python
from wodby.models.helm_chart_service_port import HelmChartServicePort

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartServicePort from a JSON string
helm_chart_service_port_instance = HelmChartServicePort.from_json(json)
# print the JSON string representation of the object
print(HelmChartServicePort.to_json())

# convert the object into a dict
helm_chart_service_port_dict = helm_chart_service_port_instance.to_dict()
# create an instance of HelmChartServicePort from a dict
helm_chart_service_port_from_dict = HelmChartServicePort.from_dict(helm_chart_service_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


