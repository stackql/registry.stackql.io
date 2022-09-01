---
title: subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets
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
<tr><td><b>Name</b></td><td><code>subnets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.subnets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `addressPrefix` | `string` | The address prefix for the subnet. |
| `applicationGatewayIpConfigurations` | `array` | Application gateway IP configurations of virtual network resource. |
| `delegations` | `array` | An array of references to the delegations on the subnet. |
| `resourceNavigationLinks` | `array` | An array of references to the external resources using subnet. |
| `privateEndpointNetworkPolicies` | `string` | Enable or Disable apply network policies on private end point in the subnet. |
| `serviceEndpointPolicies` | `array` | An array of service endpoint policies. |
| `type` | `string` | Resource type. |
| `purpose` | `string` | A read-only string identifying the intention of use for this subnet based on delegations and other user-defined properties. |
| `serviceAssociationLinks` | `array` | An array of references to services injecting into this subnet. |
| `provisioningState` | `string` | The current provisioning state. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `natGateway` | `object` | Reference to another subresource. |
| `addressPrefixes` | `array` | List of address prefixes for the subnet. |
| `privateEndpoints` | `array` | An array of references to private endpoints. |
| `ipConfigurations` | `array` | An array of references to the network interface IP configurations using subnet. |
| `ipAllocations` | `array` | Array of IpAllocation which reference this subnet. |
| `privateLinkServiceNetworkPolicies` | `string` | Enable or Disable apply network policies on private link service in the subnet. |
| `ipConfigurationProfiles` | `array` | Array of IP configuration profiles which reference this subnet. |
| `serviceEndpoints` | `array` | An array of service endpoints. |
| `routeTable` | `object` | Route table resource. |
| `networkSecurityGroup` | `object` | NetworkSecurityGroup resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Subnets_List` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets all subnets in a virtual network. |
| `Subnets_CreateOrUpdate` | `INSERT` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` | Creates or updates a subnet in the specified virtual network. |
| `Subnets_Delete` | `DELETE` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` | Deletes the specified subnet. |
| `Subnets_Get` | `EXEC` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` | Gets the specified subnet by virtual network and resource group. |
| `Subnets_PrepareNetworkPolicies` | `EXEC` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` | Prepares a subnet by applying network intent policies. |
| `Subnets_UnprepareNetworkPolicies` | `EXEC` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` | Unprepares a subnet by removing network intent policies. |
