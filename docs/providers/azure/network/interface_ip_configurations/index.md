---
title: interface_ip_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - interface_ip_configurations
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
<tr><td><b>Name</b></td><td><code>interface_ip_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.interface_ip_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `privateIPAllocationMethod` | `string` | IP address allocation method. |
| `subnet` | `object` | Subnet in a virtual network resource. |
| `loadBalancerBackendAddressPools` | `array` | The reference to LoadBalancerBackendAddressPool resource. |
| `applicationSecurityGroups` | `array` | Application security groups in which the IP configuration is included. |
| `publicIPAddress` | `object` | Public IP address resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `type` | `string` | Resource type. |
| `gatewayLoadBalancer` | `object` | Reference to another subresource. |
| `loadBalancerInboundNatRules` | `array` | A list of references of LoadBalancerInboundNatRules. |
| `provisioningState` | `string` | The current provisioning state. |
| `privateIPAddressVersion` | `string` | IP address version. |
| `privateIPAddress` | `string` | Private IP address of the IP configuration. |
| `virtualNetworkTaps` | `array` | The reference to Virtual Network Taps. |
| `applicationGatewayBackendAddressPools` | `array` | The reference to ApplicationGatewayBackendAddressPool resource. |
| `primary` | `boolean` | Whether this is a primary customer address on the network interface. |
| `privateLinkConnectionProperties` | `object` | PrivateLinkConnection properties for the network interface. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkInterfaceIPConfigurations_List` | `SELECT` | `networkInterfaceName, resourceGroupName, subscriptionId` | Get all ip configurations in a network interface. |
| `NetworkInterfaceIPConfigurations_Get` | `EXEC` | `ipConfigurationName, networkInterfaceName, resourceGroupName, subscriptionId` | Gets the specified network interface ip configuration. |
