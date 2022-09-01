---
title: replication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_links
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
<tr><td><b>Name</b></td><td><code>replication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.replication_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `percentComplete` | `integer` | Seeding completion percentage for the link. |
| `replicationMode` | `string` | Replication mode. |
| `role` | `string` | Local replication role. |
| `isTerminationAllowed` | `boolean` | Whether the user is currently allowed to terminate the link. |
| `partnerRole` | `string` | Partner replication role. |
| `linkType` | `string` | Link type (GEO, NAMED, STANDBY). |
| `replicationState` | `string` | Replication state (PENDING, SEEDING, CATCHUP, SUSPENDED). |
| `partnerServer` | `string` | Resource partner server. |
| `startTime` | `string` | Time at which the link was created. |
| `partnerDatabase` | `string` | Resource partner database. |
| `partnerLocation` | `string` | Resource partner location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationLinks_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of replication links on database. |
| `ReplicationLinks_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of replication links. |
| `ReplicationLinks_Delete` | `DELETE` | `databaseName, linkId, resourceGroupName, serverName, subscriptionId` | Deletes the replication link. |
| `ReplicationLinks_Failover` | `EXEC` | `databaseName, linkId, resourceGroupName, serverName, subscriptionId` | Fails over from the current primary server to this server. |
| `ReplicationLinks_FailoverAllowDataLoss` | `EXEC` | `databaseName, linkId, resourceGroupName, serverName, subscriptionId` | Fails over from the current primary server to this server allowing data loss. |
| `ReplicationLinks_Get` | `EXEC` | `databaseName, linkId, resourceGroupName, serverName, subscriptionId` | Gets a replication link. |
