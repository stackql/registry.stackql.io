---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
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
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `lastPlanModifiedDate` | `string` | The timestamp that table plan was last modified (UTC). |
| `resultStatistics` | `object` | Search job execution statistics. |
| `provisioningState` | `string` | Table's current provisioning state. If set to 'updating', indicates a resource lock due to ongoing operation, forbidding any update to the table until the ongoing operation is concluded. |
| `schema` | `object` | Table's schema. |
| `plan` | `string` | Instruct the system how to handle and charge the logs ingested to this table. |
| `archiveRetentionInDays` | `integer` | The table data archive retention in days. Calculated as (totalRetentionInDays-retentionInDays) |
| `restoredLogs` | `object` | Restore parameters. |
| `searchResults` | `object` | Parameters of the search job that initiated this table. |
| `totalRetentionInDays` | `integer` | The table total retention in days, between 4 and 2555. Setting this property to -1 will default to table retention. |
| `retentionInDays` | `integer` | The table retention in days, between 4 and 730. Setting this property to -1 will default to the workspace retention. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Tables_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all the tables for the specified Log Analytics workspace. |
| `Tables_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Update or Create a Log Analytics workspace table. |
| `Tables_Delete` | `DELETE` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Delete a Log Analytics workspace table. |
| `Tables_Get` | `EXEC` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Gets a Log Analytics workspace table. |
| `Tables_Migrate` | `EXEC` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Migrate a Log Analytics table from support of the Data Collector API and Custom Fields features to support of Data Collection Rule-based Custom Logs. |
| `Tables_Update` | `EXEC` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Update a Log Analytics workspace table. |
