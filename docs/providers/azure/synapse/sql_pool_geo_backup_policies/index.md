---
title: sql_pool_geo_backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_geo_backup_policies
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_geo_backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_geo_backup_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Backup policy location. |
| `state` | `string` | The state of the geo backup policy. |
| `storageType` | `string` | The storage type of the geo backup policy. |
| `kind` | `string` | Kind of geo backup policy.  This is metadata used for the Azure portal experience. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPoolGeoBackupPolicies_List` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get list of SQL pool geo backup policies |
| `SqlPoolGeoBackupPolicies_CreateOrUpdate` | `INSERT` | `geoBackupPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Updates a SQL Pool geo backup policy. |
| `SqlPoolGeoBackupPolicies_Get` | `EXEC` | `geoBackupPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get the specified SQL pool geo backup policy |