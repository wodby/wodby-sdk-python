# AppEnvironmentStackUpgradeChangelog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_stack_version** | **str** |  | 
**stack_version** | **str** |  | 
**previous_stack_rev_number** | **int** |  | 
**stack_rev_number** | **int** |  | 
**service_changes** | [**List[ServiceRevisionChange]**](ServiceRevisionChange.md) |  | 

## Example

```python
from wodby.models.app_environment_stack_upgrade_changelog import AppEnvironmentStackUpgradeChangelog

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentStackUpgradeChangelog from a JSON string
app_environment_stack_upgrade_changelog_instance = AppEnvironmentStackUpgradeChangelog.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentStackUpgradeChangelog.to_json())

# convert the object into a dict
app_environment_stack_upgrade_changelog_dict = app_environment_stack_upgrade_changelog_instance.to_dict()
# create an instance of AppEnvironmentStackUpgradeChangelog from a dict
app_environment_stack_upgrade_changelog_from_dict = AppEnvironmentStackUpgradeChangelog.from_dict(app_environment_stack_upgrade_changelog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


