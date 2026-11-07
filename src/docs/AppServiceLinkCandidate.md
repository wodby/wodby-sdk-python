# AppServiceLinkCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_id** | **int** |  | 
**app_service_name** | **str** |  | 
**app_service_title** | **str** |  | 
**cross_app** | **bool** | The candidate is in another app environment. | 
**app_id** | **int** |  | 
**app_title** | **str** |  | 
**app_instance_id** | **int** |  | 
**app_instance_title** | **str** |  | 

## Example

```python
from wodby.models.app_service_link_candidate import AppServiceLinkCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceLinkCandidate from a JSON string
app_service_link_candidate_instance = AppServiceLinkCandidate.from_json(json)
# print the JSON string representation of the object
print(AppServiceLinkCandidate.to_json())

# convert the object into a dict
app_service_link_candidate_dict = app_service_link_candidate_instance.to_dict()
# create an instance of AppServiceLinkCandidate from a dict
app_service_link_candidate_from_dict = AppServiceLinkCandidate.from_dict(app_service_link_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


