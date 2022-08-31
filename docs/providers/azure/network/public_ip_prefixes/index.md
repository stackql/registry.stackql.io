---
title: public_ip_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ip_prefixes
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
<tr><td><b>Name</b></td><td><code>public_ip_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.public_ip_prefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `ipPrefix` | `string` | The allocated Prefix. |
| `natGateway` | `object` | Nat Gateway resource. |
| `tags` | `object` | Resource tags. |
| `sku` | `object` | SKU of a public IP prefix. |
| `publicIPAddressVersion` | `string` | IP address version. |
| `prefixLength` | `integer` | The Length of the Public IP Prefix. |
| `provisioningState` | `string` | The current provisioning state. |
| `publicIPAddresses` | `array` | The list of all referenced PublicIPAddresses. |
| `type` | `string` | Resource type. |
| `customIPPrefix` | `object` | Reference to another subresource. |
| `loadBalancerFrontendIpConfiguration` | `object` | Reference to another subresource. |
| `resourceGuid` | `string` | The resource GUID property of the public IP prefix resource. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `zones` | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
| `location` | `string` | Resource location. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `ipTags` | `array` | The list of tags associated with the public IP prefix. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PublicIPPrefixes_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all public IP prefixes in a resource group. |
| `PublicIPPrefixes_ListAll` | `SELECT` | `subscriptionId` | Gets all the public IP prefixes in a subscription. |
| `PublicIPPrefixes_CreateOrUpdate` | `INSERT` | `publicIpPrefixName, resourceGroupName, subscriptionId` | Creates or updates a static or dynamic public IP prefix. |
| `PublicIPPrefixes_Delete` | `DELETE` | `publicIpPrefixName, resourceGroupName, subscriptionId` | Deletes the specified public IP prefix. |
| `PublicIPPrefixes_Get` | `EXEC` | `publicIpPrefixName, resourceGroupName, subscriptionId` | Gets the specified public IP prefix in a specified resource group. |
| `PublicIPPrefixes_UpdateTags` | `EXEC` | `publicIpPrefixName, resourceGroupName, subscriptionId` | Updates public IP prefix tags. |
