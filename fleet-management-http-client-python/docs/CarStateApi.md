# fleet-management-http-client-python.CarStateApi

All URIs are relative to */v2/management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_car_state**](CarStateApi.md#add_car_state) | **POST** /carstate | Add a new Car State.
[**get_all_car_states**](CarStateApi.md#get_all_car_states) | **GET** /carstate | Find one or all Car States for a Car with the specified ID.
[**get_car_states**](CarStateApi.md#get_car_states) | **GET** /carstate/{carId} | Find one or all Car States for a given Car.


# **add_car_state**
> add_car_state(car_state)

Add a new Car State.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.car_state import CarState
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
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
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.CarStateApi(api_client)
    car_state = fleet-management-http-client-python.CarState() # CarState | Car State model in JSON format.

    try:
        # Add a new Car State.
        api_instance.add_car_state(car_state)
    except Exception as e:
        print("Exception when calling CarStateApi->add_car_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_state** | [**CarState**](CarState.md)| Car State model in JSON format. | 

### Return type

void (empty response body)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new Car State has been successfully added. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_car_states**
> List[CarState] get_all_car_states()

Find one or all Car States for a Car with the specified ID.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.car_state import CarState
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
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
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.CarStateApi(api_client)

    try:
        # Find one or all Car States for a Car with the specified ID.
        api_response = api_instance.get_all_car_states()
        print("The response of CarStateApi->get_all_car_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarStateApi->get_all_car_states: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CarState]**](CarState.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully found all Car States complying with the request parameters. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_car_states**
> List[CarState] get_car_states(car_id, all_available=all_available)

Find one or all Car States for a given Car.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.car_state import CarState
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
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
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.CarStateApi(api_client)
    car_id = 1 # int | ID of the Car for which to find the Car States.
    all_available = true # bool | Whether to return all available car states or only the latest one (optional)

    try:
        # Find one or all Car States for a given Car.
        api_response = api_instance.get_car_states(car_id, all_available=all_available)
        print("The response of CarStateApi->get_car_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarStateApi->get_car_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| ID of the Car for which to find the Car States. | 
 **all_available** | **bool**| Whether to return all available car states or only the latest one | [optional] 

### Return type

[**List[CarState]**](CarState.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully found all Car States complying with the request parameters. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

