---
title: restorable_dropped_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_dropped_databases
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
<tr><td><b>Name</b></td><td><code>restorable_dropped_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.restorable_dropped_databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `maxSizeBytes` | `integer` | The max size of the database expressed in bytes. |
| `deletionDate` | `string` | The deletion date of the database (ISO8601 format). |
| `location` | `string` | Resource location. |
| `databaseName` | `string` | The name of the database. |
| `backupStorageRedundancy` | `string` | The storage account type used to store backups for this database. |
| `earliestRestoreDate` | `string` | The earliest restore date of the database (ISO8601 format). |
| `sku` | `object` | An ARM Resource SKU. |
| `tags` | `object` | Resource tags. |
| `creationDate` | `string` | The creation date of the database (ISO8601 format). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RestorableDroppedDatabases_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of restorable dropped databases. |
| `RestorableDroppedDatabases_Get` | `EXEC` | `resourceGroupName, restorableDroppedDatabaseId, serverName, subscriptionId` | Gets a restorable dropped database. |
