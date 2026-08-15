# ClusterInfraAppUpgradeChangelog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_instance_id** | **int** |  | 
**app_name** | **str** |  | 
**app_title** | **str** |  | 
**previous_stack_version** | **str** |  | 
**stack_version** | **str** |  | 
**previous_stack_rev_number** | **int** |  | 
**stack_rev_number** | **int** |  | 
**service_changes** | [**List[ServiceRevisionChange]**](ServiceRevisionChange.md) |  | 

## Example

```python
from wodby.models.cluster_infra_app_upgrade_changelog import ClusterInfraAppUpgradeChangelog

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInfraAppUpgradeChangelog from a JSON string
cluster_infra_app_upgrade_changelog_instance = ClusterInfraAppUpgradeChangelog.from_json(json)
# print the JSON string representation of the object
print(ClusterInfraAppUpgradeChangelog.to_json())

# convert the object into a dict
cluster_infra_app_upgrade_changelog_dict = cluster_infra_app_upgrade_changelog_instance.to_dict()
# create an instance of ClusterInfraAppUpgradeChangelog from a dict
cluster_infra_app_upgrade_changelog_from_dict = ClusterInfraAppUpgradeChangelog.from_dict(cluster_infra_app_upgrade_changelog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


