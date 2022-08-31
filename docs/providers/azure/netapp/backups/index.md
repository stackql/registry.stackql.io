---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - netapp
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `failureReason` | `string` | Failure reason |
| `backupType` | `string` | Type of backup Manual or Scheduled |
| `creationDate` | `string` | The creation date of the backup |
| `backupId` | `string` | UUID v4 used to identify the Backup |
| `label` | `string` | Label for backup |
| `type` | `string` | Resource type |
| `size` | `integer` | Size of backup |
| `useExistingSnapshot` | `boolean` | Manual backup an already existing snapshot. This will always be false for scheduled backups and true/false for manual backups |
| `volumeName` | `string` | Volume name |
| `location` | `string` | Resource location |
| `provisioningState` | `string` | Azure lifecycle management |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Backups_List` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all backups for a volume |
| `Backups_Create` | `INSERT` | `accountName, backupName, poolName, resourceGroupName, subscriptionId, volumeName, data__location` | Create a backup for the volume |
| `Backups_Delete` | `DELETE` | `accountName, backupName, poolName, resourceGroupName, subscriptionId, volumeName` | Delete a backup of the volume |
| `Backups_Get` | `EXEC` | `accountName, backupName, poolName, resourceGroupName, subscriptionId, volumeName` | Gets the specified backup of the volume |
| `Backups_GetStatus` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Get the status of the backup for a volume |
| `Backups_GetVolumeRestoreStatus` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Get the status of the restore for a volume |
| `Backups_Update` | `EXEC` | `accountName, backupName, poolName, resourceGroupName, subscriptionId, volumeName` | Patch a backup for the volume |
