---
title: virtual_network_gateway_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateway_connections
  - network_admin
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateway_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network_admin.virtual_network_gateway_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `subscriptionId` | `string` | Subscription Id of the Virtual Network Gateway Connection. |
| `connectionState` | `object` | Virtual Network Gateway Connection state. |
| `location` | `string` | Region location of resource. |
| `virtualNetworkGatewayName` | `string` | Name of the associated Virtual Network Gateway. |
| `tags` | `object` | List of key value pairs. |
| `provisioningState` | `string` | Provisioning State of the Virtual Network Gateway Connection. |
| `sku` | `string` | SKU of the associated Virtual Network Gateway. |
| `capacityReserved` | `number` | Gateway capacity reserved by this connection. |
| `virtualNetworkGatewayIPAddress` | `string` | IP address of the associated Virtual Network Gateway. |
| `resourceGroup` | `string` | Resource Group of the Virtual Network Gateway Connection. |
| `totalStampCapacity` | `number` | Total amount of Gateway capacity that is available on this stamp. |
| `localNetworkGatewayIPAddress` | `string` | IP address of the associated Local Network Gateway. |
| `type` | `string` | Type of resource. |
| `localNetworkGatewayName` | `string` | Name of the associated Local Network Gateway. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `VirtualNetworkGatewayConnections_List` | `SELECT` | `subscriptionId` |
