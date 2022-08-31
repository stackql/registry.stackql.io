---
title: api
hide_title: false
hide_table_of_contents: false
keywords:
  - api
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
<tr><td><b>Name</b></td><td><code>api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `path` | `string` | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. |
| `displayName` | `string` | API name. Must be 1 to 300 characters long. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `protocols` | `array` | Describes on which protocols the operations in this API can be invoked. |
| `sourceApiId` | `string` | API identifier of the source API. |
| `apiVersionSet` | `object` | An API Version Set contains the common configuration for a set of API Versions relating  |
| `serviceUrl` | `string` | Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Api_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all APIs of the API Management service instance. |
| `Api_CreateOrUpdate` | `INSERT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Creates new or updates existing specified API of the API Management service instance. |
| `Api_Delete` | `DELETE` | `If-Match, apiId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified API of the API Management service instance. |
| `Api_Get` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the API specified by its identifier. |
| `Api_GetEntityTag` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the API specified by its identifier. |
| `Api_ListByTags` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of apis associated with tags. |
| `Api_Update` | `EXEC` | `If-Match, apiId, resourceGroupName, serviceName, subscriptionId` | Updates the specified API of the API Management service instance. |
