---
title: network_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_functions
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>network_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.network_functions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `skuType` | `string` | Sku type. |
| `networkFunctionUserConfigurations` | `array` | The network function configurations from the user. |
| `location` | `string` | The geo-location where the resource lives |
| `tags` | `object` | Resource tags. |
| `provisioningState` | `string` | The current provisioning state. |
| `managedApplicationParameters` | `object` | The parameters for the managed application. |
| `device` | `object` | Reference to another sub resource. |
| `vendorName` | `string` | The vendor name for the network function. Once set, it cannot be updated. |
| `serviceKey` | `string` | The service key for the network function resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `vendorProvisioningState` | `string` | The current vendor provisioning state. |
| `skuName` | `string` | The sku name for the network function. Once set, it cannot be updated. |
| `networkFunctionContainerConfigurations` | `object` | The network function container configurations from the user. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `managedApplication` | `object` | Reference to another sub resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkFunctions_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the network function resources in a resource group. |
| `NetworkFunctions_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the network functions in a subscription. |
| `NetworkFunctions_CreateOrUpdate` | `INSERT` | `networkFunctionName, resourceGroupName, subscriptionId` | Creates or updates a network function resource. This operation can take up to 6 hours to complete. This is expected service behavior. |
| `NetworkFunctions_Delete` | `DELETE` | `networkFunctionName, resourceGroupName, subscriptionId` | Deletes the specified network function resource. This operation can take up to 1 hour to complete. This is expected service behavior. |
| `NetworkFunctions_ExecuteRequest` | `EXEC` | `networkFunctionName, resourceGroupName, subscriptionId, data__requestMetadata, data__serviceEndpoint` | Execute a request to services on a network function. |
| `NetworkFunctions_Get` | `EXEC` | `networkFunctionName, resourceGroupName, subscriptionId` | Gets information about the specified network function resource. |
| `NetworkFunctions_UpdateTags` | `EXEC` | `networkFunctionName, resourceGroupName, subscriptionId` | Updates the tags for the network function resource. |
