# Database


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**kind** | **str** |  | 
**status** | **str** |  | 
**version** | **str** |  | 
**region** | **str** |  | [optional] 
**zone** | **str** |  | [optional] 
**replicas** | **int** |  | [optional] 
**storage_size** | **int** | Storage size in GB. Null when the database does not set one. | [optional] 
**storage_iops** | **int** | Provisioned storage IOPS. Null when the database does not set them. | [optional] 
**machine_type** | **str** |  | [optional] 
**high_availability** | **bool** |  | [optional] 
**external** | **bool** | True for a database that runs outside Wodby, such as a provider-managed database server. | [optional] 
**external_id** | **str** | The database&#39;s ID at its provider. | [optional] 
**ssl** | **bool** | True when connections to the database use TLS. | [optional] 
**public_host** | **str** | Host name for connections from outside the database&#39;s network. Null when the database has none. | [optional] 
**public_port** | **int** |  | [optional] 
**private_host** | **str** | Host name for connections from inside the database&#39;s network. | [optional] 
**cluster_id** | **int** | The cluster that runs the database. | [optional] 
**resided_cluster_id** | **int** | The cluster whose network a provider-managed database is placed in. | [optional] 
**integration_id** | **int** |  | [optional] 
**app_service_id** | **int** |  | [optional] 
**ownership_scope** | **str** | org when the organization owns the resource, project when one project owns it. | 
**owner_project_id** | **int** |  | [optional] 
**env_id** | **int** | Legacy internal environment entity ID. Use envType. | 
**env_type** | **str** |  | 
**org_id** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from wodby.models.database import Database

# TODO update the JSON string below
json = "{}"
# create an instance of Database from a JSON string
database_instance = Database.from_json(json)
# print the JSON string representation of the object
print(Database.to_json())

# convert the object into a dict
database_dict = database_instance.to_dict()
# create an instance of Database from a dict
database_from_dict = Database.from_dict(database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


