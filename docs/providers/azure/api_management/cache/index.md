---
title: cache
hide_title: false
hide_table_of_contents: false
keywords:
  - cache
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
<tr><td><b>Name</b></td><td><code>cache</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.cache</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | Cache description |
| `resourceId` | `string` | Original uri of entity in external system cache points to |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `useFromLocation` | `string` | Location identifier to use cache from (should be either 'default' or valid Azure region identifier) |
| `connectionString` | `string` | Runtime connection string to cache |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Cache_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of all external Caches in the specified service instance. |
| `Cache_CreateOrUpdate` | `INSERT` | `cacheId, resourceGroupName, serviceName, subscriptionId` | Creates or updates an External Cache to be used in Api Management instance. |
| `Cache_Delete` | `DELETE` | `If-Match, cacheId, resourceGroupName, serviceName, subscriptionId` | Deletes specific Cache. |
| `Cache_Get` | `EXEC` | `cacheId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Cache specified by its identifier. |
| `Cache_GetEntityTag` | `EXEC` | `cacheId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the Cache specified by its identifier. |
| `Cache_Update` | `EXEC` | `If-Match, cacheId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the cache specified by its identifier. |