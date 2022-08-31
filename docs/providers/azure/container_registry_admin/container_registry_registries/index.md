---
title: container_registry_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - container_registry_registries
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
<tr><td><b>Name</b></td><td><code>container_registry_registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry_admin.container_registry_registries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `registrySizeInBytes` | `integer` | Total storage capacity (GiB) used by the registry. |
| `resourceGroup` | `string` | ResourceGroup where container registry is present. |
| `creationDate` | `string` | The time at which the registry created. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `registryId` | `string` | Container registry id. |
| `subscriptionId` | `string` | SubscriptionId where container registry is present. |
| `location` | `string` | Container registry location. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ContainerRegistryRegistries_List` | `SELECT` | `location, subscriptionId` |
