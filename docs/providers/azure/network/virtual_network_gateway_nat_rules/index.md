---
title: virtual_network_gateway_nat_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateway_nat_rules
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateway_nat_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_network_gateway_nat_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `externalMappings` | `array` | The private IP address external mapping for NAT. |
| `provisioningState` | `string` | The current provisioning state. |
| `ipConfigurationId` | `string` | The IP Configuration ID this NAT rule applies to. |
| `internalMappings` | `array` | The private IP address internal mapping for NAT. |
| `mode` | `string` | The Source NAT direction of a VPN NAT. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworkGatewayNatRules_ListByVirtualNetworkGateway` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Retrieves all nat rules for a particular virtual network gateway. |
| `VirtualNetworkGatewayNatRules_CreateOrUpdate` | `INSERT` | `natRuleName, resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Creates a nat rule to a scalable virtual network gateway if it doesn't exist else updates the existing nat rules. |
| `VirtualNetworkGatewayNatRules_Delete` | `DELETE` | `natRuleName, resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Deletes a nat rule. |
| `VirtualNetworkGatewayNatRules_Get` | `EXEC` | `natRuleName, resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Retrieves the details of a nat rule. |