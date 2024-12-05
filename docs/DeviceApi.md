# flightctl.DeviceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](DeviceApi.md#create_device) | **POST** /api/v1/devices | 
[**decommission_device**](DeviceApi.md#decommission_device) | **PUT** /api/v1/devices/{name}/decommission | 
[**delete_device**](DeviceApi.md#delete_device) | **DELETE** /api/v1/devices/{name} | 
[**delete_devices**](DeviceApi.md#delete_devices) | **DELETE** /api/v1/devices | 
[**get_rendered_device_spec**](DeviceApi.md#get_rendered_device_spec) | **GET** /api/v1/devices/{name}/rendered | 
[**list_devices**](DeviceApi.md#list_devices) | **GET** /api/v1/devices | 
[**patch_device**](DeviceApi.md#patch_device) | **PATCH** /api/v1/devices/{name} | 
[**read_device**](DeviceApi.md#read_device) | **GET** /api/v1/devices/{name} | 
[**read_device_status**](DeviceApi.md#read_device_status) | **GET** /api/v1/devices/{name}/status | 
[**replace_device**](DeviceApi.md#replace_device) | **PUT** /api/v1/devices/{name} | 
[**replace_device_status**](DeviceApi.md#replace_device_status) | **PUT** /api/v1/devices/{name}/status | 
[**request_console**](DeviceApi.md#request_console) | **GET** /api/v1/devices/{name}/console | 


# **create_device**
> Device create_device(device)



create a Device

### Example


```python
import flightctl
from flightctl.models.device import Device
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    device = flightctl.Device() # Device | 

    try:
        api_response = api_instance.create_device(device)
        print("The response of DeviceApi->create_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->create_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**Device**](Device.md)|  | 

### Return type

[**Device**](Device.md)

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

# **decommission_device**
> Device decommission_device(name, device_decommission)



schedule the device to decommission

### Example


```python
import flightctl
from flightctl.models.device import Device
from flightctl.models.device_decommission import DeviceDecommission
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | name of the Device
    device_decommission = flightctl.DeviceDecommission() # DeviceDecommission | 

    try:
        api_response = api_instance.decommission_device(name, device_decommission)
        print("The response of DeviceApi->decommission_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->decommission_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Device | 
 **device_decommission** | [**DeviceDecommission**](DeviceDecommission.md)|  | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> Device delete_device(name)



delete a Device

### Example


```python
import flightctl
from flightctl.models.device import Device
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | name of the Device

    try:
        api_response = api_instance.delete_device(name)
        print("The response of DeviceApi->delete_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Device | 

### Return type

[**Device**](Device.md)

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

# **delete_devices**
> Status delete_devices()



delete a collection of Devices

### Example


```python
import flightctl
from flightctl.models.status import Status
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)

    try:
        api_response = api_instance.delete_devices()
        print("The response of DeviceApi->delete_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_devices: %s\n" % e)
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

# **get_rendered_device_spec**
> RenderedDeviceSpec get_rendered_device_spec(name, known_rendered_version=known_rendered_version)



get the full specification for the specified device

### Example


```python
import flightctl
from flightctl.models.rendered_device_spec import RenderedDeviceSpec
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | Name of the device
    known_rendered_version = 'known_rendered_version_example' # str | The last known renderedVersion (optional)

    try:
        api_response = api_instance.get_rendered_device_spec(name, known_rendered_version=known_rendered_version)
        print("The response of DeviceApi->get_rendered_device_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_rendered_device_spec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the device | 
 **known_rendered_version** | **str**| The last known renderedVersion | [optional] 

### Return type

[**RenderedDeviceSpec**](RenderedDeviceSpec.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No content |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |
**409** | StatusConflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices**
> DeviceList list_devices(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, status_filter=status_filter, limit=limit, owner=owner, summary_only=summary_only, sort_by=sort_by, sort_order=sort_order)



list Devices

### Example


```python
import flightctl
from flightctl.models.device_list import DeviceList
from flightctl.models.sort_order import SortOrder
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supports '=', '==', and '!='.(e.g. key1=value1,key2!=value2). (optional)
    status_filter = ['status_filter_example'] # List[str] | A filter to restrict the list of devices by the value of the filtered status key. Defaults to everything. (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)
    owner = 'owner_example' # str | A selector to restrict the list of returned objects by their owner. Defaults to everything. (optional)
    summary_only = True # bool | A boolean flag to include only a summary of the devices. When set to true, the response will contain only the summary information. Only the 'owner' and 'labelSelector' parameters are supported when 'summaryOnly' is true. (optional)
    sort_by = 'metadata.name' # str | Specifies the field to sort by. (optional)
    sort_order = Asc # SortOrder | Specifies the sort order. (optional) (default to Asc)

    try:
        api_response = api_instance.list_devices(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, status_filter=status_filter, limit=limit, owner=owner, summary_only=summary_only, sort_by=sort_by, sort_order=sort_order)
        print("The response of DeviceApi->list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supports &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39;.(e.g. key1&#x3D;value1,key2!&#x3D;value2). | [optional] 
 **status_filter** | [**List[str]**](str.md)| A filter to restrict the list of devices by the value of the filtered status key. Defaults to everything. | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 
 **owner** | **str**| A selector to restrict the list of returned objects by their owner. Defaults to everything. | [optional] 
 **summary_only** | **bool**| A boolean flag to include only a summary of the devices. When set to true, the response will contain only the summary information. Only the &#39;owner&#39; and &#39;labelSelector&#39; parameters are supported when &#39;summaryOnly&#39; is true. | [optional] 
 **sort_by** | **str**| Specifies the field to sort by. | [optional] 
 **sort_order** | [**SortOrder**](.md)| Specifies the sort order. | [optional] [default to Asc]

### Return type

[**DeviceList**](DeviceList.md)

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
**403** | Not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device**
> Device patch_device(name, patch_request_inner=patch_request_inner)



Patches the specified device

### Example


```python
import flightctl
from flightctl.models.device import Device
from flightctl.models.patch_request_inner import PatchRequestInner
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | name of the device
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] |  (optional)

    try:
        api_response = api_instance.patch_device(name, patch_request_inner=patch_request_inner)
        print("The response of DeviceApi->patch_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->patch_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the device | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | [optional] 

### Return type

[**Device**](Device.md)

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

# **read_device**
> Device read_device(name)



read the specified Device

### Example


```python
import flightctl
from flightctl.models.device import Device
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | unique name of the Device

    try:
        api_response = api_instance.read_device(name)
        print("The response of DeviceApi->read_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| unique name of the Device | 

### Return type

[**Device**](Device.md)

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

# **read_device_status**
> Device read_device_status(name)



read status of the specified Device

### Example


```python
import flightctl
from flightctl.models.device import Device
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | name of the Device

    try:
        api_response = api_instance.read_device_status(name)
        print("The response of DeviceApi->read_device_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_device_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Device | 

### Return type

[**Device**](Device.md)

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

# **replace_device**
> Device replace_device(name, device)



replace the specified Device

### Example


```python
import flightctl
from flightctl.models.device import Device
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | name of the Device
    device = flightctl.Device() # Device | 

    try:
        api_response = api_instance.replace_device(name, device)
        print("The response of DeviceApi->replace_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->replace_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Device | 
 **device** | [**Device**](Device.md)|  | 

### Return type

[**Device**](Device.md)

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
**409** | StatusConflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_device_status**
> Device replace_device_status(name, device)



replace status of the specified Device

### Example


```python
import flightctl
from flightctl.models.device import Device
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | name of the Device
    device = flightctl.Device() # Device | 

    try:
        api_response = api_instance.replace_device_status(name, device)
        print("The response of DeviceApi->replace_device_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->replace_device_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Device | 
 **device** | [**Device**](Device.md)|  | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_console**
> DeviceConsole request_console(name)



Request a console connection

### Example


```python
import flightctl
from flightctl.models.device_console import DeviceConsole
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | unique name of the Device

    try:
        api_response = api_instance.request_console(name)
        print("The response of DeviceApi->request_console:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->request_console: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| unique name of the Device | 

### Return type

[**DeviceConsole**](DeviceConsole.md)

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
**409** | StatusConflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

