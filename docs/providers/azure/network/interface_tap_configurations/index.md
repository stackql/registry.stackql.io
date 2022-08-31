---
title: interface_tap_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - interface_tap_configurations
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
<tr><td><b>Name</b></td><td><code>interface_tap_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.interface_tap_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `type` | `string` | Sub Resource type. |
| `virtualNetworkTap` | `object` | Virtual Network Tap resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `provisioningState` | `string` | The current provisioning state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkInterfaceTapConfigurations_List` | `SELECT` | `networkInterfaceName, resourceGroupName, subscriptionId` | Get all Tap configurations in a network interface. |
| `NetworkInterfaceTapConfigurations_CreateOrUpdate` | `INSERT` | `networkInterfaceName, resourceGroupName, subscriptionId, tapConfigurationName` | Creates or updates a Tap configuration in the specified NetworkInterface. |
| `NetworkInterfaceTapConfigurations_Delete` | `DELETE` | `networkInterfaceName, resourceGroupName, subscriptionId, tapConfigurationName` | Deletes the specified tap configuration from the NetworkInterface. |
| `NetworkInterfaceTapConfigurations_Get` | `EXEC` | `networkInterfaceName, resourceGroupName, subscriptionId, tapConfigurationName` | Get the specified tap configuration on a network interface. |