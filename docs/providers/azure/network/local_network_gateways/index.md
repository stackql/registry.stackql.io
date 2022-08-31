---
title: local_network_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - local_network_gateways
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
<tr><td><b>Name</b></td><td><code>local_network_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.local_network_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `fqdn` | `string` | FQDN of local network gateway. |
| `resourceGuid` | `string` | The resource GUID property of the local network gateway resource. |
| `gatewayIpAddress` | `string` | IP address of local network gateway. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
| `localNetworkAddressSpace` | `object` | AddressSpace contains an array of IP address ranges that can be used by subnets of the virtual network. |
| `bgpSettings` | `object` | BGP settings details. |
| `provisioningState` | `string` | The current provisioning state. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LocalNetworkGateways_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the local network gateways in a resource group. |
| `LocalNetworkGateways_CreateOrUpdate` | `INSERT` | `localNetworkGatewayName, resourceGroupName, subscriptionId` | Creates or updates a local network gateway in the specified resource group. |
| `LocalNetworkGateways_Delete` | `DELETE` | `localNetworkGatewayName, resourceGroupName, subscriptionId` | Deletes the specified local network gateway. |
| `LocalNetworkGateways_Get` | `EXEC` | `localNetworkGatewayName, resourceGroupName, subscriptionId` | Gets the specified local network gateway in a resource group. |
| `LocalNetworkGateways_UpdateTags` | `EXEC` | `localNetworkGatewayName, resourceGroupName, subscriptionId` | Updates a local network gateway tags. |