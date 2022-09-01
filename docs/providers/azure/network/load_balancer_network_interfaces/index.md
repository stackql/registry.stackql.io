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
| `privateLinkService` | `object` | Private link service resource. |
| `hostedWorkloads` | `array` | A list of references to linked BareMetal resources. |
| `location` | `string` | Resource location. |
| `enableIPForwarding` | `boolean` | Indicates whether IP forwarding is enabled on this network interface. |
| `macAddress` | `string` | The MAC address of the network interface. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `type` | `string` | Resource type. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `tags` | `object` | Resource tags. |
| `dnsSettings` | `object` | DNS settings of a network interface. |
| `tapConfigurations` | `array` | A list of TapConfigurations of the network interface. |
| `primary` | `boolean` | Whether this is a primary network interface on a virtual machine. |
| `provisioningState` | `string` | The current provisioning state. |
| `workloadType` | `string` | WorkloadType of the NetworkInterface for BareMetal resources |
| `privateEndpoint` | `object` | Private endpoint resource. |
| `vnetEncryptionSupported` | `boolean` | Whether the virtual machine this nic is attached to supports encryption. |
| `auxiliaryMode` | `string` | Auxiliary mode of Network Interface resource. |
| `enableAcceleratedNetworking` | `boolean` | If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking. |
| `networkSecurityGroup` | `object` | NetworkSecurityGroup resource. |
| `resourceGuid` | `string` | The resource GUID property of the network interface resource. |
| `virtualMachine` | `object` | Reference to another subresource. |
| `ipConfigurations` | `array` | A list of IPConfigurations of the network interface. |
| `dscpConfiguration` | `object` | Reference to another subresource. |
| `migrationPhase` | `string` | Migration phase of Network Interface resource. |
| `nicType` | `string` | Type of Network Interface resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `LoadBalancerNetworkInterfaces_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` |
