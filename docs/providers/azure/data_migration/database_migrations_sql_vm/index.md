---
title: database_migrations_sql_vm
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_sql_vm
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
<tr><td><b>Name</b></td><td><code>database_migrations_sql_vm</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_migration.database_migrations_sql_vm</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseMigrationsSqlVm_CreateOrUpdate` | `INSERT` | `resourceGroupName, sqlVirtualMachineName, subscriptionId, targetDbName` | Create a new database migration to a given SQL VM. |
| `DatabaseMigrationsSqlVm_Get` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId, targetDbName` | Retrieve the specified database migration for a given SQL VM. |
| `DatabaseMigrationsSqlVm_cancel` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId, targetDbName` | Stop in-progress database migration to SQL VM. |
| `DatabaseMigrationsSqlVm_cutover` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId, targetDbName` | Initiate cutover for in-progress online database migration to SQL VM. |
