# StackUpgradeVolumeDeletion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service_name** | **str** |  | 
**app_service_title** | **str** |  | 
**volume** | **str** |  | 
**service_removed** | **bool** | True when the target stack revision no longer has the app service&#39;s stack service, so the upgrade deletes the whole app service. False when the service no longer uses the volume. | 

## Example

```python
from wodby.models.stack_upgrade_volume_deletion import StackUpgradeVolumeDeletion

# TODO update the JSON string below
json = "{}"
# create an instance of StackUpgradeVolumeDeletion from a JSON string
stack_upgrade_volume_deletion_instance = StackUpgradeVolumeDeletion.from_json(json)
# print the JSON string representation of the object
print(StackUpgradeVolumeDeletion.to_json())

# convert the object into a dict
stack_upgrade_volume_deletion_dict = stack_upgrade_volume_deletion_instance.to_dict()
# create an instance of StackUpgradeVolumeDeletion from a dict
stack_upgrade_volume_deletion_from_dict = StackUpgradeVolumeDeletion.from_dict(stack_upgrade_volume_deletion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


