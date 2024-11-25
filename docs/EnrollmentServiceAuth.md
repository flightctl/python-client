# EnrollmentServiceAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_certificate_data** | **str** |  | 
**client_key_data** | **str** |  | 

## Example

```python
from flightctl.models.enrollment_service_auth import EnrollmentServiceAuth

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentServiceAuth from a JSON string
enrollment_service_auth_instance = EnrollmentServiceAuth.from_json(json)
# print the JSON string representation of the object
print(EnrollmentServiceAuth.to_json())

# convert the object into a dict
enrollment_service_auth_dict = enrollment_service_auth_instance.to_dict()
# create an instance of EnrollmentServiceAuth from a dict
enrollment_service_auth_from_dict = EnrollmentServiceAuth.from_dict(enrollment_service_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

