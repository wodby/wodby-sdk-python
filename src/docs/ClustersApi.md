# wodby.ClustersApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](ClustersApi.md#create_cluster) | **POST** /clusters | Create cluster
[**create_k3_s_cluster**](ClustersApi.md#create_k3_s_cluster) | **POST** /clusters/actions/create-k3s | Create k3s cluster
[**create_wodby_cloud_cluster**](ClustersApi.md#create_wodby_cloud_cluster) | **POST** /clusters/actions/create-wodby-cloud | Create Wodby Cloud cluster
[**delete_cluster**](ClustersApi.md#delete_cluster) | **DELETE** /clusters/{id} | Delete cluster
[**get_cluster**](ClustersApi.md#get_cluster) | **GET** /clusters/{id} | Get cluster
[**get_cluster_by_name**](ClustersApi.md#get_cluster_by_name) | **GET** /clusters/by-name/{name} | Get cluster by name
[**get_cluster_infra_app_upgrade_changelog**](ClustersApi.md#get_cluster_infra_app_upgrade_changelog) | **GET** /cluster-infra-app-upgrade-changelogs/{id} | Preview cluster infrastructure app upgrades
[**get_cluster_sharing**](ClustersApi.md#get_cluster_sharing) | **GET** /clusters/sharing/{id} | Get cluster sharing
[**get_k3_s_cluster_install_command**](ClustersApi.md#get_k3_s_cluster_install_command) | **GET** /clusters/k3s-install-command/{id} | Get k3s install command
[**get_kubernetes_version_upgrade_plan**](ClustersApi.md#get_kubernetes_version_upgrade_plan) | **GET** /cluster-kubernetes-version-upgrade-plans/{id} | Get Kubernetes version upgrade plan
[**list_clusters**](ClustersApi.md#list_clusters) | **GET** /clusters | List clusters
[**list_wodby_cloud_machine_types**](ClustersApi.md#list_wodby_cloud_machine_types) | **GET** /wodby-cloud/machine-types | List Wodby Cloud machine types
[**recycle_cluster_nodes**](ClustersApi.md#recycle_cluster_nodes) | **POST** /clusters/{id}/actions/recycle-nodes | Recycle cluster nodes
[**scale_cluster**](ClustersApi.md#scale_cluster) | **POST** /clusters/{id}/actions/scale | Scale cluster nodes
[**update_cluster**](ClustersApi.md#update_cluster) | **PUT** /clusters/{id} | Update cluster
[**update_cluster_environment_policy**](ClustersApi.md#update_cluster_environment_policy) | **PUT** /clusters/environment-policy/{id} | Update cluster environment policy
[**update_cluster_gpu_node_pool**](ClustersApi.md#update_cluster_gpu_node_pool) | **POST** /clusters/{id}/actions/gpu-node-pool | Update the GPU node pool
[**update_cluster_kubernetes_version**](ClustersApi.md#update_cluster_kubernetes_version) | **POST** /clusters/{id}/actions/update-kubernetes-version | Update cluster Kubernetes version
[**update_cluster_settings**](ClustersApi.md#update_cluster_settings) | **PUT** /clusters/settings/{id} | Update cluster settings
[**update_cluster_sharing**](ClustersApi.md#update_cluster_sharing) | **PUT** /clusters/sharing/{id} | Update cluster sharing
[**update_k3_s_cluster_public_ip**](ClustersApi.md#update_k3_s_cluster_public_ip) | **POST** /clusters/{id}/actions/update-k3s-public-ip | Update k3s cluster public IP
[**upgrade_cluster_infra**](ClustersApi.md#upgrade_cluster_infra) | **POST** /clusters/{id}/actions/upgrade-infra | Upgrade cluster infrastructure
[**upgrade_cluster_infra_apps**](ClustersApi.md#upgrade_cluster_infra_apps) | **POST** /clusters/{id}/actions/upgrade-infra-apps | Upgrade cluster infrastructure app stacks


# **create_cluster**
> Cluster create_cluster(new_cluster_input)

Create cluster

Creates a cluster and returns the created resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster import Cluster
from wodby.models.new_cluster_input import NewClusterInput
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    new_cluster_input = wodby.NewClusterInput() # NewClusterInput | 

    try:
        # Create cluster
        api_response = api_instance.create_cluster(new_cluster_input)
        print("The response of ClustersApi->create_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_cluster_input** | [**NewClusterInput**](NewClusterInput.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created cluster |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_k3_s_cluster**
> Cluster create_k3_s_cluster(new_k3_s_cluster_input)

Create k3s cluster

Registers a self-hosted k3s cluster. Run the command from GET /clusters/k3s-install-command/{id} on the server to connect it.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster import Cluster
from wodby.models.new_k3_s_cluster_input import NewK3SClusterInput
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    new_k3_s_cluster_input = wodby.NewK3SClusterInput() # NewK3SClusterInput | 

    try:
        # Create k3s cluster
        api_response = api_instance.create_k3_s_cluster(new_k3_s_cluster_input)
        print("The response of ClustersApi->create_k3_s_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_k3_s_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_k3_s_cluster_input** | [**NewK3SClusterInput**](NewK3SClusterInput.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created cluster |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wodby_cloud_cluster**
> ClusterCreationResult create_wodby_cloud_cluster(new_wodby_cloud_cluster_input)

Create Wodby Cloud cluster

Creates a cluster hosted by Wodby and billed to the organization. List machine types with GET /wodby- cloud/machine-types.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster_creation_result import ClusterCreationResult
from wodby.models.new_wodby_cloud_cluster_input import NewWodbyCloudClusterInput
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    new_wodby_cloud_cluster_input = wodby.NewWodbyCloudClusterInput() # NewWodbyCloudClusterInput | 

    try:
        # Create Wodby Cloud cluster
        api_response = api_instance.create_wodby_cloud_cluster(new_wodby_cloud_cluster_input)
        print("The response of ClustersApi->create_wodby_cloud_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_wodby_cloud_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_wodby_cloud_cluster_input** | [**NewWodbyCloudClusterInput**](NewWodbyCloudClusterInput.md)|  | 

### Return type

[**ClusterCreationResult**](ClusterCreationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created cluster and its provisioning task |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> OperationResult delete_cluster(id, force=force)

Delete cluster

Deletes the cluster and returns the operation result.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 
    force = False # bool |  (optional) (default to False)

    try:
        # Delete cluster
        api_response = api_instance.delete_cluster(id, force=force)
        print("The response of ClustersApi->delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **force** | **bool**|  | [optional] [default to False]

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> Cluster get_cluster(id)

Get cluster

Returns the cluster identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster import Cluster
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 

    try:
        # Get cluster
        api_response = api_instance.get_cluster(id)
        print("The response of ClustersApi->get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_by_name**
> Cluster get_cluster_by_name(name, org_id=org_id)

Get cluster by name

Returns the cluster identified by name.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster import Cluster
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    name = 'name_example' # str | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Get cluster by name
        api_response = api_instance.get_cluster_by_name(name, org_id=org_id)
        print("The response of ClustersApi->get_cluster_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_infra_app_upgrade_changelog**
> List[ClusterInfraAppUpgradeChangelog] get_cluster_infra_app_upgrade_changelog(id, app_instance_id=app_instance_id)

Preview cluster infrastructure app upgrades

Returns stack and service revision changes for infrastructure apps on the cluster.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster_infra_app_upgrade_changelog import ClusterInfraAppUpgradeChangelog
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 
    app_instance_id = 56 # int |  (optional)

    try:
        # Preview cluster infrastructure app upgrades
        api_response = api_instance.get_cluster_infra_app_upgrade_changelog(id, app_instance_id=app_instance_id)
        print("The response of ClustersApi->get_cluster_infra_app_upgrade_changelog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_infra_app_upgrade_changelog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **app_instance_id** | **int**|  | [optional] 

### Return type

[**List[ClusterInfraAppUpgradeChangelog]**](ClusterInfraAppUpgradeChangelog.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infrastructure app upgrade changelogs |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_sharing**
> ResourceSharing get_cluster_sharing(id)

Get cluster sharing

Returns who owns the cluster and which projects can use it.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.resource_sharing import ResourceSharing
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 

    try:
        # Get cluster sharing
        api_response = api_instance.get_cluster_sharing(id)
        print("The response of ClustersApi->get_cluster_sharing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_sharing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResourceSharing**](ResourceSharing.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster sharing |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_k3_s_cluster_install_command**
> K3SInstallCommand get_k3_s_cluster_install_command(id)

Get k3s install command

Returns the shell command that installs Wodby on the k3s server and connects the cluster. The command contains short-lived credentials; treat it as a secret.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.k3_s_install_command import K3SInstallCommand
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 

    try:
        # Get k3s install command
        api_response = api_instance.get_k3_s_cluster_install_command(id)
        print("The response of ClustersApi->get_k3_s_cluster_install_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_k3_s_cluster_install_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**K3SInstallCommand**](K3SInstallCommand.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Install command |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_version_upgrade_plan**
> KubernetesVersionUpgradePlan get_kubernetes_version_upgrade_plan(id)

Get Kubernetes version upgrade plan

Returns supported Kubernetes upgrade targets, blockers, and warnings for a cluster.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.kubernetes_version_upgrade_plan import KubernetesVersionUpgradePlan
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 

    try:
        # Get Kubernetes version upgrade plan
        api_response = api_instance.get_kubernetes_version_upgrade_plan(id)
        print("The response of ClustersApi->get_kubernetes_version_upgrade_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_kubernetes_version_upgrade_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**KubernetesVersionUpgradePlan**](KubernetesVersionUpgradePlan.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kubernetes version upgrade plan |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clusters**
> List[Cluster] list_clusters(org_id=org_id, project_ids=project_ids, integration_id=integration_id, environment_id=environment_id)

List clusters

Returns clusters matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster import Cluster
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    integration_id = 56 # int |  (optional)
    environment_id = 56 # int |  (optional)

    try:
        # List clusters
        api_response = api_instance.list_clusters(org_id=org_id, project_ids=project_ids, integration_id=integration_id, environment_id=environment_id)
        print("The response of ClustersApi->list_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 
 **project_ids** | **str**| Comma-separated project ids | [optional] 
 **integration_id** | **int**|  | [optional] 
 **environment_id** | **int**|  | [optional] 

### Return type

[**List[Cluster]**](Cluster.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wodby_cloud_machine_types**
> List[WodbyCloudMachineType] list_wodby_cloud_machine_types()

List Wodby Cloud machine types

Returns the machine types available for Wodby Cloud clusters with their prices.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.wodby_cloud_machine_type import WodbyCloudMachineType
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)

    try:
        # List Wodby Cloud machine types
        api_response = api_instance.list_wodby_cloud_machine_types()
        print("The response of ClustersApi->list_wodby_cloud_machine_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_wodby_cloud_machine_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WodbyCloudMachineType]**](WodbyCloudMachineType.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Machine types |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recycle_cluster_nodes**
> OperationResult recycle_cluster_nodes(id)

Recycle cluster nodes

Replaces the cluster nodes one at a time so they come back with a fresh machine image.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 

    try:
        # Recycle cluster nodes
        api_response = api_instance.recycle_cluster_nodes(id)
        print("The response of ClustersApi->recycle_cluster_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->recycle_cluster_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node recycling task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scale_cluster**
> OperationResult scale_cluster(id, scale_cluster_input)

Scale cluster nodes

Changes the minimum and maximum node count of a managed cluster and starts the node pool update.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.scale_cluster_input import ScaleClusterInput
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 
    scale_cluster_input = wodby.ScaleClusterInput() # ScaleClusterInput | 

    try:
        # Scale cluster nodes
        api_response = api_instance.scale_cluster(id, scale_cluster_input)
        print("The response of ClustersApi->scale_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->scale_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **scale_cluster_input** | [**ScaleClusterInput**](ScaleClusterInput.md)|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scaling task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster**
> Cluster update_cluster(id, update_title_request)

Update cluster

Updates the cluster and returns the updated resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster import Cluster
from wodby.models.update_title_request import UpdateTitleRequest
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 
    update_title_request = wodby.UpdateTitleRequest() # UpdateTitleRequest | 

    try:
        # Update cluster
        api_response = api_instance.update_cluster(id, update_title_request)
        print("The response of ClustersApi->update_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->update_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_title_request** | [**UpdateTitleRequest**](UpdateTitleRequest.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated cluster |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_environment_policy**
> Cluster update_cluster_environment_policy(id, cluster_environment_policy_input)

Update cluster environment policy

Updates the cluster's environment type and allowed environment-type scope. Scope reductions that conflict with existing non-infrastructure app environments are rejected.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster import Cluster
from wodby.models.cluster_environment_policy_input import ClusterEnvironmentPolicyInput
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 
    cluster_environment_policy_input = wodby.ClusterEnvironmentPolicyInput() # ClusterEnvironmentPolicyInput | 

    try:
        # Update cluster environment policy
        api_response = api_instance.update_cluster_environment_policy(id, cluster_environment_policy_input)
        print("The response of ClustersApi->update_cluster_environment_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->update_cluster_environment_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **cluster_environment_policy_input** | [**ClusterEnvironmentPolicyInput**](ClusterEnvironmentPolicyInput.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated cluster |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_gpu_node_pool**
> OperationResult update_cluster_gpu_node_pool(id, update_cluster_gpu_node_pool_input)

Update the GPU node pool

Adds, resizes, replaces or removes the cluster's optional GPU node pool. Pods that request GPUs are scheduled onto this pool. Set gpuNodePool to null to remove the pool; removal is refused while pods on the cluster request GPUs. Changing the machine type creates the new pool before the old one is deleted.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.update_cluster_gpu_node_pool_input import UpdateClusterGPUNodePoolInput
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 
    update_cluster_gpu_node_pool_input = wodby.UpdateClusterGPUNodePoolInput() # UpdateClusterGPUNodePoolInput | 

    try:
        # Update the GPU node pool
        api_response = api_instance.update_cluster_gpu_node_pool(id, update_cluster_gpu_node_pool_input)
        print("The response of ClustersApi->update_cluster_gpu_node_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->update_cluster_gpu_node_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_cluster_gpu_node_pool_input** | [**UpdateClusterGPUNodePoolInput**](UpdateClusterGPUNodePoolInput.md)|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GPU node pool task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_kubernetes_version**
> OperationResult update_cluster_kubernetes_version(id, update_kubernetes_version_input)

Update cluster Kubernetes version

Starts upgrading the cluster to a Kubernetes version from its upgrade plan. Check GET /cluster-kubernetes- version-upgrade-plans/{id} for the allowed targets first.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.models.update_kubernetes_version_input import UpdateKubernetesVersionInput
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 
    update_kubernetes_version_input = wodby.UpdateKubernetesVersionInput() # UpdateKubernetesVersionInput | 

    try:
        # Update cluster Kubernetes version
        api_response = api_instance.update_cluster_kubernetes_version(id, update_kubernetes_version_input)
        print("The response of ClustersApi->update_cluster_kubernetes_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->update_cluster_kubernetes_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_kubernetes_version_input** | [**UpdateKubernetesVersionInput**](UpdateKubernetesVersionInput.md)|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upgrade task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_settings**
> Cluster update_cluster_settings(id, cluster_settings_input)

Update cluster settings

Updates cluster settings and returns the updated cluster.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster import Cluster
from wodby.models.cluster_settings_input import ClusterSettingsInput
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 
    cluster_settings_input = wodby.ClusterSettingsInput() # ClusterSettingsInput | 

    try:
        # Update cluster settings
        api_response = api_instance.update_cluster_settings(id, cluster_settings_input)
        print("The response of ClustersApi->update_cluster_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->update_cluster_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **cluster_settings_input** | [**ClusterSettingsInput**](ClusterSettingsInput.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated cluster |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_sharing**
> ResourceSharing update_cluster_sharing(id, resource_sharing_input)

Update cluster sharing

Changes the cluster owner and replaces the projects it is shared with. It can also make an organization-owned cluster available to every project. Returns the resulting sharing.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.resource_sharing import ResourceSharing
from wodby.models.resource_sharing_input import ResourceSharingInput
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 
    resource_sharing_input = wodby.ResourceSharingInput() # ResourceSharingInput | 

    try:
        # Update cluster sharing
        api_response = api_instance.update_cluster_sharing(id, resource_sharing_input)
        print("The response of ClustersApi->update_cluster_sharing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->update_cluster_sharing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **resource_sharing_input** | [**ResourceSharingInput**](ResourceSharingInput.md)|  | 

### Return type

[**ResourceSharing**](ResourceSharing.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated cluster sharing |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_k3_s_cluster_public_ip**
> Cluster update_k3_s_cluster_public_ip(id, update_k3_s_cluster_public_ip_input)

Update k3s cluster public IP

Changes the public IP address that routes to a self-hosted k3s cluster. Returns the cluster.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.cluster import Cluster
from wodby.models.update_k3_s_cluster_public_ip_input import UpdateK3SClusterPublicIPInput
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 
    update_k3_s_cluster_public_ip_input = wodby.UpdateK3SClusterPublicIPInput() # UpdateK3SClusterPublicIPInput | 

    try:
        # Update k3s cluster public IP
        api_response = api_instance.update_k3_s_cluster_public_ip(id, update_k3_s_cluster_public_ip_input)
        print("The response of ClustersApi->update_k3_s_cluster_public_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->update_k3_s_cluster_public_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_k3_s_cluster_public_ip_input** | [**UpdateK3SClusterPublicIPInput**](UpdateK3SClusterPublicIPInput.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated cluster |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_cluster_infra**
> OperationResult upgrade_cluster_infra(id)

Upgrade cluster infrastructure

Starts a cluster infrastructure upgrade task and returns the task identifier.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 

    try:
        # Upgrade cluster infrastructure
        api_response = api_instance.upgrade_cluster_infra(id)
        print("The response of ClustersApi->upgrade_cluster_infra:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->upgrade_cluster_infra: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upgrade task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_cluster_infra_apps**
> OperationResult upgrade_cluster_infra_apps(id)

Upgrade cluster infrastructure app stacks

Starts a cluster infrastructure app stack upgrade task and returns the task identifier.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.operation_result import OperationResult
from wodby.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wodby.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with wodby.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wodby.ClustersApi(api_client)
    id = 56 # int | 

    try:
        # Upgrade cluster infrastructure app stacks
        api_response = api_instance.upgrade_cluster_infra_apps(id)
        print("The response of ClustersApi->upgrade_cluster_infra_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->upgrade_cluster_infra_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upgrade task result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

