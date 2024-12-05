# flightctl.EnrollmentconfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollment_config**](EnrollmentconfigApi.md#enrollment_config) | **GET** /api/v1/enrollmentconfig/{name} | 


# **enrollment_config**
> EnrollmentConfig enrollment_config(name)



Get config for enrolling devices

### Example


```python
import flightctl
from flightctl.models.enrollment_config import EnrollmentConfig
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
    api_instance = flightctl.EnrollmentconfigApi(api_client)
    name = 'name_example' # str | the name of approved CSR

    try:
        api_response = api_instance.enrollment_config(name)
        print("The response of EnrollmentconfigApi->enrollment_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentconfigApi->enrollment_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the name of approved CSR | 

### Return type

[**EnrollmentConfig**](EnrollmentConfig.md)

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

