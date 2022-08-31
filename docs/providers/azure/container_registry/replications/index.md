---
title: replications
hide_title: false
hide_table_of_contents: false
keywords:
  - replications
  - container_registry
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
<tr><td><b>Name</b></td><td><code>replications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.replications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `status` | `object` | The status of an Azure resource at the time the operation was called. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
| `provisioningState` | `string` | The provisioning state of the replication at the time the operation was called. |
| `tags` | `object` | The tags of the resource. |
| `zoneRedundancy` | `string` | Whether or not zone redundancy is enabled for this container registry replication |
| `regionEndpointEnabled` | `boolean` | Specifies whether the replication's regional endpoint is enabled. Requests will not be routed to a replication whose regional endpoint is disabled, however its data will continue to be synced with other replications. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Replications_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the replications for the specified container registry. |
| `Replications_Create` | `INSERT` | `registryName, replicationName, resourceGroupName, subscriptionId` | Creates a replication for a container registry with the specified parameters. |
| `Replications_Delete` | `DELETE` | `registryName, replicationName, resourceGroupName, subscriptionId` | Deletes a replication from a container registry. |
| `Replications_Get` | `EXEC` | `registryName, replicationName, resourceGroupName, subscriptionId` | Gets the properties of the specified replication. |
| `Replications_Update` | `EXEC` | `registryName, replicationName, resourceGroupName, subscriptionId` | Updates a replication for a container registry with the specified parameters. |
