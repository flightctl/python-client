# KubernetesSecretProviderSpecSecretRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**namespace** | **str** |  | 
**mount_path** | **str** |  | 

## Example

```python
from flightctl.models.kubernetes_secret_provider_spec_secret_ref import KubernetesSecretProviderSpecSecretRef

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesSecretProviderSpecSecretRef from a JSON string
kubernetes_secret_provider_spec_secret_ref_instance = KubernetesSecretProviderSpecSecretRef.from_json(json)
# print the JSON string representation of the object
print(KubernetesSecretProviderSpecSecretRef.to_json())

# convert the object into a dict
kubernetes_secret_provider_spec_secret_ref_dict = kubernetes_secret_provider_spec_secret_ref_instance.to_dict()
# create an instance of KubernetesSecretProviderSpecSecretRef from a dict
kubernetes_secret_provider_spec_secret_ref_from_dict = KubernetesSecretProviderSpecSecretRef.from_dict(kubernetes_secret_provider_spec_secret_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


