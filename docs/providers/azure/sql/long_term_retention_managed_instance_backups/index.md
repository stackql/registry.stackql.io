---
title: long_term_retention_managed_instance_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_managed_instance_backups
  - sql
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
<tr><td><b>Name</b></td><td><code>long_term_retention_managed_instance_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.long_term_retention_managed_instance_backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `databaseName` | `string` | The name of the database the backup belong to |
| `managedInstanceCreateTime` | `string` | The create time of the instance. |
| `managedInstanceName` | `string` | The managed instance that the backup database belongs to. |
| `backupExpirationTime` | `string` | The time the long term retention backup will expire. |
| `backupStorageRedundancy` | `string` | The storage redundancy type of the backup |
| `backupTime` | `string` | The time the backup was taken |
| `databaseDeletionTime` | `string` | The delete time of the database |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LongTermRetentionManagedInstanceBackups_ListByDatabase` | `SELECT` | `databaseName, locationName, managedInstanceName, subscriptionId` | Lists all long term retention backups for a managed database. |
| `LongTermRetentionManagedInstanceBackups_ListByInstance` | `SELECT` | `locationName, managedInstanceName, subscriptionId` | Lists the long term retention backups for a given managed instance. |
| `LongTermRetentionManagedInstanceBackups_ListByLocation` | `SELECT` | `locationName, subscriptionId` | Lists the long term retention backups for managed databases in a given location. |
| `LongTermRetentionManagedInstanceBackups_ListByResourceGroupDatabase` | `SELECT` | `databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId` | Lists all long term retention backups for a managed database. |
| `LongTermRetentionManagedInstanceBackups_ListByResourceGroupInstance` | `SELECT` | `locationName, managedInstanceName, resourceGroupName, subscriptionId` | Lists the long term retention backups for a given managed instance. |
| `LongTermRetentionManagedInstanceBackups_ListByResourceGroupLocation` | `SELECT` | `locationName, resourceGroupName, subscriptionId` | Lists the long term retention backups for managed databases in a given location. |
| `LongTermRetentionManagedInstanceBackups_Delete` | `DELETE` | `backupName, databaseName, locationName, managedInstanceName, subscriptionId` | Deletes a long term retention backup. |
| `LongTermRetentionManagedInstanceBackups_DeleteByResourceGroup` | `DELETE` | `backupName, databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId` | Deletes a long term retention backup. |
| `LongTermRetentionManagedInstanceBackups_Get` | `EXEC` | `backupName, databaseName, locationName, managedInstanceName, subscriptionId` | Gets a long term retention backup for a managed database. |
| `LongTermRetentionManagedInstanceBackups_GetByResourceGroup` | `EXEC` | `backupName, databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a long term retention backup for a managed database. |
