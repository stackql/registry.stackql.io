---
title: failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - failover_groups
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
<tr><td><b>Name</b></td><td><code>failover_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.failover_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `databases` | `array` | List of databases in the failover group. |
| `location` | `string` | Resource location. |
| `partnerServers` | `array` | List of partner server information for the failover group. |
| `readOnlyEndpoint` | `object` | Read-only endpoint of the failover group instance. |
| `readWriteEndpoint` | `object` | Read-write endpoint of the failover group instance. |
| `replicationRole` | `string` | Local replication role of the failover group instance. |
| `replicationState` | `string` | Replication state of the failover group instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FailoverGroups_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Lists the failover groups in a server. |
| `FailoverGroups_CreateOrUpdate` | `INSERT` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Creates or updates a failover group. |
| `FailoverGroups_Delete` | `DELETE` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Deletes a failover group. |
| `FailoverGroups_Failover` | `EXEC` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Fails over from the current primary server to this server. |
| `FailoverGroups_ForceFailoverAllowDataLoss` | `EXEC` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Fails over from the current primary server to this server. This operation might result in data loss. |
| `FailoverGroups_Get` | `EXEC` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Gets a failover group. |
| `FailoverGroups_Update` | `EXEC` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Updates a failover group. |
