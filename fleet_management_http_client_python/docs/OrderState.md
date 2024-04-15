# OrderState

Order state object structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**order_id** | **int** |  | 
**timestamp** | **int** | A Unix timestamp in milliseconds. The timestamp is used to determine the time of creation of an object. | [optional] 

## Example

```python
from fleet_management_http_client_python.models.order_state import OrderState

# TODO update the JSON string below
json = "{}"
# create an instance of OrderState from a JSON string
order_state_instance = OrderState.from_json(json)
# print the JSON string representation of the object
print(OrderState.to_json())

# convert the object into a dict
order_state_dict = order_state_instance.to_dict()
# create an instance of OrderState from a dict
order_state_form_dict = order_state.from_dict(order_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


