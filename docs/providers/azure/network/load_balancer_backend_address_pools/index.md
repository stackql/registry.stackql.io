---
title: load_balancer_backend_address_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_backend_address_pools
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
<tr><td><b>Name</b></td><td><code>load_balancer_backend_address_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancer_backend_address_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within the set of backend address pools used by the load balancer. This name can be used to access the resource. |
| `type` | `string` | Type of the resource. |
| `outboundRule` | `object` | Reference to another subresource. |
| `tunnelInterfaces` | `array` | An array of gateway load balancer tunnel interfaces. |
| `inboundNatRules` | `array` | An array of references to inbound NAT rules that use this backend address pool. |
| `outboundRules` | `array` | An array of references to outbound rules that use this backend address pool. |
| `provisioningState` | `string` | The current provisioning state. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `loadBalancerBackendAddresses` | `array` | An array of backend addresses. |
| `location` | `string` | The location of the backend address pool. |
| `backendIPConfigurations` | `array` | An array of references to IP addresses defined in network interfaces. |
| `drainPeriodInSeconds` | `integer` | Amount of seconds Load Balancer waits for before sending RESET to client and backend address. |
| `loadBalancingRules` | `array` | An array of references to load balancing rules that use this backend address pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LoadBalancerBackendAddressPools_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the load balancer backed address pools. |
| `LoadBalancerBackendAddressPools_CreateOrUpdate` | `INSERT` | `backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId` | Creates or updates a load balancer backend address pool. |
| `LoadBalancerBackendAddressPools_Delete` | `DELETE` | `backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId` | Deletes the specified load balancer backend address pool. |
| `LoadBalancerBackendAddressPools_Get` | `EXEC` | `backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId` | Gets load balancer backend address pool. |
