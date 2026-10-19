# TeamInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | Used when creating a team. Optional for API-key requests; defaults to the API key&#39;s organization. | [optional] 
**name** | **str** |  | 
**title** | **str** |  | 
**members** | [**List[TeamMemberInput]**](TeamMemberInput.md) | The complete member list. | 

## Example

```python
from wodby.models.team_input import TeamInput

# TODO update the JSON string below
json = "{}"
# create an instance of TeamInput from a JSON string
team_input_instance = TeamInput.from_json(json)
# print the JSON string representation of the object
print(TeamInput.to_json())

# convert the object into a dict
team_input_dict = team_input_instance.to_dict()
# create an instance of TeamInput from a dict
team_input_from_dict = TeamInput.from_dict(team_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


