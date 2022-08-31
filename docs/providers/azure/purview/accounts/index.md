---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - purview
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.purview.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the identifier. |
| `name` | `string` | Gets or sets the name. |
| `provisioningState` | `string` | Gets or sets the state of the provisioning. |
| `location` | `string` | Gets or sets the location. |
| `identity` | `object` | The Managed Identity of the resource |
| `publicNetworkAccess` | `string` | Gets or sets the public network access. |
| `createdBy` | `string` | Gets the creator of the entity. |
| `createdAt` | `string` | Gets the time at which the entity was created. |
| `cloudConnectors` | `object` | External Cloud Service connectors |
| `sku` | `object` | Gets or sets the Sku. |
| `friendlyName` | `string` | Gets or sets the friendly name. |
| `managedResources` | `object` | Gets the resource identifiers of the managed resources. |
| `privateEndpointConnections` | `array` | Gets the private endpoint connections information. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `createdByObjectId` | `string` | Gets the creators of the entity's object id. |
| `endpoints` | `object` | The URIs that are the public endpoints of the account. |
| `tags` | `object` | Tags on the azure resource. |
| `managedResourceGroupName` | `string` | Gets or sets the managed resource group name |
| `type` | `string` | Gets or sets the type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List accounts in ResourceGroup |
| `Accounts_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | List accounts in Subscription |
| `Accounts_CreateOrUpdate` | `INSERT` | `accountName, api-version, resourceGroupName, subscriptionId` | Creates or updates an account |
| `Accounts_Delete` | `DELETE` | `accountName, api-version, resourceGroupName, subscriptionId` | Deletes an account resource |
| `Accounts_AddRootCollectionAdmin` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Add the administrator for root collection associated with this account. |
| `Accounts_CheckNameAvailability` | `EXEC` | `api-version, subscriptionId` | Checks if account name is available. |
| `Accounts_Get` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Get an account |
| `Accounts_ListKeys` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | List the authorization keys associated with this account. |
| `Accounts_Update` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Updates an account |