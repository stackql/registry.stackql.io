---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `provisioningState` | `string` | Azure lifecycle management |
| `snapshotId` | `string` | UUID v4 used to identify the Snapshot |
| `type` | `string` | Resource type |
| `created` | `string` | The creation date of the snapshot |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Snapshots_List` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all snapshots associated with the volume |
| `Snapshots_Create` | `INSERT` | `accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName, data__location` | Create the specified snapshot within the given volume |
| `Snapshots_Delete` | `DELETE` | `accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName` | Delete snapshot |
| `Snapshots_Get` | `EXEC` | `accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName` | Get details of the specified snapshot |
| `Snapshots_RestoreFiles` | `EXEC` | `accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName, data__filePaths` | Restore the specified files from the specified snapshot to the active filesystem |
| `Snapshots_Update` | `EXEC` | `accountName, poolName, resourceGroupName, snapshotName, subscriptionId, volumeName` | Patch a snapshot |