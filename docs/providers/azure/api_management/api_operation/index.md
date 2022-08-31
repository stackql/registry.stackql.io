---
title: api_operation
hide_title: false
hide_table_of_contents: false
keywords:
  - api_operation
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
<tr><td><b>Name</b></td><td><code>api_operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_operation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `urlTemplate` | `string` | Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date={date} |
| `displayName` | `string` | Operation Name. |
| `method` | `string` | A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiOperation_ListByApi` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the operations for the specified API. |
| `ApiOperation_CreateOrUpdate` | `INSERT` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Creates a new operation in the API or updates an existing one. |
| `ApiOperation_Delete` | `DELETE` | `If-Match, apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified operation in the API. |
| `ApiOperation_Get` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the API Operation specified by its identifier. |
| `ApiOperation_GetEntityTag` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the API operation specified by its identifier. |
| `ApiOperation_Update` | `EXEC` | `If-Match, apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the operation in the API specified by its identifier. |
