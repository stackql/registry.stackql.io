---
title: scope_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_maps
  - container_registry
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
<tr><td><b>Name</b></td><td><code>scope_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.scope_maps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `description` | `string` | The user friendly description of the scope map. |
| `provisioningState` | `string` | Provisioning state of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the scope map. E.g. BuildIn scope map. |
| `actions` | `array` | The list of scoped permissions for registry artifacts.<br />E.g. repositories/repository-name/content/read,<br />repositories/repository-name/metadata/write |
| `creationDate` | `string` | The creation date of scope map. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScopeMaps_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the scope maps for the specified container registry. |
| `ScopeMaps_Create` | `INSERT` | `registryName, resourceGroupName, scopeMapName, subscriptionId` | Creates a scope map for a container registry with the specified parameters. |
| `ScopeMaps_Delete` | `DELETE` | `registryName, resourceGroupName, scopeMapName, subscriptionId` | Deletes a scope map from a container registry. |
| `ScopeMaps_Get` | `EXEC` | `registryName, resourceGroupName, scopeMapName, subscriptionId` | Gets the properties of the specified scope map. |
| `ScopeMaps_Update` | `EXEC` | `registryName, resourceGroupName, scopeMapName, subscriptionId` | Updates a scope map with the specified parameters. |
