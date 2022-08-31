---
title: virtual_hub_ip_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_ip_configuration
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
<tr><td><b>Name</b></td><td><code>virtual_hub_ip_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_hub_ip_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the Ip Configuration. |
| `privateIPAllocationMethod` | `string` | IP address allocation method. |
| `type` | `string` | Ipconfiguration type. |
| `privateIPAddress` | `string` | The private IP address of the IP configuration. |
| `publicIPAddress` | `object` | Public IP address resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `subnet` | `object` | Subnet in a virtual network resource. |
| `provisioningState` | `string` | The current provisioning state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualHubIpConfiguration_List` | `SELECT` | `resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of all VirtualHubIpConfigurations. |
| `VirtualHubIpConfiguration_CreateOrUpdate` | `INSERT` | `ipConfigName, resourceGroupName, subscriptionId, virtualHubName` | Creates a VirtualHubIpConfiguration resource if it doesn't exist else updates the existing VirtualHubIpConfiguration. |
| `VirtualHubIpConfiguration_Delete` | `DELETE` | `ipConfigName, resourceGroupName, subscriptionId, virtualHubName` | Deletes a VirtualHubIpConfiguration. |
| `VirtualHubIpConfiguration_Get` | `EXEC` | `ipConfigName, resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of a Virtual Hub Ip configuration. |