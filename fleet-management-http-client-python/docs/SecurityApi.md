# fleet-management-http-client-python.SecurityApi

All URIs are relative to */v2/management*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](SecurityApi.md#login) | **GET** /login | 
[**token_get**](SecurityApi.md#token_get) | **GET** /token_get | 
[**token_refresh**](SecurityApi.md#token_refresh) | **GET** /token_refresh | 


# **login**
> login()



Login using Keycloak.

### Example


```python
import fleet-management-http-client-python
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
    host = "/v2/management"
)


# Enter a context with an instance of the API client
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.SecurityApi(api_client)

    try:
        api_instance.login()
    except Exception as e:
        print("Exception when calling SecurityApi->login: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the Keycloak authentication. |  -  |
**500** | The login failed due to an internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_get**
> token_get(state=state, session_state=session_state, iss=iss, code=code)



Callback endpoint for the Keycloak to receive JWT token.

### Example


```python
import fleet-management-http-client-python
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
    host = "/v2/management"
)


# Enter a context with an instance of the API client
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.SecurityApi(api_client)
    state = 'your_state_info' # str | State returned by the Keycloak authentication. (optional)
    session_state = '167e141d-2f55-4d...' # str | Session state returned by the Keycloak authentication. (optional)
    iss = 'http%3A%2F%2Flocalhost%3A8081%2Frealms%2Fmaster' # str | Code issuer returned by the Keycloak authentication. (optional)
    code = '5dea27d2-4b2d-48...' # str | Code used for JWT token generation returned by Keycloak authentication. (optional)

    try:
        api_instance.token_get(state=state, session_state=session_state, iss=iss, code=code)
    except Exception as e:
        print("Exception when calling SecurityApi->token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| State returned by the Keycloak authentication. | [optional] 
 **session_state** | **str**| Session state returned by the Keycloak authentication. | [optional] 
 **iss** | **str**| Code issuer returned by the Keycloak authentication. | [optional] 
 **code** | **str**| Code used for JWT token generation returned by Keycloak authentication. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a standard Keycloak token. |  -  |
**500** | The login failed due to an internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_refresh**
> token_refresh(refresh_token)



Endpoint to receive JWT token from refresh token.

### Example


```python
import fleet-management-http-client-python
from fleet-management-http-client-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2/management
# See configuration.py for a list of all supported configuration parameters.
configuration = fleet-management-http-client-python.Configuration(
    host = "/v2/management"
)


# Enter a context with an instance of the API client
with fleet-management-http-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fleet-management-http-client-python.SecurityApi(api_client)
    refresh_token = 'eyJhbGciOiJIUzI1NiIsI...' # str | Refresh token used for JWT token generation.

    try:
        api_instance.token_refresh(refresh_token)
    except Exception as e:
        print("Exception when calling SecurityApi->token_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**| Refresh token used for JWT token generation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a new standard Keycloak token. |  -  |
**500** | Token refresh failed due to an internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

