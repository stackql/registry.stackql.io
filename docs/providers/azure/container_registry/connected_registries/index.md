---
title: connected_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_registries
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
<tr><td><b>Name</b></td><td><code>connected_registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.connected_registries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `mode` | `string` | The mode of the connected registry resource that indicates the permissions of the registry. |
| `logging` | `object` | The logging properties of the connected registry. |
| `parent` | `object` | The properties of the connected registry parent. |
| `clientTokenIds` | `array` | The list of the ACR token resource IDs used to authenticate clients to the connected registry. |
| `notificationsList` | `array` | The list of notifications subscription information for the connected registry. |
| `statusDetails` | `array` | The list of current statuses of the connected registry. |
| `loginServer` | `object` | The login server properties of the connected registry. |
| `provisioningState` | `string` | Provisioning state of the resource. |
| `activation` | `object` | The activation properties of the connected registry. |
| `version` | `string` | The current version of ACR runtime on the connected registry. |
| `lastActivityTime` | `string` | The last activity time of the connected registry. |
| `type` | `string` | The type of the resource. |
| `connectionState` | `string` | The current connection state of the connected registry. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConnectedRegistries_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all connected registries for the specified container registry. |
| `ConnectedRegistries_Create` | `INSERT` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Creates a connected registry for a container registry with the specified parameters. |
| `ConnectedRegistries_Delete` | `DELETE` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Deletes a connected registry from a container registry. |
| `ConnectedRegistries_Deactivate` | `EXEC` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Deactivates the connected registry instance. |
| `ConnectedRegistries_Get` | `EXEC` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Gets the properties of the connected registry. |
| `ConnectedRegistries_Update` | `EXEC` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Updates a connected registry with the specified parameters. |
