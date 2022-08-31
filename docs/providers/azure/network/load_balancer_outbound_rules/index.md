---
title: load_balancer_outbound_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_outbound_rules
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
<tr><td><b>Name</b></td><td><code>load_balancer_outbound_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancer_outbound_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within the set of outbound rules used by the load balancer. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `backendAddressPool` | `object` | Reference to another subresource. |
| `idleTimeoutInMinutes` | `integer` | The timeout for the TCP idle connection. |
| `type` | `string` | Type of the resource. |
| `provisioningState` | `string` | The current provisioning state. |
| `frontendIPConfigurations` | `array` | The Frontend IP addresses of the load balancer. |
| `enableTcpReset` | `boolean` | Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP. |
| `allocatedOutboundPorts` | `integer` | The number of outbound ports to be used for NAT. |
| `protocol` | `string` | The protocol for the outbound rule in load balancer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LoadBalancerOutboundRules_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the outbound rules in a load balancer. |
| `LoadBalancerOutboundRules_Get` | `EXEC` | `loadBalancerName, outboundRuleName, resourceGroupName, subscriptionId` | Gets the specified load balancer outbound rule. |
