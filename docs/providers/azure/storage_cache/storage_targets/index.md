---
title: storage_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_targets
  - storage_cache
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
<tr><td><b>Name</b></td><td><code>storage_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_cache.storage_targets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID of the Storage Target. |
| `name` | `string` | Schema for the name of resources served by this provider. Note that objects will contain an odata @id annotation as appropriate. This will contain the complete URL of the object. These names are case-preserving, but not case sensitive. |
| `type` | `string` | Type of the Storage Target; Microsoft.StorageCache/Cache/StorageTarget |
| `clfs` | `object` | Properties pertaining to the ClfsTarget |
| `unknown` | `object` | Properties pertaining to the UnknownTarget |
| `targetType` | `string` | Type of the Storage Target. |
| `junctions` | `array` | List of Cache namespace junctions to target for namespace associations. |
| `provisioningState` | `string` | ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property |
| `nfs3` | `object` | Properties pertaining to the Nfs3Target |
| `blobNfs` | `object` | Properties pertaining to the BlobNfsTarget. |
| `location` | `string` | Region name string. |
| `allocationPercentage` | `integer` | The percentage of cache space allocated for this storage target |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `state` | `string` | Storage target operational state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StorageTargets_ListByCache` | `SELECT` | `cacheName, resourceGroupName, subscriptionId` | Returns a list of Storage Targets for the specified Cache. |
| `StorageTargets_CreateOrUpdate` | `INSERT` | `cacheName, resourceGroupName, storageTargetName, subscriptionId` | Create or update a Storage Target. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the Cache is healthy again. |
| `StorageTargets_Delete` | `DELETE` | `cacheName, resourceGroupName, storageTargetName, subscriptionId` | Removes a Storage Target from a Cache. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual removal of the Storage Target may be delayed until the Cache is healthy again. Note that if the Cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted. |
| `StorageTargets_DnsRefresh` | `EXEC` | `cacheName, resourceGroupName, storageTargetName, subscriptionId` | Tells a storage target to refresh its DNS information. |
| `StorageTargets_Get` | `EXEC` | `cacheName, resourceGroupName, storageTargetName, subscriptionId` | Returns a Storage Target from a Cache. |