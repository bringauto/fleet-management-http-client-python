# Order

Order object structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**priority** | **str** | Priority (low, normal, high) | [optional] [default to 'normal']
**user_id** | **int** |  | 
**timestamp** | **int** | A Unix timestamp in milliseconds. The timestamp is used to determine the time of creation of an object. | [optional] 
**car_id** | **int** |  | 
**notification** | **str** |  | [optional] 
**target_stop_id** | **int** |  | 
**stop_route_id** | **int** |  | 
**notification_phone** | [**MobilePhone**](MobilePhone.md) |  | [optional] 
**last_state** | [**OrderState**](OrderState.md) |  | [optional] 

## Example

```python
from fleet_management_http_client_python.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_form_dict = order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


