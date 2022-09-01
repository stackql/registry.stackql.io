---
title: job_step_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_step_executions
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
<tr><td><b>Name</b></td><td><code>job_step_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_step_executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `target` | `object` | The target that a job execution is executed on. |
| `jobVersion` | `integer` | The job version number. |
| `lifecycle` | `string` | The detailed state of the job execution. |
| `jobExecutionId` | `string` | The unique identifier of the job execution. |
| `currentAttemptStartTime` | `string` | Start time of the current attempt. |
| `endTime` | `string` | The time that the job execution completed. |
| `lastMessage` | `string` | The last status or error message. |
| `startTime` | `string` | The time that the job execution started. |
| `currentAttempts` | `integer` | Number of times the job execution has been attempted. |
| `createTime` | `string` | The time that the job execution was created. |
| `stepName` | `string` | The job step name. |
| `provisioningState` | `string` | The ARM provisioning state of the job execution. |
| `stepId` | `integer` | The job step id. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobStepExecutions_ListByJobExecution` | `SELECT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Lists the step executions of a job execution. |
| `JobStepExecutions_Get` | `EXEC` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Gets a step execution of a job execution. |
