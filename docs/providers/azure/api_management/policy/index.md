---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
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
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.policy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `value` | `string` | Contents of the Policy as defined by the format. |
| `format` | `string` | Format of the policyContent. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Policy_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all the Global Policy definitions of the Api Management service. |
| `Policy_CreateOrUpdate` | `INSERT` | `policyId, resourceGroupName, serviceName, subscriptionId` | Creates or updates the global policy configuration of the Api Management service. |
| `Policy_Delete` | `DELETE` | `If-Match, policyId, resourceGroupName, serviceName, subscriptionId` | Deletes the global policy configuration of the Api Management Service. |
| `Policy_Get` | `EXEC` | `policyId, resourceGroupName, serviceName, subscriptionId` | Get the Global policy definition of the Api Management service. |
| `Policy_GetEntityTag` | `EXEC` | `policyId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the Global policy definition in the Api Management service. |
