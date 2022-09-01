---
title: backup_short_term_retention_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_short_term_retention_policies
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
<tr><td><b>Name</b></td><td><code>backup_short_term_retention_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.backup_short_term_retention_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `retentionDays` | `integer` | The backup retention period in days. This is how many days Point-in-Time Restore will be supported. |
| `diffBackupIntervalInHours` | `integer` | The differential backup interval in hours. This is how many interval hours between each differential backup will be supported. This is only applicable to live databases but not dropped databases. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BackupShortTermRetentionPolicies_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a database's short term retention policy. |
| `BackupShortTermRetentionPolicies_CreateOrUpdate` | `INSERT` | `databaseName, policyName, resourceGroupName, serverName, subscriptionId` | Updates a database's short term retention policy. |
| `BackupShortTermRetentionPolicies_Get` | `EXEC` | `databaseName, policyName, resourceGroupName, serverName, subscriptionId` | Gets a database's short term retention policy. |
| `BackupShortTermRetentionPolicies_Update` | `EXEC` | `databaseName, policyName, resourceGroupName, serverName, subscriptionId` | Updates a database's short term retention policy. |
