# ResourceAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | [**ResourceAlertSeverityType**](ResourceAlertSeverityType.md) |  | 
**duration** | **str** | Duration is the time over which the average usage is observed before alerting. Format: positive integer followed by &#39;s&#39; for seconds, &#39;m&#39; for minutes, &#39;h&#39; for hours. | 
**percentage** | **float** | The percentage of usage that triggers the alert. | 
**description** | **str** | A human-readable description of the alert. | 

## Example

```python
from flightctl.models.resource_alert_rule import ResourceAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAlertRule from a JSON string
resource_alert_rule_instance = ResourceAlertRule.from_json(json)
# print the JSON string representation of the object
print(ResourceAlertRule.to_json())

# convert the object into a dict
resource_alert_rule_dict = resource_alert_rule_instance.to_dict()
# create an instance of ResourceAlertRule from a dict
resource_alert_rule_from_dict = ResourceAlertRule.from_dict(resource_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


