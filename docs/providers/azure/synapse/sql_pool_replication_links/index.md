---
title: sql_pool_replication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_replication_links
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
<tr><td><b>Name</b></td><td><code>sql_pool_replication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_replication_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `partnerRole` | `string` | The role of the partner Sql pool in the replication link. |
| `replicationMode` | `string` | Replication mode of this replication link. |
| `partnerLocation` | `string` | The Azure Region of the partner Sql pool. |
| `startTime` | `string` | The start time for the replication link. |
| `type` | `string` | Type of resource this is. |
| `partnerDatabase` | `string` | The name of the partner Sql pool. |
| `role` | `string` | The role of the Sql pool in the replication link. |
| `partnerServer` | `string` | The name of the workspace hosting the partner Sql pool. |
| `percentComplete` | `integer` | The percentage of seeding complete for the replication link. |
| `isTerminationAllowed` | `boolean` | Legacy value indicating whether termination is allowed.  Currently always returns true. |
| `replicationState` | `string` | The replication state for the replication link. |
| `location` | `string` | Location of the workspace that contains this firewall rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPoolReplicationLinks_List` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Lists a Sql pool's replication links. |
| `SqlPoolReplicationLinks_GetByName` | `EXEC` | `linkId, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get SQL pool replication link by name. |
