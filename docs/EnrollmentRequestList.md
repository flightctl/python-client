# EnrollmentRequestList

EnrollmentRequestList is a list of EnrollmentRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[EnrollmentRequest]**](EnrollmentRequest.md) | List of EnrollmentRequest. | 

## Example

```python
from flightctl.models.enrollment_request_list import EnrollmentRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentRequestList from a JSON string
enrollment_request_list_instance = EnrollmentRequestList.from_json(json)
# print the JSON string representation of the object
print(EnrollmentRequestList.to_json())

# convert the object into a dict
enrollment_request_list_dict = enrollment_request_list_instance.to_dict()
# create an instance of EnrollmentRequestList from a dict
enrollment_request_list_from_dict = EnrollmentRequestList.from_dict(enrollment_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

