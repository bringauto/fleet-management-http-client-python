# CarActionState

Car Action State object structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**car_id** | **int** |  | 
**timestamp** | **int** | A Unix timestamp in milliseconds. The timestamp is used to determine the time of creation of an object. | [optional] 
**action_status** | [**CarActionStatus**](CarActionStatus.md) |  | 

## Example

```python
from fleet_management_http_client_python.models.car_action_state import CarActionState

# TODO update the JSON string below
json = "{}"
# create an instance of CarActionState from a JSON string
car_action_state_instance = CarActionState.from_json(json)
# print the JSON string representation of the object
print(CarActionState.to_json())

# convert the object into a dict
car_action_state_dict = car_action_state_instance.to_dict()
# create an instance of CarActionState from a dict
car_action_state_form_dict = car_action_state.from_dict(car_action_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


