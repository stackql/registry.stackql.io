---
title: workflow_run_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_actions
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
<tr><td><b>Name</b></td><td><code>workflow_run_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.workflow_run_actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the workflow run action name. |
| `status` | `string` | The workflow status. |
| `type` | `string` | Gets the workflow run action type. |
| `trackingId` | `string` | Gets the tracking id. |
| `outputsLink` | `object` | The content link. |
| `code` | `string` | Gets the code. |
| `error` | `object` |  |
| `retryHistory` | `array` | Gets the retry histories. |
| `startTime` | `string` | Gets the start time. |
| `trackedProperties` | `object` |  |
| `correlation` | `object` | The workflow run action correlation properties. |
| `inputsLink` | `object` | The content link. |
| `endTime` | `string` | Gets the end time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkflowRunActions_List` | `SELECT` | `api-version, resourceGroupName, runName, subscriptionId, workflowName` | Gets a list of workflow run actions. |
| `WorkflowRunActions_Get` | `EXEC` | `actionName, api-version, resourceGroupName, runName, subscriptionId, workflowName` | Gets a workflow run action. |
| `WorkflowRunActions_ListExpressionTraces` | `EXEC` | `actionName, api-version, resourceGroupName, runName, subscriptionId, workflowName` | Lists a workflow run expression trace. |
