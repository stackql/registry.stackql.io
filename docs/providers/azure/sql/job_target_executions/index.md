---
title: job_target_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_target_executions
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
<tr><td><b>Name</b></td><td><code>job_target_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_target_executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `stepName` | `string` | The job step name. |
| `endTime` | `string` | The time that the job execution completed. |
| `target` | `object` | The target that a job execution is executed on. |
| `currentAttempts` | `integer` | Number of times the job execution has been attempted. |
| `currentAttemptStartTime` | `string` | Start time of the current attempt. |
| `lifecycle` | `string` | The detailed state of the job execution. |
| `provisioningState` | `string` | The ARM provisioning state of the job execution. |
| `stepId` | `integer` | The job step id. |
| `createTime` | `string` | The time that the job execution was created. |
| `jobExecutionId` | `string` | The unique identifier of the job execution. |
| `lastMessage` | `string` | The last status or error message. |
| `startTime` | `string` | The time that the job execution started. |
| `jobVersion` | `integer` | The job version number. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobTargetExecutions_ListByJobExecution` | `SELECT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Lists target executions for all steps of a job execution. |
| `JobTargetExecutions_ListByStep` | `SELECT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Lists the target executions of a job step execution. |
| `JobTargetExecutions_Get` | `EXEC` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId, targetId` | Gets a target execution. |