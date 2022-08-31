---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - netapp
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
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `encryptionType` | `string` | Encryption type of the capacity pool, set encryption type for data at rest for this pool and all volumes in it. This value can only be set when creating new pool. |
| `poolId` | `string` | UUID v4 used to identify the Pool |
| `utilizedThroughputMibps` | `number` | Utilized throughput of pool in MiB/s |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `qosType` | `string` | The qos type of the pool |
| `serviceLevel` | `string` | The service level of the file system |
| `totalThroughputMibps` | `number` | Total throughput of pool in MiB/s |
| `coolAccess` | `boolean` | If enabled (true) the pool can contain cool Access enabled volumes. |
| `size` | `integer` | Provisioned size of the pool (in bytes). Allowed values are in 1TiB chunks (value must be multiply of 4398046511104). |
| `provisioningState` | `string` | Azure lifecycle management |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Pools_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List all capacity pools in the NetApp Account |
| `Pools_CreateOrUpdate` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId, data__location` | Create or Update a capacity pool |
| `Pools_Delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId` | Delete the specified capacity pool |
| `Pools_Get` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | Get details of the specified capacity pool |
| `Pools_Update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | Patch the specified capacity pool |
