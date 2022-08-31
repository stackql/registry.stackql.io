---
title: load_balancer_load_balancing_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_load_balancing_rules
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
<tr><td><b>Name</b></td><td><code>load_balancer_load_balancing_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancer_load_balancing_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within the set of load balancing rules used by the load balancer. This name can be used to access the resource. |
| `loadDistribution` | `string` | The load distribution policy for this rule. |
| `disableOutboundSnat` | `boolean` | Configures SNAT for the VMs in the backend pool to use the publicIP address specified in the frontend of the load balancing rule. |
| `frontendIPConfiguration` | `object` | Reference to another subresource. |
| `backendAddressPool` | `object` | Reference to another subresource. |
| `protocol` | `string` | The transport protocol for the endpoint. |
| `enableTcpReset` | `boolean` | Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP. |
| `probe` | `object` | Reference to another subresource. |
| `provisioningState` | `string` | The current provisioning state. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `idleTimeoutInMinutes` | `integer` | The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP. |
| `backendPort` | `integer` | The port used for internal connections on the endpoint. Acceptable values are between 0 and 65535. Note that value 0 enables "Any Port". |
| `backendAddressPools` | `array` | An array of references to pool of DIPs. |
| `enableFloatingIP` | `boolean` | Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint. |
| `frontendPort` | `integer` | The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values are between 0 and 65534. Note that value 0 enables "Any Port". |
| `type` | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LoadBalancerLoadBalancingRules_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the load balancing rules in a load balancer. |
| `LoadBalancerLoadBalancingRules_Get` | `EXEC` | `loadBalancerName, loadBalancingRuleName, resourceGroupName, subscriptionId` | Gets the specified load balancer load balancing rule. |
