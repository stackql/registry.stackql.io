---
title: inbound_nat_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_nat_rules
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
<tr><td><b>Name</b></td><td><code>inbound_nat_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.inbound_nat_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within the set of inbound NAT rules used by the load balancer. This name can be used to access the resource. |
| `provisioningState` | `string` | The current provisioning state. |
| `protocol` | `string` | The transport protocol for the endpoint. |
| `backendIPConfiguration` | `object` | IPConfiguration in a network interface. |
| `enableTcpReset` | `boolean` | Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP. |
| `enableFloatingIP` | `boolean` | Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint. |
| `backendAddressPool` | `object` | Reference to another subresource. |
| `idleTimeoutInMinutes` | `integer` | The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP. |
| `frontendIPConfiguration` | `object` | Reference to another subresource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `type` | `string` | Type of the resource. |
| `backendPort` | `integer` | The port used for the internal endpoint. Acceptable values range from 1 to 65535. |
| `frontendPort` | `integer` | The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values range from 1 to 65534. |
| `frontendPortRangeEnd` | `integer` | The port range end for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeStart. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534. |
| `frontendPortRangeStart` | `integer` | The port range start for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeEnd. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Acceptable values range from 1 to 65534. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `InboundNatRules_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the inbound NAT rules in a load balancer. |
| `InboundNatRules_CreateOrUpdate` | `INSERT` | `inboundNatRuleName, loadBalancerName, resourceGroupName, subscriptionId` | Creates or updates a load balancer inbound NAT rule. |
| `InboundNatRules_Delete` | `DELETE` | `inboundNatRuleName, loadBalancerName, resourceGroupName, subscriptionId` | Deletes the specified load balancer inbound NAT rule. |
| `InboundNatRules_Get` | `EXEC` | `inboundNatRuleName, loadBalancerName, resourceGroupName, subscriptionId` | Gets the specified load balancer inbound NAT rule. |
