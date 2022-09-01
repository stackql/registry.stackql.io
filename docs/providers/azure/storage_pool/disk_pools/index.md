---
title: disk_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_pools
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>disk_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_pool.disk_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `provisioningState` | `string` | Provisioning state of the iSCSI Target. |
| `subnetId` | `string` | Azure Resource ID of a Subnet for the Disk Pool. |
| `availabilityZones` | `array` | Logical zone for Disk Pool resource; example: ["1"]. |
| `managedBy` | `string` | Azure resource id. Indicates if this resource is managed by another Azure resource. |
| `disks` | `array` | List of Azure Managed Disks to attach to a Disk Pool. |
| `sku` | `object` | Sku for ARM resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `managedByExtended` | `array` | List of Azure resource ids that manage this resource. |
| `additionalCapabilities` | `array` | List of additional capabilities for Disk Pool. |
| `status` | `string` | Operational status of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DiskPools_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of DiskPools in a resource group. |
| `DiskPools_ListBySubscription` | `SELECT` | `subscriptionId` | Gets a list of Disk Pools in a subscription |
| `DiskPools_CreateOrUpdate` | `INSERT` | `diskPoolName, resourceGroupName, subscriptionId, data__location, data__sku` | Create or Update Disk pool. This create or update operation can take 15 minutes to complete. This is expected service behavior. |
| `DiskPools_Delete` | `DELETE` | `diskPoolName, resourceGroupName, subscriptionId` | Delete a Disk pool; attached disks are not affected. This delete operation can take 10 minutes to complete. This is expected service behavior. |
| `DiskPools_Deallocate` | `EXEC` | `diskPoolName, resourceGroupName, subscriptionId` | Shuts down the Disk Pool and releases the compute resources. You are not billed for the compute resources that this Disk Pool uses. This operation can take 10 minutes to complete. This is expected service behavior. |
| `DiskPools_Get` | `EXEC` | `diskPoolName, resourceGroupName, subscriptionId` | Get a Disk pool. |
| `DiskPools_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `diskPoolName, resourceGroupName, subscriptionId` | Gets the network endpoints of all outbound dependencies of a Disk Pool |
| `DiskPools_Start` | `EXEC` | `diskPoolName, resourceGroupName, subscriptionId` | The operation to start a Disk Pool. This start operation can take 10 minutes to complete. This is expected service behavior. |
| `DiskPools_Update` | `EXEC` | `diskPoolName, resourceGroupName, subscriptionId` | Update a Disk pool. |
| `DiskPools_Upgrade` | `EXEC` | `diskPoolName, resourceGroupName, subscriptionId` | Upgrade replaces the underlying virtual machine hosts one at a time. This operation can take 10-15 minutes to complete. This is expected service behavior. |
