---
title: container_registry_capacity
hide_title: false
hide_table_of_contents: false
keywords:
  - container_registry_capacity
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
<tr><td><b>Name</b></td><td><code>container_registry_capacity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry_admin.container_registry_capacity</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `allowPush` | `boolean` | Flag denotes if pushes are blocked for all registries. |
| `maximumCapacityInGiB` | `integer` | Total storage capacity (GiB) which can used by the registry. |
| `registriesConsumptionInGiB` | `number` | Total storage capacity (GiB) consumed by the registry. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ContainerRegistryCapacity_List` | `SELECT` | `location, subscriptionId` | Returns a list of container registry capacity properties. |
| `ContainerRegistryCapacity_Get` | `EXEC` | `capacityName, location, subscriptionId` | Returns container registry capacity property. |
