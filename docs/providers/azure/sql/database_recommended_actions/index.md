---
title: database_recommended_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - database_recommended_actions
  - sql
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
<tr><td><b>Name</b></td><td><code>database_recommended_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_recommended_actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `recommendationReason` | `string` | Gets the reason for recommending this action. e.g., DuplicateIndex |
| `score` | `integer` | Gets the impact of this recommended action. Possible values are 1 - Low impact, 2 - Medium Impact and 3 - High Impact |
| `details` | `object` | Gets additional details specific to this recommended action. |
| `lastRefresh` | `string` | Gets time when this recommended action was last refreshed. |
| `state` | `object` | Contains information of current state for an Azure SQL Database, Server or Elastic Pool Recommended Action. |
| `isArchivedAction` | `boolean` | Gets if this recommended action was suggested some time ago but user chose to ignore this and system added a new recommended action again. |
| `estimatedImpact` | `array` | Gets the estimated impact info for this recommended action e.g., Estimated CPU gain, Estimated Disk Space change |
| `revertActionInitiatedBy` | `string` | Gets if approval for reverting this recommended action was given by user/system. |
| `revertActionInitiatedTime` | `string` | Gets the time when this recommended action was approved for revert. |
| `executeActionInitiatedBy` | `string` | Gets if approval for applying this recommended action was given by user/system. |
| `timeSeries` | `array` | Gets the time series info of metrics for this recommended action e.g., CPU consumption time series |
| `executeActionDuration` | `string` | Gets the time taken for applying this recommended action on user resource. e.g., time taken for index creation |
| `executeActionInitiatedTime` | `string` | Gets the time when this recommended action was approved for execution. |
| `errorDetails` | `object` | Contains error information for an Azure SQL Database, Server or Elastic Pool Recommended Action. |
| `implementationDetails` | `object` | Contains information for manual implementation for an Azure SQL Database, Server or Elastic Pool Recommended Action. |
| `isExecutableAction` | `boolean` | Gets if this recommended action is actionable by user |
| `revertActionDuration` | `string` | Gets the time taken for reverting changes of this recommended action on user resource. e.g., time taken for dropping the created index. |
| `observedImpact` | `array` | Gets the observed/actual impact info for this recommended action e.g., Actual CPU gain, Actual Disk Space change |
| `linkedObjects` | `array` | Gets the linked objects, if any. |
| `isRevertableAction` | `boolean` | Gets if changes applied by this recommended action can be reverted by user |
| `kind` | `string` | Resource kind. |
| `executeActionStartTime` | `string` | Gets the time when system started applying this recommended action on the user resource. e.g., index creation start time |
| `revertActionStartTime` | `string` | Gets the time when system started reverting changes of this recommended action on user resource. e.g., time when index drop is executed. |
| `validSince` | `string` | Gets the time since when this recommended action is valid. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseRecommendedActions_ListByDatabaseAdvisor` | `SELECT` | `advisorName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets list of Database Recommended Actions. |
| `DatabaseRecommendedActions_Get` | `EXEC` | `advisorName, databaseName, recommendedActionName, resourceGroupName, serverName, subscriptionId` | Gets a database recommended action. |
| `DatabaseRecommendedActions_Update` | `EXEC` | `advisorName, databaseName, recommendedActionName, resourceGroupName, serverName, subscriptionId` | Updates a database recommended action. |
