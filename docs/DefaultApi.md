# flightctl.DefaultApi

All URIs are relative to *https://raw.githubusercontent.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_certificate_signing_request**](DefaultApi.md#approve_certificate_signing_request) | **POST** /api/v1/certificatesigningrequests/{name}/approval | 
[**auth_config**](DefaultApi.md#auth_config) | **GET** /api/v1/auth/config | 
[**auth_validate**](DefaultApi.md#auth_validate) | **GET** /api/v1/auth/validate | 
[**deny_certificate_signing_request**](DefaultApi.md#deny_certificate_signing_request) | **DELETE** /api/v1/certificatesigningrequests/{name}/approval | 


# **approve_certificate_signing_request**
> CertificateSigningRequest approve_certificate_signing_request(name)



approve the specified CertificateSigningRequest

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
    api_instance = flightctl.DefaultApi(api_client)
    name = 'name_example' # str | name of the CertificateSigningRequest

    try:
        api_response = api_instance.approve_certificate_signing_request(name)
        print("The response of DefaultApi->approve_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->approve_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |
**409** | StatusConflict |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_config**
> AuthConfig auth_config()



Get auth configuration

### Example


```python
import flightctl
from flightctl.models.auth_config import AuthConfig
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
    api_instance = flightctl.DefaultApi(api_client)

    try:
        api_response = api_instance.auth_config()
        print("The response of DefaultApi->auth_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthConfig**](AuthConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**418** | Auth not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_validate**
> auth_validate(authentication=authentication)



Validate auth token

### Example


```python
import flightctl
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
    api_instance = flightctl.DefaultApi(api_client)
    authentication = 'authentication_example' # str |  (optional)

    try:
        api_instance.auth_validate(authentication=authentication)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token valid |  -  |
**401** | Token invalid |  -  |
**418** | Auth not configured |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deny_certificate_signing_request**
> CertificateSigningRequest deny_certificate_signing_request(name)



deny the specified CertificateSigningRequest

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
    api_instance = flightctl.DefaultApi(api_client)
    name = 'name_example' # str | name of the CertificateSigningRequest

    try:
        api_response = api_instance.deny_certificate_signing_request(name)
        print("The response of DefaultApi->deny_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->deny_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest | 

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

