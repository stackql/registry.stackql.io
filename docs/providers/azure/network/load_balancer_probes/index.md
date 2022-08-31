---
title: load_balancer_probes
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_probes
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
<tr><td><b>Name</b></td><td><code>load_balancer_probes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.load_balancer_probes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within the set of probes used by the load balancer. This name can be used to access the resource. |
| `provisioningState` | `string` | The current provisioning state. |
| `port` | `integer` | The port for communicating the probe. Possible values range from 1 to 65535, inclusive. |
| `protocol` | `string` | The protocol of the end point. If 'Tcp' is specified, a received ACK is required for the probe to be successful. If 'Http' or 'Https' is specified, a 200 OK response from the specifies URI is required for the probe to be successful. |
| `type` | `string` | Type of the resource. |
| `loadBalancingRules` | `array` | The load balancer rules that use this probe. |
| `numberOfProbes` | `integer` | The number of probes where if no response, will result in stopping further traffic from being delivered to the endpoint. This values allows endpoints to be taken out of rotation faster or slower than the typical times used in Azure. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `intervalInSeconds` | `integer` | The interval, in seconds, for how frequently to probe the endpoint for health status. Typically, the interval is slightly less than half the allocated timeout period (in seconds) which allows two full probes before taking the instance out of rotation. The default value is 15, the minimum value is 5. |
| `requestPath` | `string` | The URI used for requesting health status from the VM. Path is required if a protocol is set to http. Otherwise, it is not allowed. There is no default value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LoadBalancerProbes_List` | `SELECT` | `loadBalancerName, resourceGroupName, subscriptionId` | Gets all the load balancer probes. |
| `LoadBalancerProbes_Get` | `EXEC` | `loadBalancerName, probeName, resourceGroupName, subscriptionId` | Gets load balancer probe. |
