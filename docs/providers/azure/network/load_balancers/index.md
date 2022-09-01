---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
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
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `resourceGuid` | `string` | The resource GUID property of the load balancer resource. |
| `sku` | `object` | SKU of a load balancer. |
| `frontendIPConfigurations` | `array` | Object representing the frontend IPs to be used for the load balancer. |
| `tags` | `object` | Resource tags. |
| `probes` | `array` | Collection of probe objects used in the load balancer. |
| `provisioningState` | `string` | The current provisioning state. |
| `inboundNatPools` | `array` | Defines an external port range for inbound NAT to a single backend port on NICs associated with a load balancer. Inbound NAT rules are created automatically for each NIC associated with the Load Balancer using an external port from this range. Defining an Inbound NAT pool on your Load Balancer is mutually exclusive with defining inbound NAT rules. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machines cannot reference an inbound NAT pool. They have to reference individual inbound NAT rules. |
| `inboundNatRules` | `array` | Collection of inbound NAT Rules used by a load balancer. Defining inbound NAT rules on your load balancer is mutually exclusive with defining an inbound NAT pool. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machines cannot reference an Inbound NAT pool. They have to reference individual inbound NAT rules. |
| `location` | `string` | Resource location. |
| `outboundRules` | `array` | The outbound rules. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `loadBalancingRules` | `array` | Object collection representing the load balancing rules Gets the provisioning. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `backendAddressPools` | `array` | Collection of backend address pools used by a load balancer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LoadBalancers_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the load balancers in a resource group. |
| `LoadBalancers_ListAll` | `SELECT` | `subscriptionId` | Gets all the load balancers in a subscription. |
| `LoadBalancers_CreateOrUpdate` | `INSERT` | `loadBalancerName, resourceGroupName, subscriptionId` | Creates or updates a load balancer. |
| `LoadBalancers_Delete` | `DELETE` | `loadBalancerName, resourceGroupName, subscriptionId` | Deletes the specified load balancer. |
| `LoadBalancers_Get` | `EXEC` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets the specified load balancer. |
| `LoadBalancers_ListInboundNatRulePortMappings` | `EXEC` | `backendPoolName, groupName, loadBalancerName, subscriptionId` | List of inbound NAT rule port mappings. |
| `LoadBalancers_SwapPublicIpAddresses` | `EXEC` | `location, subscriptionId` | Swaps VIPs between two load balancers. |
| `LoadBalancers_UpdateTags` | `EXEC` | `loadBalancerName, resourceGroupName, subscriptionId` | Updates a load balancer tags. |
