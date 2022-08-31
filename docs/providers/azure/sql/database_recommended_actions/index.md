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
| `isRevertableAction` | `boolean` | Gets if changes applied by this recommended action can be reverted by user |
| `revertActionDuration` | `string` | Gets the time taken for reverting changes of this recommended action on user resource. e.g., time taken for dropping the created index. |
| `isExecutableAction` | `boolean` | Gets if this recommended action is actionable by user |
| `executeActionInitiatedTime` | `string` | Gets the time when this recommended action was approved for execution. |
| `revertActionInitiatedBy` | `string` | Gets if approval for reverting this recommended action was given by user/system. |
| `validSince` | `string` | Gets the time since when this recommended action is valid. |
| `lastRefresh` | `string` | Gets time when this recommended action was last refreshed. |
| `score` | `integer` | Gets the impact of this recommended action. Possible values are 1 - Low impact, 2 - Medium Impact and 3 - High Impact |
| `details` | `object` | Gets additional details specific to this recommended action. |
| `revertActionInitiatedTime` | `string` | Gets the time when this recommended action was approved for revert. |
| `recommendationReason` | `string` | Gets the reason for recommending this action. e.g., DuplicateIndex |
| `timeSeries` | `array` | Gets the time series info of metrics for this recommended action e.g., CPU consumption time series |
| `revertActionStartTime` | `string` | Gets the time when system started reverting changes of this recommended action on user resource. e.g., time when index drop is executed. |
| `implementationDetails` | `object` | Contains information for manual implementation for an Azure SQL Database, Server or Elastic Pool Recommended Action. |
| `observedImpact` | `array` | Gets the observed/actual impact info for this recommended action e.g., Actual CPU gain, Actual Disk Space change |
| `executeActionInitiatedBy` | `string` | Gets if approval for applying this recommended action was given by user/system. |
| `isArchivedAction` | `boolean` | Gets if this recommended action was suggested some time ago but user chose to ignore this and system added a new recommended action again. |
| `linkedObjects` | `array` | Gets the linked objects, if any. |
| `errorDetails` | `object` | Contains error information for an Azure SQL Database, Server or Elastic Pool Recommended Action. |
| `kind` | `string` | Resource kind. |
| `state` | `object` | Contains information of current state for an Azure SQL Database, Server or Elastic Pool Recommended Action. |
| `location` | `string` | Resource location. |
| `executeActionStartTime` | `string` | Gets the time when system started applying this recommended action on the user resource. e.g., index creation start time |
| `estimatedImpact` | `array` | Gets the estimated impact info for this recommended action e.g., Estimated CPU gain, Estimated Disk Space change |
| `executeActionDuration` | `string` | Gets the time taken for applying this recommended action on user resource. e.g., time taken for index creation |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseRecommendedActions_ListByDatabaseAdvisor` | `SELECT` | `advisorName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets list of Database Recommended Actions. |
| `DatabaseRecommendedActions_Get` | `EXEC` | `advisorName, databaseName, recommendedActionName, resourceGroupName, serverName, subscriptionId` | Gets a database recommended action. |
| `DatabaseRecommendedActions_Update` | `EXEC` | `advisorName, databaseName, recommendedActionName, resourceGroupName, serverName, subscriptionId` | Updates a database recommended action. |
