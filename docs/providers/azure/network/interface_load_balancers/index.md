---
title: interface_load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - interface_load_balancers
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
<tr><td><b>Name</b></td><td><code>interface_load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.interface_load_balancers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `provisioningState` | `string` | The current provisioning state. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `loadBalancingRules` | `array` | Object collection representing the load balancing rules Gets the provisioning. |
| `probes` | `array` | Collection of probe objects used in the load balancer. |
| `inboundNatRules` | `array` | Collection of inbound NAT Rules used by a load balancer. Defining inbound NAT rules on your load balancer is mutually exclusive with defining an inbound NAT pool. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machines cannot reference an Inbound NAT pool. They have to reference individual inbound NAT rules. |
| `sku` | `object` | SKU of a load balancer. |
| `location` | `string` | Resource location. |
| `backendAddressPools` | `array` | Collection of backend address pools used by a load balancer. |
| `inboundNatPools` | `array` | Defines an external port range for inbound NAT to a single backend port on NICs associated with a load balancer. Inbound NAT rules are created automatically for each NIC associated with the Load Balancer using an external port from this range. Defining an Inbound NAT pool on your Load Balancer is mutually exclusive with defining inbound NAT rules. Inbound NAT pools are referenced from virtual machine scale sets. NICs that are associated with individual virtual machines cannot reference an inbound NAT pool. They have to reference individual inbound NAT rules. |
| `resourceGuid` | `string` | The resource GUID property of the load balancer resource. |
| `frontendIPConfigurations` | `array` | Object representing the frontend IPs to be used for the load balancer. |
| `outboundRules` | `array` | The outbound rules. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `NetworkInterfaceLoadBalancers_List` | `SELECT` | `networkInterfaceName, resourceGroupName, subscriptionId` |
