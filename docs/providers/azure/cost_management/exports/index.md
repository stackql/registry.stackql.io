---
title: exports
hide_title: false
hide_table_of_contents: false
keywords:
  - exports
  - cost_management
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
<tr><td><b>Name</b></td><td><code>exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.exports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `schedule` | `object` | The schedule associated with the export. |
| `type` | `string` | Resource type. |
| `eTag` | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Exports_List` | `SELECT` | `scope` | The operation to list all exports at the given scope. |
| `Exports_CreateOrUpdate` | `INSERT` | `exportName, scope` | The operation to create or update a export. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| `Exports_Delete` | `DELETE` | `exportName, scope` | The operation to delete a export. |
| `Exports_Execute` | `EXEC` | `exportName, scope` | The operation to execute an export. |
| `Exports_Get` | `EXEC` | `exportName, scope` | The operation to get the export for the defined scope by export name. |
| `Exports_GetExecutionHistory` | `EXEC` | `exportName, scope` | The operation to get the execution history of an export for the defined scope and export name. |