---
title: managed_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_databases
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
<tr><td><b>Name</b></td><td><code>managed_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `lastBackupName` | `string` | Last backup file name for restore of this managed database. |
| `autoCompleteRestore` | `boolean` | Whether to auto complete restore of this managed database. |
| `recoverableDatabaseId` | `string` | The resource identifier of the recoverable database associated with create operation of this database. |
| `location` | `string` | Resource location. |
| `storageContainerSasToken` | `string` | Conditional. If createMode is RestoreExternalBackup, this value is required. Specifies the storage container sas token. |
| `failoverGroupId` | `string` | Instance Failover Group resource identifier that this managed database belongs to. |
| `earliestRestorePoint` | `string` | Earliest restore point in time for point in time restore. |
| `longTermRetentionBackupResourceId` | `string` | The name of the Long Term Retention backup to be used for restore of this managed database. |
| `status` | `string` | Status of the database. |
| `collation` | `string` | Collation of the managed database. |
| `defaultSecondaryLocation` | `string` | Geo paired region. |
| `tags` | `object` | Resource tags. |
| `storageContainerUri` | `string` | Conditional. If createMode is RestoreExternalBackup, this value is required. Specifies the uri of the storage container where backups for this restore are stored. |
| `sourceDatabaseId` | `string` | The resource identifier of the source database associated with create operation of this database. |
| `restorePointInTime` | `string` | Conditional. If createMode is PointInTimeRestore, this value is required. Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. |
| `catalogCollation` | `string` | Collation of the metadata catalog. |
| `restorableDroppedDatabaseId` | `string` | The restorable dropped database resource id to restore when creating this database. |
| `creationDate` | `string` | Creation date of the database. |
| `createMode` | `string` | Managed database create mode. PointInTimeRestore: Create a database by restoring a point in time backup of an existing database. SourceDatabaseName, SourceManagedInstanceName and PointInTime must be specified. RestoreExternalBackup: Create a database by restoring from external backup files. Collation, StorageContainerUri and StorageContainerSasToken must be specified. Recovery: Creates a database by restoring a geo-replicated backup. RecoverableDatabaseId must be specified as the recoverable database resource ID to restore. RestoreLongTermRetentionBackup: Create a database by restoring from a long term retention backup (longTermRetentionBackupResourceId required). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedDatabases_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed databases. |
| `ManagedDatabases_CreateOrUpdate` | `INSERT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__location` | Creates a new database or updates an existing database. |
| `ManagedDatabases_Delete` | `DELETE` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Deletes a managed database. |
| `ManagedDatabases_CompleteRestore` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__lastBackupName` | Completes the restore operation on a managed database. |
| `ManagedDatabases_Get` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed database. |
| `ManagedDatabases_ListInaccessibleByInstance` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of inaccessible managed databases in a managed instance |
| `ManagedDatabases_Update` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Updates an existing database. |
