---
title: apply_updates
hide_title: false
hide_table_of_contents: false
keywords:
  - apply_updates
  - maintenance
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
<tr><td><b>Name</b></td><td><code>apply_updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maintenance.apply_updates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `lastUpdateTime` | `string` | Last Update time |
| `resourceId` | `string` | The resourceId |
| `status` | `string` | The status |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApplyUpdates_List` | `SELECT` | `subscriptionId` |  |
| `ApplyUpdates_CreateOrUpdate` | `INSERT` | `providerName, resourceGroupName, resourceName, resourceType, subscriptionId` | Apply maintenance updates to resource |
| `ApplyUpdates_CreateOrUpdateParent` | `EXEC` | `providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | Apply maintenance updates to resource with parent |
| `ApplyUpdates_Get` | `EXEC` | `applyUpdateName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId` | Track maintenance updates to resource |
| `ApplyUpdates_GetParent` | `EXEC` | `applyUpdateName, providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | Track maintenance updates to resource with parent |
