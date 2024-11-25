# flightctl.EnrollmentrequestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_enrollment_request**](EnrollmentrequestApi.md#approve_enrollment_request) | **POST** /api/v1/enrollmentrequests/{name}/approval | 
[**create_enrollment_request**](EnrollmentrequestApi.md#create_enrollment_request) | **POST** /api/v1/enrollmentrequests | 
[**delete_enrollment_request**](EnrollmentrequestApi.md#delete_enrollment_request) | **DELETE** /api/v1/enrollmentrequests/{name} | 
[**delete_enrollment_requests**](EnrollmentrequestApi.md#delete_enrollment_requests) | **DELETE** /api/v1/enrollmentrequests | 
[**list_enrollment_requests**](EnrollmentrequestApi.md#list_enrollment_requests) | **GET** /api/v1/enrollmentrequests | 
[**read_enrollment_request**](EnrollmentrequestApi.md#read_enrollment_request) | **GET** /api/v1/enrollmentrequests/{name} | 
[**read_enrollment_request_status**](EnrollmentrequestApi.md#read_enrollment_request_status) | **GET** /api/v1/enrollmentrequests/{name}/status | 
[**replace_enrollment_request**](EnrollmentrequestApi.md#replace_enrollment_request) | **PUT** /api/v1/enrollmentrequests/{name} | 
[**replace_enrollment_request_status**](EnrollmentrequestApi.md#replace_enrollment_request_status) | **PUT** /api/v1/enrollmentrequests/{name}/status | 


# **approve_enrollment_request**
> EnrollmentRequestApproval approve_enrollment_request(name, enrollment_request_approval)



create approval of the specified EnrollmentRequest

### Example


```python
import flightctl
from flightctl.models.enrollment_request_approval import EnrollmentRequestApproval
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | name of the EnrollmentRequest
    enrollment_request_approval = flightctl.EnrollmentRequestApproval() # EnrollmentRequestApproval | 

    try:
        api_response = api_instance.approve_enrollment_request(name, enrollment_request_approval)
        print("The response of EnrollmentrequestApi->approve_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->approve_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the EnrollmentRequest | 
 **enrollment_request_approval** | [**EnrollmentRequestApproval**](EnrollmentRequestApproval.md)|  | 

### Return type

[**EnrollmentRequestApproval**](EnrollmentRequestApproval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | UnprocessableEntity |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_enrollment_request**
> EnrollmentRequest create_enrollment_request(enrollment_request)



request enrollment of a Device

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    enrollment_request = flightctl.EnrollmentRequest() # EnrollmentRequest | 

    try:
        api_response = api_instance.create_enrollment_request(enrollment_request)
        print("The response of EnrollmentrequestApi->create_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->create_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_request** | [**EnrollmentRequest**](EnrollmentRequest.md)|  | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**208** | Already Reported |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**409** | StatusConflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_enrollment_request**
> EnrollmentRequest delete_enrollment_request(name)



delete a Enrollment Request

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | name of the Enrollment Request

    try:
        api_response = api_instance.delete_enrollment_request(name)
        print("The response of EnrollmentrequestApi->delete_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->delete_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Enrollment Request | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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

# **delete_enrollment_requests**
> Status delete_enrollment_requests()



delete a collection of Enrollments

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
    api_instance = flightctl.EnrollmentrequestApi(api_client)

    try:
        api_response = api_instance.delete_enrollment_requests()
        print("The response of EnrollmentrequestApi->delete_enrollment_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->delete_enrollment_requests: %s\n" % e)
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

# **list_enrollment_requests**
> EnrollmentRequestList list_enrollment_requests(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, sort_by=sort_by, sort_order=sort_order)



list Enrollment Requests

### Example


```python
import flightctl
from flightctl.models.enrollment_request_list import EnrollmentRequestList
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supports '=', '==', and '!='.(e.g. key1=value1,key2!=value2). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)
    sort_by = 'metadata.name' # str | Specifies the field to sort by. (optional)
    sort_order = Asc # SortOrder | Specifies the sort order. (optional) (default to Asc)

    try:
        api_response = api_instance.list_enrollment_requests(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, sort_by=sort_by, sort_order=sort_order)
        print("The response of EnrollmentrequestApi->list_enrollment_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->list_enrollment_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supports &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39;.(e.g. key1&#x3D;value1,key2!&#x3D;value2). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 
 **sort_by** | **str**| Specifies the field to sort by. | [optional] 
 **sort_order** | [**SortOrder**](.md)| Specifies the sort order. | [optional] [default to Asc]

### Return type

[**EnrollmentRequestList**](EnrollmentRequestList.md)

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

# **read_enrollment_request**
> EnrollmentRequest read_enrollment_request(name)



read the specified Enrollment

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | the fingerprint of the EnrollmentRequest

    try:
        api_response = api_instance.read_enrollment_request(name)
        print("The response of EnrollmentrequestApi->read_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->read_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the fingerprint of the EnrollmentRequest | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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

# **read_enrollment_request_status**
> EnrollmentRequest read_enrollment_request_status(name)



read status of the specified EnrollmentRequest

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | name of the EnrollmentRequest

    try:
        api_response = api_instance.read_enrollment_request_status(name)
        print("The response of EnrollmentrequestApi->read_enrollment_request_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->read_enrollment_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the EnrollmentRequest | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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

# **replace_enrollment_request**
> EnrollmentRequest replace_enrollment_request(name, enrollment_request)



replace the specified Enrollment Request

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | name of the EnrollmentRequest
    enrollment_request = flightctl.EnrollmentRequest() # EnrollmentRequest | 

    try:
        api_response = api_instance.replace_enrollment_request(name, enrollment_request)
        print("The response of EnrollmentrequestApi->replace_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->replace_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the EnrollmentRequest | 
 **enrollment_request** | [**EnrollmentRequest**](EnrollmentRequest.md)|  | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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

# **replace_enrollment_request_status**
> EnrollmentRequest replace_enrollment_request_status(name, enrollment_request)



replace status of the specified EnrollmentRequest

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | name of the EnrollmentRequest
    enrollment_request = flightctl.EnrollmentRequest() # EnrollmentRequest | 

    try:
        api_response = api_instance.replace_enrollment_request_status(name, enrollment_request)
        print("The response of EnrollmentrequestApi->replace_enrollment_request_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->replace_enrollment_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the EnrollmentRequest | 
 **enrollment_request** | [**EnrollmentRequest**](EnrollmentRequest.md)|  | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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

