---
title: database_migrations_sql_db
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_sql_db
  - data_migration
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
<tr><td><b>Name</b></td><td><code>database_migrations_sql_db</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_migration.database_migrations_sql_db</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseMigrationsSqlDb_CreateOrUpdate` | `INSERT` | `resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName` | Create or Update Database Migration resource. |
| `DatabaseMigrationsSqlDb_Delete` | `DELETE` | `resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName` | Delete Database Migration resource. |
| `DatabaseMigrationsSqlDb_Get` | `EXEC` | `resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName` | Retrieve the Database Migration resource. |
| `DatabaseMigrationsSqlDb_cancel` | `EXEC` | `resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName` | Stop on going migration for the database. |
