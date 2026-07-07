# HelmChartInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** | Optional chart source name to use in generated Wodby manifests. | [optional] 
**source** | **str** | Optional Helm repository or OCI source URL. | [optional] 
**chart** | **str** | Helm chart reference, such as bitnami/redis, oci://registry.example.com/chart, a chart archive URL, or a server-local chart path. | 
**version** | **str** | Optional Helm chart version. | [optional] 
**release** | **str** | Optional Helm release name used for rendering analysis. | [optional] 
**namespace** | **str** | Optional Kubernetes namespace used for rendering analysis. | [optional] 
**values** | **Dict[str, object]** |  | [optional] 
**values_yaml** | **str** | Optional Helm values YAML. Use either values or valuesYaml, not both. | [optional] 

## Example

```python
from wodby.models.helm_chart_input import HelmChartInput

# TODO update the JSON string below
json = "{}"
# create an instance of HelmChartInput from a JSON string
helm_chart_input_instance = HelmChartInput.from_json(json)
# print the JSON string representation of the object
print(HelmChartInput.to_json())

# convert the object into a dict
helm_chart_input_dict = helm_chart_input_instance.to_dict()
# create an instance of HelmChartInput from a dict
helm_chart_input_from_dict = HelmChartInput.from_dict(helm_chart_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


