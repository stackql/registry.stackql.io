---
title: container_registry_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - container_registry_configuration
  - container_registry_admin
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
<tr><td><b>Name</b></td><td><code>container_registry_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry_admin.container_registry_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `maximumCapacityInGiB` | `integer` | Total storage capacity (GiB) which can used by the registry. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ContainerRegistryConfiguration_List` | `SELECT` | `location, subscriptionId` | Returns a list of configuration at the given location. |
| `ContainerRegistryConfiguration_Delete` | `DELETE` | `configurationName, location, subscriptionId` | Delete an existing container registry configuration |
| `ContainerRegistryConfiguration_Get` | `EXEC` | `configurationName, location, subscriptionId` | Returns the specified configuration details. |
| `ContainerRegistryConfiguration_Put` | `EXEC` | `configurationName, location, subscriptionId` | Configure container registry overall configuration properties. |