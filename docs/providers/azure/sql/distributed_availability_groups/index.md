---
title: distributed_availability_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - distributed_availability_groups
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
<tr><td><b>Name</b></td><td><code>distributed_availability_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.distributed_availability_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `targetReplicaId` | `string` | The target replica id |
| `sourceEndpoint` | `string` | The source endpoint |
| `secondaryAvailabilityGroupName` | `string` | The secondary availability group name |
| `linkState` | `string` | The link state |
| `sourceReplicaId` | `string` | The source replica id |
| `distributedAvailabilityGroupId` | `string` | The distributed availability group id |
| `lastHardenedLsn` | `string` | The last hardened lsn |
| `replicationMode` | `string` | The replication mode of a distributed availability group. Parameter will be ignored during link creation. |
| `primaryAvailabilityGroupName` | `string` | The primary availability group name |
| `targetDatabase` | `string` | The name of the target database |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DistributedAvailabilityGroups_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of a distributed availability groups in instance. |
| `DistributedAvailabilityGroups_CreateOrUpdate` | `INSERT` | `distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId` | Creates a distributed availability group between Sql On-Prem and Sql Managed Instance. |
| `DistributedAvailabilityGroups_Delete` | `DELETE` | `distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId` | Drops a distributed availability group between Sql On-Prem and Sql Managed Instance. |
| `DistributedAvailabilityGroups_Get` | `EXEC` | `distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a distributed availability group info. |
| `DistributedAvailabilityGroups_Update` | `EXEC` | `distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId` | Updates a distributed availability group replication mode. |
