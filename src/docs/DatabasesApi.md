# wodby.DatabasesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_database**](DatabasesApi.md#create_database) | **POST** /databases | Create database
[**create_database_db**](DatabasesApi.md#create_database_db) | **POST** /database-dbs | Create database DB
[**create_database_user**](DatabasesApi.md#create_database_user) | **POST** /database-users | Create database user
[**delete_database**](DatabasesApi.md#delete_database) | **DELETE** /databases/{id} | Delete database
[**delete_database_db**](DatabasesApi.md#delete_database_db) | **DELETE** /database-dbs/{id} | Delete database DB
[**delete_database_user**](DatabasesApi.md#delete_database_user) | **DELETE** /database-users/{id} | Delete database user
[**get_database**](DatabasesApi.md#get_database) | **GET** /databases/{id} | Get database
[**get_database_by_name**](DatabasesApi.md#get_database_by_name) | **GET** /databases/by-name/{name} | Get database by name
[**get_database_db**](DatabasesApi.md#get_database_db) | **GET** /database-dbs/{id} | Get database DB
[**list_database_charsets**](DatabasesApi.md#list_database_charsets) | **GET** /databases/{id}/options/charsets | List database charsets
[**list_database_dbs**](DatabasesApi.md#list_database_dbs) | **GET** /database-dbs | List database DBs
[**list_database_users**](DatabasesApi.md#list_database_users) | **GET** /database-users | List database users
[**list_databases**](DatabasesApi.md#list_databases) | **GET** /databases | List databases
[**update_database**](DatabasesApi.md#update_database) | **PUT** /databases/{id} | Update database
[**update_database_user_dbs**](DatabasesApi.md#update_database_user_dbs) | **PUT** /database-users/{id}/dbs | Update database user DB grants


# **create_database**
> Database create_database(new_database_input)

Create database

Creates a database and returns the created resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database import Database
from wodby.models.new_database_input import NewDatabaseInput
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
    api_instance = wodby.DatabasesApi(api_client)
    new_database_input = wodby.NewDatabaseInput() # NewDatabaseInput | 

    try:
        # Create database
        api_response = api_instance.create_database(new_database_input)
        print("The response of DatabasesApi->create_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->create_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_database_input** | [**NewDatabaseInput**](NewDatabaseInput.md)|  | 

### Return type

[**Database**](Database.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created database |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_database_db**
> DatabaseDB create_database_db(new_database_db_input)

Create database DB

Creates a DB inside a database.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database_db import DatabaseDB
from wodby.models.new_database_db_input import NewDatabaseDBInput
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
    api_instance = wodby.DatabasesApi(api_client)
    new_database_db_input = wodby.NewDatabaseDBInput() # NewDatabaseDBInput | 

    try:
        # Create database DB
        api_response = api_instance.create_database_db(new_database_db_input)
        print("The response of DatabasesApi->create_database_db:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->create_database_db: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_database_db_input** | [**NewDatabaseDBInput**](NewDatabaseDBInput.md)|  | 

### Return type

[**DatabaseDB**](DatabaseDB.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created database DB |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_database_user**
> DatabaseUser create_database_user(new_database_user_input)

Create database user

Creates a database user and optionally grants it access to DBs.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database_user import DatabaseUser
from wodby.models.new_database_user_input import NewDatabaseUserInput
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
    api_instance = wodby.DatabasesApi(api_client)
    new_database_user_input = wodby.NewDatabaseUserInput() # NewDatabaseUserInput | 

    try:
        # Create database user
        api_response = api_instance.create_database_user(new_database_user_input)
        print("The response of DatabasesApi->create_database_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->create_database_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_database_user_input** | [**NewDatabaseUserInput**](NewDatabaseUserInput.md)|  | 

### Return type

[**DatabaseUser**](DatabaseUser.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created database user |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database**
> OperationResult delete_database(id)

Delete database

Deletes the database and returns the operation result.

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
    api_instance = wodby.DatabasesApi(api_client)
    id = 56 # int | 

    try:
        # Delete database
        api_response = api_instance.delete_database(id)
        print("The response of DatabasesApi->delete_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database_db**
> OperationResult delete_database_db(id)

Delete database DB

Deletes a database DB and returns the operation result.

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
    api_instance = wodby.DatabasesApi(api_client)
    id = 56 # int | 

    try:
        # Delete database DB
        api_response = api_instance.delete_database_db(id)
        print("The response of DatabasesApi->delete_database_db:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database_db: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database_user**
> OperationResult delete_database_user(id)

Delete database user

Deletes a database user and returns the operation result.

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
    api_instance = wodby.DatabasesApi(api_client)
    id = 56 # int | 

    try:
        # Delete database user
        api_response = api_instance.delete_database_user(id)
        print("The response of DatabasesApi->delete_database_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database_user: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete result |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database**
> Database get_database(id)

Get database

Returns the database identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database import Database
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
    api_instance = wodby.DatabasesApi(api_client)
    id = 56 # int | 

    try:
        # Get database
        api_response = api_instance.get_database(id)
        print("The response of DatabasesApi->get_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Database**](Database.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_by_name**
> Database get_database_by_name(name, org_id=org_id)

Get database by name

Returns the database identified by name.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database import Database
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
    api_instance = wodby.DatabasesApi(api_client)
    name = 'name_example' # str | 
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)

    try:
        # Get database by name
        api_response = api_instance.get_database_by_name(name, org_id=org_id)
        print("The response of DatabasesApi->get_database_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 

### Return type

[**Database**](Database.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_db**
> DatabaseDB get_database_db(id)

Get database DB

Returns the database DB identified by the request path.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database_db import DatabaseDB
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
    api_instance = wodby.DatabasesApi(api_client)
    id = 56 # int | 

    try:
        # Get database DB
        api_response = api_instance.get_database_db(id)
        print("The response of DatabasesApi->get_database_db:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_db: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DatabaseDB**](DatabaseDB.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database DB |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_database_charsets**
> List[DatabaseCharset] list_database_charsets(id)

List database charsets

Returns charset and default collation options supported by a database.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database_charset import DatabaseCharset
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
    api_instance = wodby.DatabasesApi(api_client)
    id = 56 # int | 

    try:
        # List database charsets
        api_response = api_instance.list_database_charsets(id)
        print("The response of DatabasesApi->list_database_charsets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->list_database_charsets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[DatabaseCharset]**](DatabaseCharset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of database charsets |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_database_dbs**
> List[DatabaseDB] list_database_dbs(database_id)

List database DBs

Returns DBs that belong to a database.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database_db import DatabaseDB
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
    api_instance = wodby.DatabasesApi(api_client)
    database_id = 56 # int | 

    try:
        # List database DBs
        api_response = api_instance.list_database_dbs(database_id)
        print("The response of DatabasesApi->list_database_dbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->list_database_dbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **int**|  | 

### Return type

[**List[DatabaseDB]**](DatabaseDB.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of database DBs |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_database_users**
> List[DatabaseUser] list_database_users(database_id)

List database users

Returns users that belong to a database without revealing passwords.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database_user import DatabaseUser
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
    api_instance = wodby.DatabasesApi(api_client)
    database_id = 56 # int | 

    try:
        # List database users
        api_response = api_instance.list_database_users(database_id)
        print("The response of DatabasesApi->list_database_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->list_database_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **int**|  | 

### Return type

[**List[DatabaseUser]**](DatabaseUser.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of database users |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_databases**
> List[Database] list_databases(org_id=org_id, project_ids=project_ids, kind=kind)

List databases

Returns databases matching the request filters.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database import Database
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
    api_instance = wodby.DatabasesApi(api_client)
    org_id = 56 # int | Optional for API-key requests; defaults to the API key's organization. If provided, it must match the key's organization. (optional)
    project_ids = 'project_ids_example' # str | Comma-separated project ids (optional)
    kind = 'kind_example' # str |  (optional)

    try:
        # List databases
        api_response = api_instance.list_databases(org_id=org_id, project_ids=project_ids, kind=kind)
        print("The response of DatabasesApi->list_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->list_databases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| Optional for API-key requests; defaults to the API key&#39;s organization. If provided, it must match the key&#39;s organization. | [optional] 
 **project_ids** | **str**| Comma-separated project ids | [optional] 
 **kind** | **str**|  | [optional] 

### Return type

[**List[Database]**](Database.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of databases |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database**
> Database update_database(id, update_title_request)

Update database

Updates the database and returns the updated resource.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database import Database
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
    api_instance = wodby.DatabasesApi(api_client)
    id = 56 # int | 
    update_title_request = wodby.UpdateTitleRequest() # UpdateTitleRequest | 

    try:
        # Update database
        api_response = api_instance.update_database(id, update_title_request)
        print("The response of DatabasesApi->update_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->update_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_title_request** | [**UpdateTitleRequest**](UpdateTitleRequest.md)|  | 

### Return type

[**Database**](Database.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated database |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_user_dbs**
> DatabaseUser update_database_user_dbs(id, update_database_user_dbs_input)

Update database user DB grants

Replaces the DB grants for a database user.

### Example

* Api Key Authentication (apiKeyHeader):

```python
import wodby
from wodby.models.database_user import DatabaseUser
from wodby.models.update_database_user_dbs_input import UpdateDatabaseUserDBsInput
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
    api_instance = wodby.DatabasesApi(api_client)
    id = 56 # int | 
    update_database_user_dbs_input = wodby.UpdateDatabaseUserDBsInput() # UpdateDatabaseUserDBsInput | 

    try:
        # Update database user DB grants
        api_response = api_instance.update_database_user_dbs(id, update_database_user_dbs_input)
        print("The response of DatabasesApi->update_database_user_dbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->update_database_user_dbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_database_user_dbs_input** | [**UpdateDatabaseUserDBsInput**](UpdateDatabaseUserDBsInput.md)|  | 

### Return type

[**DatabaseUser**](DatabaseUser.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated database user |  -  |
**4XX** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

