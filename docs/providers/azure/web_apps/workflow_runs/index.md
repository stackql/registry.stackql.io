---
title: workflow_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_runs
  - web_apps
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
<tr><td><b>Id</b></td><td><code>azure.web_apps.workflow_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the workflow run name. |
| `endTime` | `string` | Gets the end time. |
| `startTime` | `string` | Gets the start time. |
| `status` | `string` | The workflow status. |
| `response` | `object` | The workflow run trigger. |
| `correlationId` | `string` | Gets the correlation id. |
| `outputs` | `object` | Gets the outputs. |
| `code` | `string` | Gets the code. |
| `waitEndTime` | `string` | Gets the wait end time. |
| `workflow` | `object` | The resource reference. |
| `error` | `object` |  |
| `correlation` | `object` | The correlation property. |
| `type` | `string` | Gets the workflow run type. |
| `trigger` | `object` | The workflow run trigger. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkflowRuns_List` | `SELECT` | `name, resourceGroupName, subscriptionId, workflowName` | Gets a list of workflow runs. |
| `WorkflowRuns_Cancel` | `EXEC` | `name, resourceGroupName, runName, subscriptionId, workflowName` | Cancels a workflow run. |
| `WorkflowRuns_Get` | `EXEC` | `name, resourceGroupName, runName, subscriptionId, workflowName` | Gets a workflow run. |
