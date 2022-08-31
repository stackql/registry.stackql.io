---
title: apply_update_for_resource_group
hide_title: false
hide_table_of_contents: false
keywords:
  - apply_update_for_resource_group
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
<tr><td><b>Name</b></td><td><code>apply_update_for_resource_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maintenance.apply_update_for_resource_group</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `status` | `string` | The status |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `lastUpdateTime` | `string` | Last Update time |
| `resourceId` | `string` | The resourceId |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ApplyUpdateForResourceGroup_List` | `SELECT` | `resourceGroupName, subscriptionId` |