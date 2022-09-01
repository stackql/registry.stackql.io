---
title: ip_allocations
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_allocations
  - network
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
<tr><td><b>Name</b></td><td><code>ip_allocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.ip_allocations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `prefix` | `string` | The address prefix for the IpAllocation. |
| `location` | `string` | Resource location. |
| `subnet` | `object` | Reference to another subresource. |
| `virtualNetwork` | `object` | Reference to another subresource. |
| `tags` | `object` | Resource tags. |
| `ipamAllocationId` | `string` | The IPAM allocation ID. |
| `allocationTags` | `object` | IpAllocation tags. |
| `prefixType` | `string` | IP address version. |
| `type` | `string` | Resource type. |
| `prefixLength` | `integer` | The address prefix length for the IpAllocation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IpAllocations_List` | `SELECT` | `subscriptionId` | Gets all IpAllocations in a subscription. |
| `IpAllocations_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all IpAllocations in a resource group. |
| `IpAllocations_CreateOrUpdate` | `INSERT` | `ipAllocationName, resourceGroupName, subscriptionId` | Creates or updates an IpAllocation in the specified resource group. |
| `IpAllocations_Delete` | `DELETE` | `ipAllocationName, resourceGroupName, subscriptionId` | Deletes the specified IpAllocation. |
| `IpAllocations_Get` | `EXEC` | `ipAllocationName, resourceGroupName, subscriptionId` | Gets the specified IpAllocation by resource group. |
| `IpAllocations_UpdateTags` | `EXEC` | `ipAllocationName, resourceGroupName, subscriptionId` | Updates a IpAllocation tags. |
