---
title: interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - interfaces
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
<tr><td><b>Name</b></td><td><code>interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.interfaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `auxiliaryMode` | `string` | Auxiliary mode of Network Interface resource. |
| `location` | `string` | Resource location. |
| `enableIPForwarding` | `boolean` | Indicates whether IP forwarding is enabled on this network interface. |
| `enableAcceleratedNetworking` | `boolean` | If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking. |
| `hostedWorkloads` | `array` | A list of references to linked BareMetal resources. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `primary` | `boolean` | Whether this is a primary network interface on a virtual machine. |
| `dnsSettings` | `object` | DNS settings of a network interface. |
| `ipConfigurations` | `array` | A list of IPConfigurations of the network interface. |
| `migrationPhase` | `string` | Migration phase of Network Interface resource. |
| `macAddress` | `string` | The MAC address of the network interface. |
| `nicType` | `string` | Type of Network Interface resource. |
| `privateLinkService` | `object` | Private link service resource. |
| `workloadType` | `string` | WorkloadType of the NetworkInterface for BareMetal resources |
| `vnetEncryptionSupported` | `boolean` | Whether the virtual machine this nic is attached to supports encryption. |
| `provisioningState` | `string` | The current provisioning state. |
| `tapConfigurations` | `array` | A list of TapConfigurations of the network interface. |
| `dscpConfiguration` | `object` | Reference to another subresource. |
| `resourceGuid` | `string` | The resource GUID property of the network interface resource. |
| `networkSecurityGroup` | `object` | NetworkSecurityGroup resource. |
| `virtualMachine` | `object` | Reference to another subresource. |
| `tags` | `object` | Resource tags. |
| `privateEndpoint` | `object` | Private endpoint resource. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkInterfaces_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all network interfaces in a resource group. |
| `NetworkInterfaces_ListAll` | `SELECT` | `subscriptionId` | Gets all network interfaces in a subscription. |
| `NetworkInterfaces_CreateOrUpdate` | `INSERT` | `networkInterfaceName, resourceGroupName, subscriptionId` | Creates or updates a network interface. |
| `NetworkInterfaces_Delete` | `DELETE` | `networkInterfaceName, resourceGroupName, subscriptionId` | Deletes the specified network interface. |
| `NetworkInterfaces_Get` | `EXEC` | `networkInterfaceName, resourceGroupName, subscriptionId` | Gets information about the specified network interface. |
| `NetworkInterfaces_GetCloudServiceNetworkInterface` | `EXEC` | `api-version, cloudServiceName, networkInterfaceName, resourceGroupName, roleInstanceName, subscriptionId` | Get the specified network interface in a cloud service. |
| `NetworkInterfaces_GetEffectiveRouteTable` | `EXEC` | `networkInterfaceName, resourceGroupName, subscriptionId` | Gets all route tables applied to a network interface. |
| `NetworkInterfaces_GetVirtualMachineScaleSetIpConfiguration` | `EXEC` | `api-version, ipConfigurationName, networkInterfaceName, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex` | Get the specified network interface ip configuration in a virtual machine scale set. |
| `NetworkInterfaces_GetVirtualMachineScaleSetNetworkInterface` | `EXEC` | `api-version, networkInterfaceName, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex` | Get the specified network interface in a virtual machine scale set. |
| `NetworkInterfaces_ListCloudServiceNetworkInterfaces` | `EXEC` | `api-version, cloudServiceName, resourceGroupName, subscriptionId` | Gets all network interfaces in a cloud service. |
| `NetworkInterfaces_ListCloudServiceRoleInstanceNetworkInterfaces` | `EXEC` | `api-version, cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId` | Gets information about all network interfaces in a role instance in a cloud service. |
| `NetworkInterfaces_ListEffectiveNetworkSecurityGroups` | `EXEC` | `networkInterfaceName, resourceGroupName, subscriptionId` | Gets all network security groups applied to a network interface. |
| `NetworkInterfaces_ListVirtualMachineScaleSetIpConfigurations` | `EXEC` | `api-version, networkInterfaceName, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex` | Get the specified network interface ip configuration in a virtual machine scale set. |
| `NetworkInterfaces_ListVirtualMachineScaleSetNetworkInterfaces` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineScaleSetName` | Gets all network interfaces in a virtual machine scale set. |
| `NetworkInterfaces_ListVirtualMachineScaleSetVMNetworkInterfaces` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex` | Gets information about all network interfaces in a virtual machine in a virtual machine scale set. |
| `NetworkInterfaces_UpdateTags` | `EXEC` | `networkInterfaceName, resourceGroupName, subscriptionId` | Updates a network interface tags. |
