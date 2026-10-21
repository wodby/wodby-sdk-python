# ServiceExcludedBaseVersion

Set for an inherited service revision whose base service has a newer version than its fromVersionConstraint, or its exact fromVersion, allows. Raising the constraint in the inherited service's manifest lets it use that version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_service_revision_id** | **int** |  | 
**base_service_name** | **str** |  | 
**base_service_version** | **str** | The base service&#39;s newest version, which the inherited revision does not allow. | 
**base_service_rev_number** | **int** |  | 
**current_version** | **str** | The base service version this revision was built from. | 
**from_version_constraint** | **str** | The inherited manifest&#39;s fromVersionConstraint. Absent when the manifest pins an exact fromVersion. | [optional] 

## Example

```python
from wodby.models.service_excluded_base_version import ServiceExcludedBaseVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceExcludedBaseVersion from a JSON string
service_excluded_base_version_instance = ServiceExcludedBaseVersion.from_json(json)
# print the JSON string representation of the object
print(ServiceExcludedBaseVersion.to_json())

# convert the object into a dict
service_excluded_base_version_dict = service_excluded_base_version_instance.to_dict()
# create an instance of ServiceExcludedBaseVersion from a dict
service_excluded_base_version_from_dict = ServiceExcludedBaseVersion.from_dict(service_excluded_base_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


