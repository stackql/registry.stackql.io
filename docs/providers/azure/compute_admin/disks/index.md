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
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `diskSku` | `string` | Disk Sku. |
| `managedBy` | `string` | Compute resource Uri which owns this disk. |
| `creationSourceUri` | `string` | The disk creation source uri. |
| `provisionSizeGB` | `integer` | The provision size of disk in GB. |
| `status` | `string` | Disk State. |
| `diskType` | `string` | Disk resource type. |
| `userResourceId` | `string` | The disk resource Uri from user view. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `sharePath` | `string` | The disk share path. |
| `exclusiveAllocatedSize` | `integer` | The exclusive allocated size for the disk. |
| `creationOption` | `string` | Disk creation option. |
| `diskId` | `string` | The disk id. |
| `actualSizeGB` | `integer` | The actual size of disk in GB. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Disks_List` | `SELECT` | `location, subscriptionId` | Returns a list of disks. |
| `Disks_Get` | `EXEC` | `diskId, location, subscriptionId` | Returns the disk. |
