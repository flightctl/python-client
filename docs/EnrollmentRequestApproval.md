# EnrollmentRequestApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **Dict[str, str]** | labels is a set of labels to apply to the device. | [optional] 
**approved** | **bool** | approved indicates whether the request has been approved. | 
**approved_by** | **str** | approvedBy is the name of the approver. | [optional] 
**approved_at** | **datetime** | approvedAt is the time at which the request was approved. | [optional] 

## Example

```python
from flightctl.models.enrollment_request_approval import EnrollmentRequestApproval

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentRequestApproval from a JSON string
enrollment_request_approval_instance = EnrollmentRequestApproval.from_json(json)
# print the JSON string representation of the object
print(EnrollmentRequestApproval.to_json())

# convert the object into a dict
enrollment_request_approval_dict = enrollment_request_approval_instance.to_dict()
# create an instance of EnrollmentRequestApproval from a dict
enrollment_request_approval_from_dict = EnrollmentRequestApproval.from_dict(enrollment_request_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


