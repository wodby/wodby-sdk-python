# UpdateStackServiceRevisionsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stack_service_ids** | **List[int]** | Root stack services to advance, by their IDs in the published revision or the draft. Their derivatives advance with them. Omit or leave empty to advance every outdated service. | [optional] 

## Example

```python
from wodby.models.update_stack_service_revisions_input import UpdateStackServiceRevisionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStackServiceRevisionsInput from a JSON string
update_stack_service_revisions_input_instance = UpdateStackServiceRevisionsInput.from_json(json)
# print the JSON string representation of the object
print(UpdateStackServiceRevisionsInput.to_json())

# convert the object into a dict
update_stack_service_revisions_input_dict = update_stack_service_revisions_input_instance.to_dict()
# create an instance of UpdateStackServiceRevisionsInput from a dict
update_stack_service_revisions_input_from_dict = UpdateStackServiceRevisionsInput.from_dict(update_stack_service_revisions_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


