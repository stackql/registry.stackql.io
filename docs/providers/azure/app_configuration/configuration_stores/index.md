---
title: configuration_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_stores
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>configuration_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_configuration.configuration_stores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `softDeleteRetentionInDays` | `integer` | The amount of time in days that the configuration store will be retained when it is soft deleted. |
| `disableLocalAuth` | `boolean` | Disables all authentication methods other than AAD authentication. |
| `publicNetworkAccess` | `string` | Control permission for data plane traffic coming from public networks while private endpoint is enabled. |
| `identity` | `object` | An identity that can be associated with a resource. |
| `sku` | `object` | Describes a configuration store SKU. |
| `creationDate` | `string` | The creation date of configuration store. |
| `privateEndpointConnections` | `array` | The list of private endpoint connections that are set up for this resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `createMode` | `string` | Indicates whether the configuration store need to be recovered. |
| `encryption` | `object` | The encryption settings for a configuration store. |
| `provisioningState` | `string` | The provisioning state of the configuration store. |
| `enablePurgeProtection` | `boolean` | Property specifying whether protection against purge is enabled for this configuration store. |
| `tags` | `object` | Resource tags. |
| `endpoint` | `string` | The DNS endpoint where the configuration store API will be available. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConfigurationStores_List` | `SELECT` | `subscriptionId` | Lists the configuration stores for a given subscription. |
| `ConfigurationStores_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the configuration stores for a given resource group. |
| `ConfigurationStores_Create` | `INSERT` | `configStoreName, resourceGroupName, subscriptionId, data__location, data__sku` | Creates a configuration store with the specified parameters. |
| `ConfigurationStores_Delete` | `DELETE` | `configStoreName, resourceGroupName, subscriptionId` | Deletes a configuration store. |
| `ConfigurationStores_Get` | `EXEC` | `configStoreName, resourceGroupName, subscriptionId` | Gets the properties of the specified configuration store. |
| `ConfigurationStores_GetDeleted` | `EXEC` | `configStoreName, location, subscriptionId` | Gets a deleted Azure app configuration store. |
| `ConfigurationStores_ListDeleted` | `EXEC` | `subscriptionId` | Gets information about the deleted configuration stores in a subscription. |
| `ConfigurationStores_ListKeys` | `EXEC` | `configStoreName, resourceGroupName, subscriptionId` | Lists the access key for the specified configuration store. |
| `ConfigurationStores_PurgeDeleted` | `EXEC` | `configStoreName, location, subscriptionId` | Permanently deletes the specified configuration store. |
| `ConfigurationStores_RegenerateKey` | `EXEC` | `configStoreName, resourceGroupName, subscriptionId` | Regenerates an access key for the specified configuration store. |
| `ConfigurationStores_Update` | `EXEC` | `configStoreName, resourceGroupName, subscriptionId` | Updates a configuration store with the specified parameters. |
