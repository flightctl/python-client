# flightctl.FleetApi

All URIs are relative to *https://raw.githubusercontent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fleet**](FleetApi.md#create_fleet) | **POST** /api/v1/fleets | 
[**delete_fleet**](FleetApi.md#delete_fleet) | **DELETE** /api/v1/fleets/{name} | 
[**delete_fleets**](FleetApi.md#delete_fleets) | **DELETE** /api/v1/fleets | 
[**list_fleets**](FleetApi.md#list_fleets) | **GET** /api/v1/fleets | 
[**patch_fleet**](FleetApi.md#patch_fleet) | **PATCH** /api/v1/fleets/{name} | 
[**read_fleet**](FleetApi.md#read_fleet) | **GET** /api/v1/fleets/{name} | 
[**read_fleet_status**](FleetApi.md#read_fleet_status) | **GET** /api/v1/fleets/{name}/status | 
[**replace_fleet**](FleetApi.md#replace_fleet) | **PUT** /api/v1/fleets/{name} | 
[**replace_fleet_status**](FleetApi.md#replace_fleet_status) | **PUT** /api/v1/fleets/{name}/status | 


# **create_fleet**
> Fleet create_fleet(fleet)



create a Fleet

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "https://raw.githubusercontent.com"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.FleetApi(api_client)
    fleet = flightctl.Fleet() # Fleet | 

    try:
        api_response = api_instance.create_fleet(fleet)
        print("The response of FleetApi->create_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->create_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet** | [**Fleet**](Fleet.md)|  | 

### Return type

[**Fleet**](Fleet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**409** | StatusConflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fleet**
> Fleet delete_fleet(name)



delete a Fleet

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "https://raw.githubusercontent.com"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | name of the Fleet

    try:
        api_response = api_instance.delete_fleet(name)
        print("The response of FleetApi->delete_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->delete_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Fleet | 

### Return type

[**Fleet**](Fleet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fleets**
> Status delete_fleets()



delete a collection of Fleets

### Example


```python
import flightctl
from flightctl.models.status import Status
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "https://raw.githubusercontent.com"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.FleetApi(api_client)

    try:
        api_response = api_instance.delete_fleets()
        print("The response of FleetApi->delete_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->delete_fleets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fleets**
> FleetList list_fleets(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, owner=owner, add_devices_count=add_devices_count, sort_by=sort_by, sort_order=sort_order)



list Fleets

### Example


```python
import flightctl
from flightctl.models.fleet_list import FleetList
from flightctl.models.sort_order import SortOrder
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "https://raw.githubusercontent.com"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.FleetApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supports '=', '==', and '!='.(e.g. key1=value1,key2!=value2). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)
    owner = 'owner_example' # str | A selector to restrict the list of returned objects by their owner. Defaults to everything. (optional)
    add_devices_count = True # bool | include the number of devices in each fleet (optional)
    sort_by = 'metadata.name' # str | Specifies the field to sort by. (optional)
    sort_order = Asc # SortOrder | Specifies the sort order. (optional) (default to Asc)

    try:
        api_response = api_instance.list_fleets(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, owner=owner, add_devices_count=add_devices_count, sort_by=sort_by, sort_order=sort_order)
        print("The response of FleetApi->list_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->list_fleets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supports &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39;.(e.g. key1&#x3D;value1,key2!&#x3D;value2). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 
 **owner** | **str**| A selector to restrict the list of returned objects by their owner. Defaults to everything. | [optional] 
 **add_devices_count** | **bool**| include the number of devices in each fleet | [optional] 
 **sort_by** | **str**| Specifies the field to sort by. | [optional] 
 **sort_order** | [**SortOrder**](.md)| Specifies the sort order. | [optional] [default to Asc]

### Return type

[**FleetList**](FleetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_fleet**
> Fleet patch_fleet(name, patch_request_inner=patch_request_inner)



Patches the specified fleet

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
from flightctl.models.patch_request_inner import PatchRequestInner
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "https://raw.githubusercontent.com"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | name of the fleet
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] |  (optional)

    try:
        api_response = api_instance.patch_fleet(name, patch_request_inner=patch_request_inner)
        print("The response of FleetApi->patch_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->patch_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the fleet | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | [optional] 

### Return type

[**Fleet**](Fleet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |
**409** | StatusConflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_fleet**
> Fleet read_fleet(name, add_devices_summary=add_devices_summary)



read the specified Fleet

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "https://raw.githubusercontent.com"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | unique name of the Fleet
    add_devices_summary = True # bool | include a summary of the devices in the fleet (optional)

    try:
        api_response = api_instance.read_fleet(name, add_devices_summary=add_devices_summary)
        print("The response of FleetApi->read_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->read_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| unique name of the Fleet | 
 **add_devices_summary** | **bool**| include a summary of the devices in the fleet | [optional] 

### Return type

[**Fleet**](Fleet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_fleet_status**
> Fleet read_fleet_status(name)



read status of the specified Fleet

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "https://raw.githubusercontent.com"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | name of the Fleet

    try:
        api_response = api_instance.read_fleet_status(name)
        print("The response of FleetApi->read_fleet_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->read_fleet_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Fleet | 

### Return type

[**Fleet**](Fleet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_fleet**
> Fleet replace_fleet(name, fleet)



replace the specified Fleet

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "https://raw.githubusercontent.com"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | name of the Fleet
    fleet = flightctl.Fleet() # Fleet | 

    try:
        api_response = api_instance.replace_fleet(name, fleet)
        print("The response of FleetApi->replace_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->replace_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Fleet | 
 **fleet** | [**Fleet**](Fleet.md)|  | 

### Return type

[**Fleet**](Fleet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_fleet_status**
> Fleet replace_fleet_status(name, fleet)



replace status of the specified Fleet

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://raw.githubusercontent.com
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "https://raw.githubusercontent.com"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | name of the Fleet
    fleet = flightctl.Fleet() # Fleet | 

    try:
        api_response = api_instance.replace_fleet_status(name, fleet)
        print("The response of FleetApi->replace_fleet_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->replace_fleet_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Fleet | 
 **fleet** | [**Fleet**](Fleet.md)|  | 

### Return type

[**Fleet**](Fleet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

