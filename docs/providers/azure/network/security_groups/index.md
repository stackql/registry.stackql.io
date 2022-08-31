---
title: security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - security_groups
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
<tr><td><b>Name</b></td><td><code>security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.security_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `provisioningState` | `string` | The current provisioning state. |
| `flowLogs` | `array` | A collection of references to flow log resources. |
| `networkInterfaces` | `array` | A collection of references to network interfaces. |
| `defaultSecurityRules` | `array` | The default security rules of network security group. |
| `subnets` | `array` | A collection of references to subnets. |
| `securityRules` | `array` | A collection of security rules of the network security group. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `tags` | `object` | Resource tags. |
| `flushConnection` | `boolean` | When enabled, flows created from Network Security Group connections will be re-evaluated when rules are updates. Initial enablement will trigger re-evaluation. |
| `type` | `string` | Resource type. |
| `resourceGuid` | `string` | The resource GUID property of the network security group resource. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkSecurityGroups_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all network security groups in a resource group. |
| `NetworkSecurityGroups_ListAll` | `SELECT` | `subscriptionId` | Gets all network security groups in a subscription. |
| `NetworkSecurityGroups_CreateOrUpdate` | `INSERT` | `networkSecurityGroupName, resourceGroupName, subscriptionId` | Creates or updates a network security group in the specified resource group. |
| `NetworkSecurityGroups_Delete` | `DELETE` | `networkSecurityGroupName, resourceGroupName, subscriptionId` | Deletes the specified network security group. |
| `NetworkSecurityGroups_Get` | `EXEC` | `networkSecurityGroupName, resourceGroupName, subscriptionId` | Gets the specified network security group. |
| `NetworkSecurityGroups_UpdateTags` | `EXEC` | `networkSecurityGroupName, resourceGroupName, subscriptionId` | Updates a network security group tags. |
