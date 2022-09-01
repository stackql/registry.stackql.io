---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - iot_central
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_central.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `provisioningState` | `string` | The provisioning state of the application. |
| `networkRuleSets` | `object` | Network Rule Set Properties of this IoT Central application. |
| `tags` | `object` | Resource tags. |
| `sku` | `object` | Information about the SKU of the IoT Central application. |
| `publicNetworkAccess` | `string` | Whether requests from the public network are allowed. |
| `subdomain` | `string` | The subdomain of the application. |
| `privateEndpointConnections` | `array` | Private endpoint connections created on this IoT Central application. |
| `template` | `string` | The ID of the application template, which is a blueprint that defines the characteristics and behaviors of an application. Optional; if not specified, defaults to a blank blueprint and allows the application to be defined from scratch. |
| `applicationId` | `string` | The ID of the application. |
| `state` | `string` | The current state of the application. |
| `displayName` | `string` | The display name of the application. |
| `identity` | `object` | Managed service identity (either system assigned, or none) |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Apps_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get all the IoT Central Applications in a resource group. |
| `Apps_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Get all IoT Central Applications in a subscription. |
| `Apps_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, resourceName, subscriptionId, data__sku` | Create or update the metadata of an IoT Central application. The usual pattern to modify a property is to retrieve the IoT Central application metadata and security metadata, and then combine them with the modified values in a new body to update the IoT Central application. |
| `Apps_Delete` | `DELETE` | `api-version, resourceGroupName, resourceName, subscriptionId` | Delete an IoT Central application. |
| `Apps_CheckNameAvailability` | `EXEC` | `api-version, subscriptionId, data__name` | Check if an IoT Central application name is available. |
| `Apps_CheckSubdomainAvailability` | `EXEC` | `api-version, subscriptionId, data__name` | Check if an IoT Central application subdomain is available. |
| `Apps_Get` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get the metadata of an IoT Central application. |
| `Apps_ListTemplates` | `EXEC` | `api-version, subscriptionId` | Get all available application templates. |
| `Apps_Update` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Update the metadata of an IoT Central application. |
