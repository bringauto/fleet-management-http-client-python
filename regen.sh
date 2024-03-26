#!/bin/bash

npx @openapitools/openapi-generator-cli generate -i openapi/openapi.yaml \
 --generator-name python \
 --output . \
 --package-name fleet-management-http-client-python \
 --additional-properties=generateSourceCodeOnly=true,apiTests=false,modelTests=false