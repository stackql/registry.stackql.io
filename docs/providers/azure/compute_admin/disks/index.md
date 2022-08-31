---
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
  - compute_admin
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
<tr><td><b>Name</b></td><td><code>disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute_admin.disks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `diskId` | `string` | The disk id. |
| `exclusiveAllocatedSize` | `integer` | The exclusive allocated size for the disk. |
| `actualSizeGB` | `integer` | The actual size of disk in GB. |
| `managedBy` | `string` | Compute resource Uri which owns this disk. |
| `creationSourceUri` | `string` | The disk creation source uri. |
| `diskSku` | `string` | Disk Sku. |
| `status` | `string` | Disk State. |
| `provisionSizeGB` | `integer` | The provision size of disk in GB. |
| `userResourceId` | `string` | The disk resource Uri from user view. |
| `creationOption` | `string` | Disk creation option. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `diskType` | `string` | Disk resource type. |
| `sharePath` | `string` | The disk share path. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Disks_List` | `SELECT` | `location, subscriptionId` | Returns a list of disks. |
| `Disks_Get` | `EXEC` | `diskId, location, subscriptionId` | Returns the disk. |
