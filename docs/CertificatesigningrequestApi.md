# flightctl.CertificatesigningrequestApi

All URIs are relative to *https://raw.githubusercontent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate_signing_request**](CertificatesigningrequestApi.md#create_certificate_signing_request) | **POST** /api/v1/certificatesigningrequests | 
[**delete_certificate_signing_request**](CertificatesigningrequestApi.md#delete_certificate_signing_request) | **DELETE** /api/v1/certificatesigningrequests/{name} | 
[**delete_certificate_signing_requests**](CertificatesigningrequestApi.md#delete_certificate_signing_requests) | **DELETE** /api/v1/certificatesigningrequests | 
[**list_certificate_signing_requests**](CertificatesigningrequestApi.md#list_certificate_signing_requests) | **GET** /api/v1/certificatesigningrequests | 
[**patch_certificate_signing_request**](CertificatesigningrequestApi.md#patch_certificate_signing_request) | **PATCH** /api/v1/certificatesigningrequests/{name} | 
[**read_certificate_signing_request**](CertificatesigningrequestApi.md#read_certificate_signing_request) | **GET** /api/v1/certificatesigningrequests/{name} | 
[**replace_certificate_signing_request**](CertificatesigningrequestApi.md#replace_certificate_signing_request) | **PUT** /api/v1/certificatesigningrequests/{name} | 


# **create_certificate_signing_request**
> CertificateSigningRequest create_certificate_signing_request(certificate_signing_request)



request Certificate Signing

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request import CertificateSigningRequest
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
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    certificate_signing_request = flightctl.CertificateSigningRequest() # CertificateSigningRequest | 

    try:
        api_response = api_instance.create_certificate_signing_request(certificate_signing_request)
        print("The response of CertificatesigningrequestApi->create_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->create_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_signing_request** | [**CertificateSigningRequest**](CertificateSigningRequest.md)|  | 

### Return type

[**CertificateSigningRequest**](CertificateSigningRequest.md)

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
**202** | Accepted |  -  |
**208** | Already Reported |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate_signing_request**
> CertificateSigningRequest delete_certificate_signing_request(name)



delete a Certificate Signing Request

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request import CertificateSigningRequest
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
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    name = 'name_example' # str | name of the Certificate Signing Request

    try:
        api_response = api_instance.delete_certificate_signing_request(name)
        print("The response of CertificatesigningrequestApi->delete_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->delete_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Certificate Signing Request | 

### Return type

[**CertificateSigningRequest**](CertificateSigningRequest.md)

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

# **delete_certificate_signing_requests**
> Status delete_certificate_signing_requests()



delete a collection of CertificateSigningRequest

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
    api_instance = flightctl.CertificatesigningrequestApi(api_client)

    try:
        api_response = api_instance.delete_certificate_signing_requests()
        print("The response of CertificatesigningrequestApi->delete_certificate_signing_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->delete_certificate_signing_requests: %s\n" % e)
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

# **list_certificate_signing_requests**
> CertificateSigningRequestList list_certificate_signing_requests(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, sort_by=sort_by, sort_order=sort_order)



list CertificateSigningRequests

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request_list import CertificateSigningRequestList
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
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supports '=', '==', and '!='.(e.g. key1=value1,key2!=value2). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)
    sort_by = 'metadata.name' # str | Specifies the field to sort by. (optional)
    sort_order = Asc # SortOrder | Specifies the sort order. (optional) (default to Asc)

    try:
        api_response = api_instance.list_certificate_signing_requests(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, sort_by=sort_by, sort_order=sort_order)
        print("The response of CertificatesigningrequestApi->list_certificate_signing_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->list_certificate_signing_requests: %s\n" % e)
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

[**CertificateSigningRequestList**](CertificateSigningRequestList.md)

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

# **patch_certificate_signing_request**
> CertificateSigningRequest patch_certificate_signing_request(name, patch_request_inner=patch_request_inner)



partially update the specified CertificateSigningRequest

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request import CertificateSigningRequest
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
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    name = 'name_example' # str | name of the certificatesigningrequest
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] |  (optional)

    try:
        api_response = api_instance.patch_certificate_signing_request(name, patch_request_inner=patch_request_inner)
        print("The response of CertificatesigningrequestApi->patch_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->patch_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the certificatesigningrequest | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | [optional] 

### Return type

[**CertificateSigningRequest**](CertificateSigningRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json
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

# **read_certificate_signing_request**
> CertificateSigningRequest read_certificate_signing_request(name)



read the specified certificateSigningRequest

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request import CertificateSigningRequest
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
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    name = 'name_example' # str | the device identifier of the CertificateSigningRequest

    try:
        api_response = api_instance.read_certificate_signing_request(name)
        print("The response of CertificatesigningrequestApi->read_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->read_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the device identifier of the CertificateSigningRequest | 

### Return type

[**CertificateSigningRequest**](CertificateSigningRequest.md)

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

# **replace_certificate_signing_request**
> CertificateSigningRequest replace_certificate_signing_request(name, certificate_signing_request)



replace the specified CertificateSigningRequest

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request import CertificateSigningRequest
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
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    name = 'name_example' # str | name of the CertificateSigningRequest
    certificate_signing_request = flightctl.CertificateSigningRequest() # CertificateSigningRequest | 

    try:
        api_response = api_instance.replace_certificate_signing_request(name, certificate_signing_request)
        print("The response of CertificatesigningrequestApi->replace_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->replace_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest | 
 **certificate_signing_request** | [**CertificateSigningRequest**](CertificateSigningRequest.md)|  | 

### Return type

[**CertificateSigningRequest**](CertificateSigningRequest.md)

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

