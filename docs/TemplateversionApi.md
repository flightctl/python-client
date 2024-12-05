# flightctl.TemplateversionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_template_version**](TemplateversionApi.md#delete_template_version) | **DELETE** /api/v1/fleets/{fleet}/templateversions/{name} | 
[**delete_template_versions**](TemplateversionApi.md#delete_template_versions) | **DELETE** /api/v1/fleets/{fleet}/templateversions | 
[**list_template_versions**](TemplateversionApi.md#list_template_versions) | **GET** /api/v1/fleets/{fleet}/templateversions | 
[**read_template_version**](TemplateversionApi.md#read_template_version) | **GET** /api/v1/fleets/{fleet}/templateversions/{name} | 


# **delete_template_version**
> TemplateVersion delete_template_version(fleet, name)



delete a template version

### Example


```python
import flightctl
from flightctl.models.template_version import TemplateVersion
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
    api_instance = flightctl.TemplateversionApi(api_client)
    fleet = 'fleet_example' # str | The owner of the template version.
    name = 'name_example' # str | name of the template version.

    try:
        api_response = api_instance.delete_template_version(fleet, name)
        print("The response of TemplateversionApi->delete_template_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateversionApi->delete_template_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet** | **str**| The owner of the template version. | 
 **name** | **str**| name of the template version. | 

### Return type

[**TemplateVersion**](TemplateVersion.md)

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

# **delete_template_versions**
> Status delete_template_versions(fleet)



delete a collection of template versions

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
    api_instance = flightctl.TemplateversionApi(api_client)
    fleet = 'fleet_example' # str | The owner of the template versions.

    try:
        api_response = api_instance.delete_template_versions(fleet)
        print("The response of TemplateversionApi->delete_template_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateversionApi->delete_template_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet** | **str**| The owner of the template versions. | 

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

# **list_template_versions**
> TemplateVersionList list_template_versions(fleet, var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, sort_by=sort_by, sort_order=sort_order)



list template versions

### Example


```python
import flightctl
from flightctl.models.sort_order import SortOrder
from flightctl.models.template_version_list import TemplateVersionList
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
    api_instance = flightctl.TemplateversionApi(api_client)
    fleet = 'fleet_example' # str | The owner of the template versions.
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supports '=', '==', and '!='.(e.g. key1=value1,key2!=value2). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)
    sort_by = 'metadata.name' # str | Specifies the field to sort by. (optional)
    sort_order = Asc # SortOrder | Specifies the sort order. (optional) (default to Asc)

    try:
        api_response = api_instance.list_template_versions(fleet, var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, sort_by=sort_by, sort_order=sort_order)
        print("The response of TemplateversionApi->list_template_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateversionApi->list_template_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet** | **str**| The owner of the template versions. | 
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supports &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39;.(e.g. key1&#x3D;value1,key2!&#x3D;value2). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 
 **sort_by** | **str**| Specifies the field to sort by. | [optional] 
 **sort_order** | [**SortOrder**](.md)| Specifies the sort order. | [optional] [default to Asc]

### Return type

[**TemplateVersionList**](TemplateVersionList.md)

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

# **read_template_version**
> TemplateVersion read_template_version(fleet, name)



read the specified template version

### Example


```python
import flightctl
from flightctl.models.template_version import TemplateVersion
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
    api_instance = flightctl.TemplateversionApi(api_client)
    fleet = 'fleet_example' # str | The owner of the template version.
    name = 'name_example' # str | Name of the template version.

    try:
        api_response = api_instance.read_template_version(fleet, name)
        print("The response of TemplateversionApi->read_template_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateversionApi->read_template_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet** | **str**| The owner of the template version. | 
 **name** | **str**| Name of the template version. | 

### Return type

[**TemplateVersion**](TemplateVersion.md)

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

