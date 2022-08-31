---
title: registered_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_prefixes
  - peering
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
<tr><td><b>Name</b></td><td><code>registered_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.registered_prefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `prefix` | `string` | The customer's prefix from which traffic originates. |
| `prefixValidationState` | `string` | The prefix validation state. |
| `provisioningState` | `string` | The provisioning state of the resource. |
| `type` | `string` | The type of the resource. |
| `errorMessage` | `string` | The error message associated with the validation state, if any. |
| `peeringServicePrefixKey` | `string` | The peering service prefix key that is to be shared with the customer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegisteredPrefixes_ListByPeering` | `SELECT` | `peeringName, resourceGroupName, subscriptionId` | Lists all registered prefixes under the given subscription, resource group and peering. |
| `RegisteredPrefixes_CreateOrUpdate` | `INSERT` | `peeringName, registeredPrefixName, resourceGroupName, subscriptionId` | Creates a new registered prefix with the specified name under the given subscription, resource group and peering. |
| `RegisteredPrefixes_Delete` | `DELETE` | `peeringName, registeredPrefixName, resourceGroupName, subscriptionId` | Deletes an existing registered prefix with the specified name under the given subscription, resource group and peering. |
| `RegisteredPrefixes_Get` | `EXEC` | `peeringName, registeredPrefixName, resourceGroupName, subscriptionId` | Gets an existing registered prefix with the specified name under the given subscription, resource group and peering. |
| `RegisteredPrefixes_Validate` | `EXEC` | `peeringName, registeredPrefixName, resourceGroupName, subscriptionId` | Validates an existing registered prefix with the specified name under the given subscription, resource group and peering. |
