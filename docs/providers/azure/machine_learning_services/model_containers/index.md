---
title: model_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - model_containers
  - machine_learning_services
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
<tr><td><b>Name</b></td><td><code>model_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.model_containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ModelContainers_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `ModelContainers_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId, workspaceName, data__properties` |
| `ModelContainers_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId, workspaceName` |
| `ModelContainers_Get` | `EXEC` | `name, resourceGroupName, subscriptionId, workspaceName` |
