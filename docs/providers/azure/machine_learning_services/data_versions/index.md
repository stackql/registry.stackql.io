---
title: data_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - data_versions
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
<tr><td><b>Name</b></td><td><code>data_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.data_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Data version base definition |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `DataVersions_List` | `SELECT` | `name, resourceGroupName, subscriptionId, workspaceName` |
| `DataVersions_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId, version, workspaceName, data__properties` |
| `DataVersions_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId, version, workspaceName` |
| `DataVersions_Get` | `EXEC` | `name, resourceGroupName, subscriptionId, version, workspaceName` |
