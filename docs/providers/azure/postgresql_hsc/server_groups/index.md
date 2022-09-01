---
title: server_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - server_groups
  - postgresql_hsc
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
<tr><td><b>Name</b></td><td><code>server_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql_hsc.server_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `administratorLogin` | `string` | The administrator's login name of servers in server group. Can only be specified when the server is being created (and is required for creation). |
| `citusVersion` | `string` | The Citus version. |
| `availabilityZone` | `string` | Availability Zone information of the server group. |
| `enableMx` | `boolean` | If Citus MX is enabled or not for the server group. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `administratorLoginPassword` | `string` | The password of the administrator login. |
| `enableZfs` | `boolean` | If ZFS compression is enabled or not for the server group. |
| `tags` | `object` | Resource tags. |
| `state` | `string` | A state of a server group/server that is visible to user. |
| `pointInTimeUTC` | `string` | Restore point creation time (ISO8601 format), specifying the time to restore from. It's required when 'createMode' is 'PointInTimeRestore' |
| `sourceServerGroup` | `string` | The source server group id for read replica server groups. |
| `postgresqlVersion` | `string` | The PostgreSQL version. |
| `sourceSubscriptionId` | `string` | The source subscription id to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica' |
| `enableShardsOnCoordinator` | `boolean` | If shards on coordinator is enabled or not for the server group. |
| `sourceResourceGroupName` | `string` | The source resource group name to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica' |
| `sourceLocation` | `string` | The source server group location to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica' |
| `createMode` | `string` | The mode to create a new server group. |
| `backupRetentionDays` | `integer` | The backup retention days for server group. |
| `sourceServerGroupName` | `string` | The source server group name to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica' |
| `standbyAvailabilityZone` | `string` | Standby Availability Zone information of the server group. |
| `resourceProviderType` | `string` | The resource provider type of server group. |
| `serverRoleGroups` | `array` | The list of server role groups. |
| `maintenanceWindow` | `object` | Maintenance window of a server group. |
| `location` | `string` | The geo-location where the resource lives |
| `privateDnsZoneArguments` | `` | The private dns zone arguments for a server group. |
| `delegatedSubnetArguments` | `` | The delegated subnet arguments for a server group. |
| `readReplicas` | `array` | The array of read replica server groups. |
| `earliestRestoreTime` | `string` | The earliest restore point time (ISO8601 format) for server group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerGroups_List` | `SELECT` | `subscriptionId` | List all the server groups in a given subscription. |
| `ServerGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the server groups in a given resource group. |
| `ServerGroups_CreateOrUpdate` | `INSERT` | `resourceGroupName, serverGroupName, subscriptionId` | Creates a new server group with servers. |
| `ServerGroups_Delete` | `DELETE` | `resourceGroupName, serverGroupName, subscriptionId` | Deletes a server group together with servers in it. |
| `ServerGroups_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Check the availability of name for resource |
| `ServerGroups_Get` | `EXEC` | `resourceGroupName, serverGroupName, subscriptionId` | Gets information about a server group. |
| `ServerGroups_Restart` | `EXEC` | `resourceGroupName, serverGroupName, subscriptionId` | Restarts the server group. |
| `ServerGroups_Start` | `EXEC` | `resourceGroupName, serverGroupName, subscriptionId` | Starts the server group. |
| `ServerGroups_Stop` | `EXEC` | `resourceGroupName, serverGroupName, subscriptionId` | Stops the server group. |
| `ServerGroups_Update` | `EXEC` | `resourceGroupName, serverGroupName, subscriptionId` | Updates an existing server group. The request body can contain one to many of the properties present in the normal server group definition. |
