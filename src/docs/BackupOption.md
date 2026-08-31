# BackupOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**values** | **List[str]** |  | 

## Example

```python
from wodby.models.backup_option import BackupOption

# TODO update the JSON string below
json = "{}"
# create an instance of BackupOption from a JSON string
backup_option_instance = BackupOption.from_json(json)
# print the JSON string representation of the object
print(BackupOption.to_json())

# convert the object into a dict
backup_option_dict = backup_option_instance.to_dict()
# create an instance of BackupOption from a dict
backup_option_from_dict = BackupOption.from_dict(backup_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


