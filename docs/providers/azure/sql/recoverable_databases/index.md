---
title: recoverable_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - recoverable_databases
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
<tr><td><b>Name</b></td><td><code>recoverable_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.recoverable_databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `elasticPoolName` | `string` | The elastic pool name of the database |
| `lastAvailableBackupDate` | `string` | The last available backup date of the database (ISO8601 format) |
| `serviceLevelObjective` | `string` | The service level objective name of the database |
| `edition` | `string` | The edition of the database |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RecoverableDatabases_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of recoverable databases |
| `RecoverableDatabases_Get` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a recoverable database, which is a resource representing a database's geo backup |