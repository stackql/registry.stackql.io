---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
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
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `requestedBackupStorageRedundancy` | `string` | The storage account type to be used to store backups for this database. |
| `creationDate` | `string` | The creation date of the database (ISO8601 format). |
| `highAvailabilityReplicaCount` | `integer` | The number of secondary replicas associated with the database that are used to provide high availability. Not applicable to a Hyperscale database within an elastic pool. |
| `currentSku` | `object` | An ARM Resource SKU. |
| `resumedDate` | `string` | The date when database was resumed by user action or database login (ISO8601 format). Null if the database is paused. |
| `maxSizeBytes` | `integer` | The max size of the database expressed in bytes. |
| `earliestRestoreDate` | `string` | This records the earliest start date and time that restore is available for this database (ISO8601 format). |
| `licenseType` | `string` | The license type to apply for this database. `LicenseIncluded` if you need a license, or `BasePrice` if you have a license and are eligible for the Azure Hybrid Benefit. |
| `sourceDatabaseId` | `string` | The resource identifier of the source database associated with create operation of this database. |
| `minCapacity` | `number` | Minimal capacity that database will always have allocated, if not paused |
| `location` | `string` | Resource location. |
| `currentServiceObjectiveName` | `string` | The current service level objective name of the database. |
| `elasticPoolId` | `string` | The resource identifier of the elastic pool containing this database. |
| `secondaryType` | `string` | The secondary type of the database if it is a secondary.  Valid values are Geo, Named and Standby. |
| `longTermRetentionBackupResourceId` | `string` | The resource identifier of the long term retention backup associated with create operation of this database. |
| `failoverGroupId` | `string` | Failover Group resource identifier that this database belongs to. |
| `maxLogSizeBytes` | `integer` | The max log size for this database. |
| `zoneRedundant` | `boolean` | Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. |
| `recoverableDatabaseId` | `string` | The resource identifier of the recoverable database associated with create operation of this database. |
| `catalogCollation` | `string` | Collation of the metadata catalog. |
| `tags` | `object` | Resource tags. |
| `readScale` | `string` | The state of read-only routing. If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica in the same region. Not applicable to a Hyperscale database within an elastic pool. |
| `managedBy` | `string` | Resource that manages the database. |
| `autoPauseDelay` | `integer` | Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled |
| `maintenanceConfigurationId` | `string` | Maintenance configuration id assigned to the database. This configuration defines the period when the maintenance updates will occur. |
| `kind` | `string` | Kind of database. This is metadata used for the Azure portal experience. |
| `sourceDatabaseDeletionDate` | `string` | Specifies the time that the database was deleted. |
| `isInfraEncryptionEnabled` | `boolean` | Infra encryption is enabled for this database. |
| `sampleName` | `string` | The name of the sample schema to apply when creating this database. |
| `requestedServiceObjectiveName` | `string` | The requested service level objective name of the database. |
| `pausedDate` | `string` | The date when database was paused by user configuration or action(ISO8601 format). Null if the database is ready. |
| `recoveryServicesRecoveryPointId` | `string` | The resource identifier of the recovery point associated with create operation of this database. |
| `databaseId` | `string` | The ID of the database. |
| `collation` | `string` | The collation of the database. |
| `federatedClientId` | `string` | The Client id used for cross tenant per database CMK scenario |
| `restorableDroppedDatabaseId` | `string` | The resource identifier of the restorable dropped database associated with create operation of this database. |
| `defaultSecondaryLocation` | `string` | The default secondary region for this database. |
| `createMode` | `string` | Specifies the mode of database creation.
| `restorePointInTime` | `string` | Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. |
| `isLedgerOn` | `boolean` | Whether or not this database is a ledger database, which means all tables in the database are ledger tables. Note: the value of this property cannot be changed after the database has been created. |
| `sku` | `object` | An ARM Resource SKU. |
| `currentBackupStorageRedundancy` | `string` | The storage account type used to store backups for this database. |
| `status` | `string` | The status of the database. |
| `sourceResourceId` | `string` | The resource identifier of the source associated with the create operation of this database.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Databases_ListByElasticPool` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Gets a list of databases in an elastic pool. |
| `Databases_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of databases. |
| `Databases_CreateOrUpdate` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, data__location` | Creates a new database or updates an existing database. |
| `Databases_Delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId` | Deletes the database. |
| `Databases_Export` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri` | Exports a database. |
| `Databases_Failover` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Failovers a database. |
| `Databases_Get` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a database. |
| `Databases_Import` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri` | Imports a bacpac into a new database. |
| `Databases_ListInaccessibleByServer` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets a list of inaccessible databases in a logical server |
| `Databases_ListMetricDefinitions` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Returns database metric definitions. |
| `Databases_ListMetrics` | `EXEC` | `$filter, databaseName, resourceGroupName, serverName, subscriptionId` | Returns database metrics. |
| `Databases_Pause` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Pauses a database. |
| `Databases_Rename` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, data__id` | Renames a database. |
| `Databases_Resume` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Resumes a database. |
| `Databases_Update` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Updates an existing database. |
| `Databases_UpgradeDataWarehouse` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Upgrades a data warehouse. |