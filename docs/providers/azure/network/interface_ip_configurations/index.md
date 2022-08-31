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
| `primary` | `boolean` | Whether this is a primary customer address on the network interface. |
| `loadBalancerInboundNatRules` | `array` | A list of references of LoadBalancerInboundNatRules. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `virtualNetworkTaps` | `array` | The reference to Virtual Network Taps. |
| `applicationGatewayBackendAddressPools` | `array` | The reference to ApplicationGatewayBackendAddressPool resource. |
| `type` | `string` | Resource type. |
| `provisioningState` | `string` | The current provisioning state. |
| `loadBalancerBackendAddressPools` | `array` | The reference to LoadBalancerBackendAddressPool resource. |
| `subnet` | `object` | Subnet in a virtual network resource. |
| `privateIPAllocationMethod` | `string` | IP address allocation method. |
| `privateIPAddressVersion` | `string` | IP address version. |
| `privateIPAddress` | `string` | Private IP address of the IP configuration. |
| `applicationSecurityGroups` | `array` | Application security groups in which the IP configuration is included. |
| `gatewayLoadBalancer` | `object` | Reference to another subresource. |
| `privateLinkConnectionProperties` | `object` | PrivateLinkConnection properties for the network interface. |
| `publicIPAddress` | `object` | Public IP address resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkInterfaceIPConfigurations_List` | `SELECT` | `networkInterfaceName, resourceGroupName, subscriptionId` | Get all ip configurations in a network interface. |
| `NetworkInterfaceIPConfigurations_Get` | `EXEC` | `ipConfigurationName, networkInterfaceName, resourceGroupName, subscriptionId` | Gets the specified network interface ip configuration. |
