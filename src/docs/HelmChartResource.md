# HelmChartResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**api_version** | **str** |  | [optional] 
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 

## Example

```python
from wodby.models.helm_chart_resource import HelmChartResource

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartResource from a JSON string
helm_chart_resource_instance = HelmChartResource.from_json(json)
# print the JSON string representation of the object
print(HelmChartResource.to_json())

# convert the object into a dict
helm_chart_resource_dict = helm_chart_resource_instance.to_dict()
# create an instance of HelmChartResource from a dict
helm_chart_resource_from_dict = HelmChartResource.from_dict(helm_chart_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


