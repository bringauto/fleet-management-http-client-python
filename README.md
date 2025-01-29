# Fleet Management HTTP API Client

This is a Client for the Fleet Management HTTP API. You can find the Fleet Management HTTP API repository [here](https://github.com/bringauto/fleet-management-http-api).
The HTTP API is described by the `openapi/openapi.yaml` according to [OpenAPI Specification](https://openapis.org).
A full specification can be found in the `openapi` folder in the root folder.

## Auto-generated code

The auto-generated code can be found in the `fleet_management_http_client_python` folder.
The code is generated using the `openapi-generator-cli` tool. The code is generated using the `openapi/openapi.yaml` file.
DO NOT edit the auto-generated code manually.

## Documentation

The auto-generated documentation for the client models and API is in the `fleet_http_client_python/docs` folder.

# Usage

To use the client, get the code from the repository or install it according to the instructions below. You can look at the `example/client_impl.py` file for an example of how to use the client.

## Installation

To install the client, run

```bash
pip install git+https://github.com/bringauto/fleet-management-http-client-python.git
```

## Client re-generation

If you want to re-generate the client code with the new specification, you first have to replace the specification in the `openapi` folder.
Then you can run the `regen.sh` script (from the root folder). [npm](https://www.npmjs.com/), git and [OpenAPI Generator](https://openapi-generator.tech/docs/installation) are required.

# Requirements

Python 3.10.12+

# Authorization

## Reading data

The client can get access to reading data from the server by either

- providing a `Bearer` JWT token in the `Authorization` header.
- providing a valid API key as a query parameter in the request. This authentication has precedence over the `Bearer` token.

## Writing data

The client can get access to modifiying data on the server by settting a cookie containing the name of a tenant,
that the client has access to. This is done in addition to the authorization methods for reading data.

The client is responsible for setting the cookie in the request.

To read more on the tenants, see the [Fleet Management HTTP API](https://github.com/bringauto/fleet-management-http-api/blob/master/docs/tenants.md)
