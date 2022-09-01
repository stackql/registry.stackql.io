---
title: virtual_network_taps
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_taps
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
<tr><td><b>Name</b></td><td><code>virtual_network_taps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_network_taps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `provisioningState` | `string` | The current provisioning state. |
| `destinationLoadBalancerFrontEndIPConfiguration` | `object` | Frontend IP address of the load balancer. |
| `destinationPort` | `integer` | The VXLAN destination port that will receive the tapped traffic. |
| `resourceGuid` | `string` | The resource GUID property of the virtual network tap resource. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `networkInterfaceTapConfigurations` | `array` | Specifies the list of resource IDs for the network interface IP configuration that needs to be tapped. |
| `tags` | `object` | Resource tags. |
| `destinationNetworkInterfaceIPConfiguration` | `object` | IPConfiguration in a network interface. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworkTaps_ListAll` | `SELECT` | `subscriptionId` | Gets all the VirtualNetworkTaps in a subscription. |
| `VirtualNetworkTaps_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the VirtualNetworkTaps in a subscription. |
| `VirtualNetworkTaps_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, tapName` | Creates or updates a Virtual Network Tap. |
| `VirtualNetworkTaps_Delete` | `DELETE` | `resourceGroupName, subscriptionId, tapName` | Deletes the specified virtual network tap. |
| `VirtualNetworkTaps_Get` | `EXEC` | `resourceGroupName, subscriptionId, tapName` | Gets information about the specified virtual network tap. |
| `VirtualNetworkTaps_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, tapName` | Updates an VirtualNetworkTap tags. |
