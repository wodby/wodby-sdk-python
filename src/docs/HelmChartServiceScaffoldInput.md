# HelmChartServiceScaffoldInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart** | [**HelmChartInput**](HelmChartInput.md) |  | 
**service_name** | **str** | Optional generated Wodby service name. | [optional] 
**service_title** | **str** | Optional generated Wodby service title. | [optional] 
**service_type** | **str** | Optional generated Wodby service type. Defaults to service. | [optional] 
**icon** | **str** | Optional generated service icon. | [optional] 

## Example

```python
from wodby.models.helm_chart_service_scaffold_input import HelmChartServiceScaffoldInput

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartServiceScaffoldInput from a JSON string
helm_chart_service_scaffold_input_instance = HelmChartServiceScaffoldInput.from_json(json)
# print the JSON string representation of the object
print(HelmChartServiceScaffoldInput.to_json())

# convert the object into a dict
helm_chart_service_scaffold_input_dict = helm_chart_service_scaffold_input_instance.to_dict()
# create an instance of HelmChartServiceScaffoldInput from a dict
helm_chart_service_scaffold_input_from_dict = HelmChartServiceScaffoldInput.from_dict(helm_chart_service_scaffold_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


