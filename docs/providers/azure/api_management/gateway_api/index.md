---
title: gateway_api
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_api
  - api_management
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.gateway_api</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `sourceApiId` | `string` | API identifier of the source API. |
| `serviceUrl` | `string` | Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long. |
| `protocols` | `array` | Describes on which protocols the operations in this API can be invoked. |
| `apiVersionSet` | `object` | An API Version Set contains the common configuration for a set of API Versions relating  |
| `path` | `string` | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `displayName` | `string` | API name. Must be 1 to 300 characters long. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GatewayApi_ListByService` | `SELECT` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the APIs associated with a gateway. |
| `GatewayApi_CreateOrUpdate` | `INSERT` | `apiId, gatewayId, resourceGroupName, serviceName, subscriptionId` | Adds an API to the specified Gateway. |
| `GatewayApi_Delete` | `DELETE` | `apiId, gatewayId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified API from the specified Gateway. |
| `GatewayApi_GetEntityTag` | `EXEC` | `apiId, gatewayId, resourceGroupName, serviceName, subscriptionId` | Checks that API entity specified by identifier is associated with the Gateway entity. |
