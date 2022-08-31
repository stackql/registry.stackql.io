---
title: factories
hide_title: false
hide_table_of_contents: false
keywords:
  - factories
  - data_factory
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
<tr><td><b>Name</b></td><td><code>factories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.factories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `eTag` | `string` | Etag identifies change in the resource. |
| `type` | `string` | The resource type. |
| `identity` | `object` | Identity properties of the factory resource. |
| `publicNetworkAccess` | `string` | Whether or not public network access is allowed for the data factory. |
| `purviewConfiguration` | `object` | Purview configuration. |
| `location` | `string` | The resource location. |
| `encryption` | `object` | Definition of CMK for the factory. |
| `repoConfiguration` | `object` | Factory's git repo information. |
| `provisioningState` | `string` | Factory provisioning state, example Succeeded. |
| `version` | `string` | Version of the factory. |
| `createTime` | `string` | Time the factory was created in ISO8601 format. |
| `globalParameters` | `object` | Definition of all parameters for an entity. |
| `tags` | `object` | The resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Factories_List` | `SELECT` | `api-version, subscriptionId` | Lists factories under the specified subscription. |
| `Factories_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Lists factories. |
| `Factories_CreateOrUpdate` | `INSERT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Creates or updates a factory. |
| `Factories_Delete` | `DELETE` | `api-version, factoryName, resourceGroupName, subscriptionId` | Deletes a factory. |
| `Factories_ConfigureFactoryRepo` | `EXEC` | `api-version, locationId, subscriptionId` | Updates a factory's repo information. |
| `Factories_Get` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Gets a factory. |
| `Factories_GetDataPlaneAccess` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Get Data Plane access. |
| `Factories_GetGitHubAccessToken` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, data__gitHubAccessCode, data__gitHubAccessTokenBaseUrl` | Get GitHub Access Token. |
| `Factories_Update` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Updates a factory. |
