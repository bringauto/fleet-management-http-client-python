# fleet-management-http-client-python.StopApi

All URIs are relative to */v2/management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stop**](StopApi.md#create_stop) | **POST** /stop | Create a new Stop.
[**delete_stop**](StopApi.md#delete_stop) | **DELETE** /stop/{stopId} | Delete a Stop with the specified ID.
[**get_stop**](StopApi.md#get_stop) | **GET** /stop/{stopId} | Find and return a single Stop by its ID.
[**get_stops**](StopApi.md#get_stops) | **GET** /stop | Find and return all existing Stops.
[**update_stop**](StopApi.md#update_stop) | **PUT** /stop | Update already existing Stop.


# **create_stop**
> Stop create_stop(stop)

Create a new Stop.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.stop import Stop
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
    api_instance = fleet-management-http-client-python.StopApi(api_client)
    stop = fleet-management-http-client-python.Stop() # Stop | Stop model in JSON format.

    try:
        # Create a new Stop.
        api_response = api_instance.create_stop(stop)
        print("The response of StopApi->create_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StopApi->create_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop** | [**Stop**](Stop.md)| Stop model in JSON format. | 

### Return type

[**Stop**](Stop.md)

### Authorization

[oAuth2AuthCode](../README.md#oAuth2AuthCode), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Stop has been successfully created. |  -  |
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
import fleet-management-http-client-python
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
    api_instance = fleet-management-http-client-python.StopApi(api_client)
    stop_id = 1 # int | ID of the Stop to be deleted.

    try:
        # Delete a Stop with the specified ID.
        api_instance.delete_stop(stop_id)
    except Exception as e:
        print("Exception when calling StopApi->delete_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop_id** | **int**| ID of the Stop to be deleted. | 

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
import fleet-management-http-client-python
from fleet-management-http-client-python.models.stop import Stop
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
    api_instance = fleet-management-http-client-python.StopApi(api_client)
    stop_id = 1 # int | ID of Stop to be returned.

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
 **stop_id** | **int**| ID of Stop to be returned. | 

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
import fleet-management-http-client-python
from fleet-management-http-client-python.models.stop import Stop
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
    api_instance = fleet-management-http-client-python.StopApi(api_client)

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

# **update_stop**
> update_stop(stop)

Update already existing Stop.

### Example

* OAuth Authentication (oAuth2AuthCode):
* Api Key Authentication (APIKeyAuth):

```python
import fleet-management-http-client-python
from fleet-management-http-client-python.models.stop import Stop
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
    api_instance = fleet-management-http-client-python.StopApi(api_client)
    stop = fleet-management-http-client-python.Stop() # Stop | JSON representation of the updated Stop.

    try:
        # Update already existing Stop.
        api_instance.update_stop(stop)
    except Exception as e:
        print("Exception when calling StopApi->update_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop** | [**Stop**](Stop.md)| JSON representation of the updated Stop. | 

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
**200** | The Stop has been successfully updated. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

