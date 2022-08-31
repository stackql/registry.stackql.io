---
title: custom_ip_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_ip_prefixes
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
<tr><td><b>Name</b></td><td><code>custom_ip_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.custom_ip_prefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `publicIpPrefixes` | `array` | The list of all referenced PublicIpPrefixes. |
| `noInternetAdvertise` | `boolean` | Whether to Advertise the range to Internet. |
| `resourceGuid` | `string` | The resource GUID property of the custom IP prefix resource. |
| `type` | `string` | Resource type. |
| `commissionedState` | `string` | The commissioned state of the Custom IP Prefix. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `failedReason` | `string` | The reason why resource is in failed state. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `zones` | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
| `customIpPrefixParent` | `object` | Reference to another subresource. |
| `provisioningState` | `string` | The current provisioning state. |
| `signedMessage` | `string` | Signed message for WAN validation. |
| `cidr` | `string` | The prefix range in CIDR notation. Should include the start address and the prefix length. |
| `tags` | `object` | Resource tags. |
| `authorizationMessage` | `string` | Authorization message for WAN validation. |
| `childCustomIpPrefixes` | `array` | The list of all Children for IPv6 /48 CustomIpPrefix. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CustomIPPrefixes_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all custom IP prefixes in a resource group. |
| `CustomIPPrefixes_ListAll` | `SELECT` | `subscriptionId` | Gets all the custom IP prefixes in a subscription. |
| `CustomIPPrefixes_CreateOrUpdate` | `INSERT` | `customIpPrefixName, resourceGroupName, subscriptionId` | Creates or updates a custom IP prefix. |
| `CustomIPPrefixes_Delete` | `DELETE` | `customIpPrefixName, resourceGroupName, subscriptionId` | Deletes the specified custom IP prefix. |
| `CustomIPPrefixes_Get` | `EXEC` | `customIpPrefixName, resourceGroupName, subscriptionId` | Gets the specified custom IP prefix in a specified resource group. |
| `CustomIPPrefixes_UpdateTags` | `EXEC` | `customIpPrefixName, resourceGroupName, subscriptionId` | Updates custom IP prefix tags. |
