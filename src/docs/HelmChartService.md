# HelmChartService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**labels** | **Dict[str, str]** |  | [optional] 
**selector** | **Dict[str, str]** |  | [optional] 
**ports** | [**List[HelmChartServicePort]**](HelmChartServicePort.md) |  | [optional] 
**headless** | **bool** |  | 

## Example

```python
from wodby.models.helm_chart_service import HelmChartService

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartService from a JSON string
helm_chart_service_instance = HelmChartService.from_json(json)
# print the JSON string representation of the object
print(HelmChartService.to_json())

# convert the object into a dict
helm_chart_service_dict = helm_chart_service_instance.to_dict()
# create an instance of HelmChartService from a dict
helm_chart_service_from_dict = HelmChartService.from_dict(helm_chart_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


