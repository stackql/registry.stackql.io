---
title: workflow_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_runs
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>workflow_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.workflow_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the workflow run name. |
| `outputs` | `object` | Gets the outputs. |
| `workflow` | `object` | The resource reference. |
| `waitEndTime` | `string` | Gets the wait end time. |
| `correlation` | `object` | The correlation property. |
| `startTime` | `string` | Gets the start time. |
| `endTime` | `string` | Gets the end time. |
| `response` | `object` | The workflow run trigger. |
| `code` | `string` | Gets the code. |
| `status` | `string` | The workflow status. |
| `trigger` | `object` | The workflow run trigger. |
| `error` | `object` |  |
| `type` | `string` | Gets the workflow run type. |
| `correlationId` | `string` | Gets the correlation id. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkflowRuns_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId, workflowName` | Gets a list of workflow runs. |
| `WorkflowRuns_Cancel` | `EXEC` | `api-version, resourceGroupName, runName, subscriptionId, workflowName` | Cancels a workflow run. |
| `WorkflowRuns_Get` | `EXEC` | `api-version, resourceGroupName, runName, subscriptionId, workflowName` | Gets a workflow run. |