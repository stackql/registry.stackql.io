---
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
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
<tr><td><b>Name</b></td><td><code>backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.backup_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `weeklyBackupsToKeep` | `integer` | Weekly backups count to keep |
| `tags` | `object` | Resource tags. |
| `volumesAssigned` | `integer` | Volumes using current backup policy |
| `dailyBackupsToKeep` | `integer` | Daily backups count to keep |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `monthlyBackupsToKeep` | `integer` | Monthly backups count to keep |
| `volumeBackups` | `array` | A list of volumes assigned to this policy |
| `backupPolicyId` | `string` | Backup Policy Resource ID |
| `enabled` | `boolean` | The property to decide policy is enabled or not |
| `provisioningState` | `string` | Azure lifecycle management |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BackupPolicies_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List backup policies for Netapp Account |
| `BackupPolicies_Create` | `INSERT` | `accountName, backupPolicyName, resourceGroupName, subscriptionId, data__location` | Create a backup policy for Netapp Account |
| `BackupPolicies_Delete` | `DELETE` | `accountName, backupPolicyName, resourceGroupName, subscriptionId` | Delete backup policy |
| `BackupPolicies_Get` | `EXEC` | `accountName, backupPolicyName, resourceGroupName, subscriptionId` | Get a particular backup Policy |
| `BackupPolicies_Update` | `EXEC` | `accountName, backupPolicyName, resourceGroupName, subscriptionId` | Patch a backup policy for Netapp Account |
