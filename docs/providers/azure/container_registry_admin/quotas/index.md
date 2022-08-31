---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
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
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry_admin.quotas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `capacityPerRegistryInGiB` | `integer` | Storage capacity (GiB) of each registry. |
| `numberOfRegistries` | `integer` | Total number of container registry accounts. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Quotas_List` | `SELECT` | `location, subscriptionId` | Returns a list of container registry quotas at the given location. |
| `Quotas_Delete` | `DELETE` | `location, quotaName, subscriptionId` | Delete an existing container registry quota |
| `Quotas_Get` | `EXEC` | `location, quotaName, subscriptionId` | Returns the specified container registry quota. |
