---
title: managed_instance_long_term_retention_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_long_term_retention_policies
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
<tr><td><b>Name</b></td><td><code>managed_instance_long_term_retention_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_long_term_retention_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `monthlyRetention` | `string` | The monthly retention policy for an LTR backup in an ISO 8601 format. |
| `weekOfYear` | `integer` | The week of year to take the yearly backup in an ISO 8601 format. |
| `weeklyRetention` | `string` | The weekly retention policy for an LTR backup in an ISO 8601 format. |
| `yearlyRetention` | `string` | The yearly retention policy for an LTR backup in an ISO 8601 format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstanceLongTermRetentionPolicies_ListByDatabase` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a database's long term retention policy. |
| `ManagedInstanceLongTermRetentionPolicies_CreateOrUpdate` | `INSERT` | `databaseName, managedInstanceName, policyName, resourceGroupName, subscriptionId` | Sets a managed database's long term retention policy. |
| `ManagedInstanceLongTermRetentionPolicies_Get` | `EXEC` | `databaseName, managedInstanceName, policyName, resourceGroupName, subscriptionId` | Gets a managed database's long term retention policy. |