---
title: global_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - global_schema
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
<tr><td><b>Name</b></td><td><code>global_schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.global_schema</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | Free-form schema entity description. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `value` | `` | Json-encoded string for non json-based schema. |
| `document` | `object` | Global Schema Document Properties. |
| `schemaType` | `string` | Schema Type. Immutable. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GlobalSchema_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of schemas registered with service instance. |
| `GlobalSchema_CreateOrUpdate` | `INSERT` | `resourceGroupName, schemaId, serviceName, subscriptionId` | Creates new or updates existing specified Schema of the API Management service instance. |
| `GlobalSchema_Delete` | `DELETE` | `If-Match, resourceGroupName, schemaId, serviceName, subscriptionId` | Deletes specific Schema. |
| `GlobalSchema_Get` | `EXEC` | `resourceGroupName, schemaId, serviceName, subscriptionId` | Gets the details of the Schema specified by its identifier. |
| `GlobalSchema_GetEntityTag` | `EXEC` | `resourceGroupName, schemaId, serviceName, subscriptionId` | Gets the entity state (Etag) version of the Schema specified by its identifier. |
