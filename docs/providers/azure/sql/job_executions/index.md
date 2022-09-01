---
title: job_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_executions
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
<tr><td><b>Name</b></td><td><code>job_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `target` | `object` | The target that a job execution is executed on. |
| `createTime` | `string` | The time that the job execution was created. |
| `lastMessage` | `string` | The last status or error message. |
| `lifecycle` | `string` | The detailed state of the job execution. |
| `startTime` | `string` | The time that the job execution started. |
| `currentAttemptStartTime` | `string` | Start time of the current attempt. |
| `stepName` | `string` | The job step name. |
| `provisioningState` | `string` | The ARM provisioning state of the job execution. |
| `jobVersion` | `integer` | The job version number. |
| `jobExecutionId` | `string` | The unique identifier of the job execution. |
| `currentAttempts` | `integer` | Number of times the job execution has been attempted. |
| `stepId` | `integer` | The job step id. |
| `endTime` | `string` | The time that the job execution completed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobExecutions_ListByAgent` | `SELECT` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Lists all executions in a job agent. |
| `JobExecutions_ListByJob` | `SELECT` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Lists a job's executions. |
| `JobExecutions_Create` | `INSERT` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Starts an elastic job execution. |
| `JobExecutions_CreateOrUpdate` | `INSERT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Creates or updates a job execution. |
| `JobExecutions_Cancel` | `EXEC` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Requests cancellation of a job execution. |
| `JobExecutions_Get` | `EXEC` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Gets a job execution. |
