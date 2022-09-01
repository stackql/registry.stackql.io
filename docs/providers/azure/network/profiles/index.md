---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
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
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `tags` | `object` | Resource tags. |
| `containerNetworkInterfaces` | `array` | List of child container network interfaces. |
| `location` | `string` | Resource location. |
| `provisioningState` | `string` | The current provisioning state. |
| `containerNetworkInterfaceConfigurations` | `array` | List of chid container network interface configurations. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `resourceGuid` | `string` | The resource GUID property of the network profile resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkProfiles_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all network profiles in a resource group. |
| `NetworkProfiles_ListAll` | `SELECT` | `subscriptionId` | Gets all the network profiles in a subscription. |
| `NetworkProfiles_CreateOrUpdate` | `INSERT` | `networkProfileName, resourceGroupName, subscriptionId` | Creates or updates a network profile. |
| `NetworkProfiles_Delete` | `DELETE` | `networkProfileName, resourceGroupName, subscriptionId` | Deletes the specified network profile. |
| `NetworkProfiles_Get` | `EXEC` | `networkProfileName, resourceGroupName, subscriptionId` | Gets the specified network profile in a specified resource group. |
| `NetworkProfiles_UpdateTags` | `EXEC` | `networkProfileName, resourceGroupName, subscriptionId` | Updates network profile tags. |
