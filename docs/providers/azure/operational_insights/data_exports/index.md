---
title: data_exports
hide_title: false
hide_table_of_contents: false
keywords:
  - data_exports
  - operational_insights
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
<tr><td><b>Name</b></td><td><code>data_exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.data_exports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dataExportId` | `string` | The data export rule ID. |
| `destination` | `object` | Destination properties. |
| `enable` | `boolean` | Active when enabled. |
| `lastModifiedDate` | `string` | Date and time when the export was last modified. |
| `tableNames` | `array` | An array of tables to export, for example: [“Heartbeat, SecurityEvent”]. |
| `createdDate` | `string` | The latest data export rule modification time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataExports_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Lists the data export instances within a workspace. |
| `DataExports_CreateOrUpdate` | `INSERT` | `dataExportName, resourceGroupName, subscriptionId, workspaceName` | Create or update a data export. |
| `DataExports_Delete` | `DELETE` | `dataExportName, resourceGroupName, subscriptionId, workspaceName` | Deletes the specified data export in a given workspace.. |
| `DataExports_Get` | `EXEC` | `dataExportName, resourceGroupName, subscriptionId, workspaceName` | Gets a data export instance. |
