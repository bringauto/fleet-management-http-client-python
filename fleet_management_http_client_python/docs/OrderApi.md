# fleet_management_http_client_python.OrderApi

All URIs are relative to */v2/management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_orders**](OrderApi.md#create_orders) | **POST** /order | Create new Orders.
[**delete_order**](OrderApi.md#delete_order) | **DELETE** /order/{carId}/{orderId} | Delete an Order identified by its ID and ID of a car to which it is assigned.
[**get_car_orders**](OrderApi.md#get_car_orders) | **GET** /order/{carId} | Find existing Orders by the corresponding Car ID and return them.
[**get_order**](OrderApi.md#get_order) | **GET** /order/{carId}/{orderId} | Find an existing Order by the car ID and the order ID and return it.
[**get_orders**](OrderApi.md#get_orders) | **GET** /order | Find all currently existing Orders.


# **create_orders**
> List[Order] create_orders(order)

Create new Orders.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.order import Order
from fleet_management_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_management_http_client_python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet_management_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_management_http_client_python.OrderApi(api_client)
    order = [fleet_management_http_client_python.Order()] # List[Order] | A list of Order models in JSON format.

    try:
        # Create new Orders.
        api_response = api_instance.create_orders(order)
        print("The response of OrderApi->create_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**List[Order]**](Order.md)| A list of Order models in JSON format. | 

### Return type

[**List[Order]**](Order.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new Orders have been successfully created. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order**
> delete_order(car_id, order_id)

Delete an Order identified by its ID and ID of a car to which it is assigned.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_management_http_client_python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet_management_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_management_http_client_python.OrderApi(api_client)
    car_id = 56 # int | The car ID.
    order_id = 56 # int | The order ID.

    try:
        # Delete an Order identified by its ID and ID of a car to which it is assigned.
        api_instance.delete_order(car_id, order_id)
    except Exception as e:
        print("Exception when calling OrderApi->delete_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| The car ID. | 
 **order_id** | **int**| The order ID. | 

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Order with the specified ID has been successfully deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**405** | Method not allowed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_car_orders**
> List[Order] get_car_orders(car_id, since=since)

Find existing Orders by the corresponding Car ID and return them.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.order import Order
from fleet_management_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_management_http_client_python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet_management_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_management_http_client_python.OrderApi(api_client)
    car_id = 56 # int | The car ID.
    since = 56 # int | A Unix timestamp in milliseconds. If specified, only objects created at the time or later will be returned. If unspecified, all objects are returned (since is set to 0 in that case). (optional)

    try:
        # Find existing Orders by the corresponding Car ID and return them.
        api_response = api_instance.get_car_orders(car_id, since=since)
        print("The response of OrderApi->get_car_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_car_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| The car ID. | 
 **since** | **int**| A Unix timestamp in milliseconds. If specified, only objects created at the time or later will be returned. If unspecified, all objects are returned (since is set to 0 in that case). | [optional] 

### Return type

[**List[Order]**](Order.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Orders assigned to the Car with the given ID have been found, sorted by their creation timestamp from oldest to newest and returned. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> Order get_order(car_id, order_id)

Find an existing Order by the car ID and the order ID and return it.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.order import Order
from fleet_management_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_management_http_client_python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet_management_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_management_http_client_python.OrderApi(api_client)
    car_id = 56 # int | The car ID.
    order_id = 56 # int | The order ID.

    try:
        # Find an existing Order by the car ID and the order ID and return it.
        api_response = api_instance.get_order(car_id, order_id)
        print("The response of OrderApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| The car ID. | 
 **order_id** | **int**| The order ID. | 

### Return type

[**Order**](Order.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Order with the specified car ID and order ID has been found and returned. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> List[Order] get_orders(since=since)

Find all currently existing Orders.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.order import Order
from fleet_management_http_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet_management_http_client_python.Configuration(
    host = "/v2/management"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with fleet_management_http_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet_management_http_client_python.OrderApi(api_client)
    since = 56 # int | A Unix timestamp in milliseconds. If specified, only objects created at the time or later will be returned. If unspecified, all objects are returned (since is set to 0 in that case). (optional)

    try:
        # Find all currently existing Orders.
        api_response = api_instance.get_orders(since=since)
        print("The response of OrderApi->get_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| A Unix timestamp in milliseconds. If specified, only objects created at the time or later will be returned. If unspecified, all objects are returned (since is set to 0 in that case). | [optional] 

### Return type

[**List[Order]**](Order.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All the currently existing Orders have been sorted by their creation timestamp from the oldest to newest and returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

