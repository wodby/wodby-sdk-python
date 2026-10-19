# IgnoreStackServiceRevisionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stack_service_id** | **int** | Root stack service whose update to skip. Its derivatives skip it too. | 
**service_rev_id** | **int** | Service revision to stop offering. | 

## Example

```python
from wodby.models.ignore_stack_service_revision_input import IgnoreStackServiceRevisionInput

# TODO update the JSON string below
json = "{}"
# create an instance of IgnoreStackServiceRevisionInput from a JSON string
ignore_stack_service_revision_input_instance = IgnoreStackServiceRevisionInput.from_json(json)
# print the JSON string representation of the object
print(IgnoreStackServiceRevisionInput.to_json())

# convert the object into a dict
ignore_stack_service_revision_input_dict = ignore_stack_service_revision_input_instance.to_dict()
# create an instance of IgnoreStackServiceRevisionInput from a dict
ignore_stack_service_revision_input_from_dict = IgnoreStackServiceRevisionInput.from_dict(ignore_stack_service_revision_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


