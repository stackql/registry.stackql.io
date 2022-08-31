---
title: load_balancer_network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_network_interfaces
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
<tr><td><b>Name</b></td><td><code>load_balancer_network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancer_network_interfaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `privateEndpoint` | `object` | Private endpoint resource. |
| `nicType` | `string` | Type of Network Interface resource. |
| `resourceGuid` | `string` | The resource GUID property of the network interface resource. |
| `tapConfigurations` | `array` | A list of TapConfigurations of the network interface. |
| `virtualMachine` | `object` | Reference to another subresource. |
| `enableAcceleratedNetworking` | `boolean` | If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking. |
| `workloadType` | `string` | WorkloadType of the NetworkInterface for BareMetal resources |
| `enableIPForwarding` | `boolean` | Indicates whether IP forwarding is enabled on this network interface. |
| `tags` | `object` | Resource tags. |
| `vnetEncryptionSupported` | `boolean` | Whether the virtual machine this nic is attached to supports encryption. |
| `primary` | `boolean` | Whether this is a primary network interface on a virtual machine. |
| `dnsSettings` | `object` | DNS settings of a network interface. |
| `dscpConfiguration` | `object` | Reference to another subresource. |
| `provisioningState` | `string` | The current provisioning state. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `privateLinkService` | `object` | Private link service resource. |
| `ipConfigurations` | `array` | A list of IPConfigurations of the network interface. |
| `hostedWorkloads` | `array` | A list of references to linked BareMetal resources. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `networkSecurityGroup` | `object` | NetworkSecurityGroup resource. |
| `migrationPhase` | `string` | Migration phase of Network Interface resource. |
| `auxiliaryMode` | `string` | Auxiliary mode of Network Interface resource. |
| `location` | `string` | Resource location. |
| `macAddress` | `string` | The MAC address of the network interface. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `LoadBalancerNetworkInterfaces_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` |
