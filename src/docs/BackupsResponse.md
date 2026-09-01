# BackupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Backup]**](Backup.md) |  | 
**total_count** | **int** |  | 
**next_page** | **int** |  | [optional] 

## Example

```python
from wodby.models.backups_response import BackupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackupsResponse from a JSON string
backups_response_instance = BackupsResponse.from_json(json)
# print the JSON string representation of the object
print(BackupsResponse.to_json())

# convert the object into a dict
backups_response_dict = backups_response_instance.to_dict()
# create an instance of BackupsResponse from a dict
backups_response_from_dict = BackupsResponse.from_dict(backups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


