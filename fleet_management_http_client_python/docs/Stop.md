# Stop

Stop object structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**position** | [**GNSSPosition**](GNSSPosition.md) |  | 
**notification_phone** | [**MobilePhone**](MobilePhone.md) |  | [optional] 

## Example

```python
from fleet_management_http_client_python.models.stop import Stop

# TODO update the JSON string below
json = "{}"
# create an instance of Stop from a JSON string
stop_instance = Stop.from_json(json)
# print the JSON string representation of the object
print(Stop.to_json())

# convert the object into a dict
stop_dict = stop_instance.to_dict()
# create an instance of Stop from a dict
stop_form_dict = stop.from_dict(stop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


