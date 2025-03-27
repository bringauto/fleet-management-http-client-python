# fleet_management_http_client_python.StopApi

All URIs are relative to */v2/management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stops**](StopApi.md#create_stops) | **POST** /stop | Create new Stops.
[**delete_stop**](StopApi.md#delete_stop) | **DELETE** /stop/{stopId} | Delete a Stop with the specified ID.
[**get_stop**](StopApi.md#get_stop) | **GET** /stop/{stopId} | Find and return a single Stop by its ID.
[**get_stops**](StopApi.md#get_stops) | **GET** /stop | Find and return all existing Stops.
[**update_stops**](StopApi.md#update_stops) | **PUT** /stop | Update already existing Stops.


# **create_stops**
> List[Stop] create_stops(stop)

Create new Stops.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.stop import Stop
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
    api_instance = fleet_management_http_client_python.StopApi(api_client)
    stop = [fleet_management_http_client_python.Stop()] # List[Stop] | A list of Stop models in JSON format.

    try:
        # Create new Stops.
        api_response = api_instance.create_stops(stop)
        print("The response of StopApi->create_stops:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StopApi->create_stops: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop** | [**List[Stop]**](Stop.md)| A list of Stop models in JSON format. | 

### Return type

[**List[Stop]**](Stop.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Stops have been successfully created. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stop**
> delete_stop(stop_id)

Delete a Stop with the specified ID.

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
    api_instance = fleet_management_http_client_python.StopApi(api_client)
    stop_id = 56 # int | The Stop ID.

    try:
        # Delete a Stop with the specified ID.
        api_instance.delete_stop(stop_id)
    except Exception as e:
        print("Exception when calling StopApi->delete_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop_id** | **int**| The Stop ID. | 

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
**200** | The Stop with the specified ID has been deleted. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**405** | Method not allowed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stop**
> Stop get_stop(stop_id)

Find and return a single Stop by its ID.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.stop import Stop
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
    api_instance = fleet_management_http_client_python.StopApi(api_client)
    stop_id = 56 # int | The Stop ID.

    try:
        # Find and return a single Stop by its ID.
        api_response = api_instance.get_stop(stop_id)
        print("The response of StopApi->get_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StopApi->get_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop_id** | **int**| The Stop ID. | 

### Return type

[**Stop**](Stop.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Stop with the specified ID has been found and returned. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stops**
> List[Stop] get_stops()

Find and return all existing Stops.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.stop import Stop
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
    api_instance = fleet_management_http_client_python.StopApi(api_client)

    try:
        # Find and return all existing Stops.
        api_response = api_instance.get_stops()
        print("The response of StopApi->get_stops:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StopApi->get_stops: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Stop]**](Stop.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All the currently existing Stops have been returned. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stops**
> update_stops(stop)

Update already existing Stops.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet_management_http_client_python
from fleet_management_http_client_python.models.stop import Stop
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
    api_instance = fleet_management_http_client_python.StopApi(api_client)
    stop = [fleet_management_http_client_python.Stop()] # List[Stop] | JSON representation of a list of the Stops with updated data.

    try:
        # Update already existing Stops.
        api_instance.update_stops(stop)
    except Exception as e:
        print("Exception when calling StopApi->update_stops: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop** | [**List[Stop]**](Stop.md)| JSON representation of a list of the Stops with updated data. | 

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
**200** | The Stops have been successfully updated. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

