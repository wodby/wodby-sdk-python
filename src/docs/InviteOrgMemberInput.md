# InviteOrgMemberInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**email** | **str** |  | 
**role** | **str** |  | 
**team_ids** | **List[int]** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 

## Example

```python
from wodby.models.invite_org_member_input import InviteOrgMemberInput

# TODO update the JSON string below
json = "{}"
# create an instance of InviteOrgMemberInput from a JSON string
invite_org_member_input_instance = InviteOrgMemberInput.from_json(json)
# print the JSON string representation of the object
print(InviteOrgMemberInput.to_json())

# convert the object into a dict
invite_org_member_input_dict = invite_org_member_input_instance.to_dict()
# create an instance of InviteOrgMemberInput from a dict
invite_org_member_input_from_dict = InviteOrgMemberInput.from_dict(invite_org_member_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


