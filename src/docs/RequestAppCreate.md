# RequestAppCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | 
**title** | **str** |  | [optional] 
**name** | **str** |  | 
**stack_id** | **str** |  | 
**docroot** | **str** |  | [optional] 
**sitename** | **str** |  | [optional] 
**server_id** | **str** |  | 
**instance_type** | [**InstanceType**](InstanceType.md) |  | [optional] 
**instance_name** | **str** |  | [optional] 
**instance_title** | **str** |  | [optional] 
**services** | [**list[RequestAppCreateServices]**](RequestAppCreateServices.md) |  | [optional] 
**deployment_type** | **str** |  | [optional] [default to 'vanilla']
**post_deployment** | **bool** |  | [optional] 
**git** | [**RequestAppCreateGit**](RequestAppCreateGit.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


