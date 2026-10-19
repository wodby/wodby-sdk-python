# BackupDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from wodby.models.backup_download import BackupDownload

# TODO update the JSON string below
json = "{}"
# create an instance of BackupDownload from a JSON string
backup_download_instance = BackupDownload.from_json(json)
# print the JSON string representation of the object
print(BackupDownload.to_json())

# convert the object into a dict
backup_download_dict = backup_download_instance.to_dict()
# create an instance of BackupDownload from a dict
backup_download_from_dict = BackupDownload.from_dict(backup_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


