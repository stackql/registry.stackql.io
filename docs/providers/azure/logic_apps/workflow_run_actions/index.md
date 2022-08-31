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
| `error` | `object` |  |
| `retryHistory` | `array` | Gets the retry histories. |
| `status` | `string` | The workflow status. |
| `code` | `string` | Gets the code. |
| `inputsLink` | `object` | The content link. |
| `endTime` | `string` | Gets the end time. |
| `correlation` | `object` | The workflow run action correlation properties. |
| `type` | `string` | Gets the workflow run action type. |
| `trackedProperties` | `object` |  |
| `outputsLink` | `object` | The content link. |
| `startTime` | `string` | Gets the start time. |
| `trackingId` | `string` | Gets the tracking id. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkflowRunActions_List` | `SELECT` | `api-version, resourceGroupName, runName, subscriptionId, workflowName` | Gets a list of workflow run actions. |
| `WorkflowRunActions_Get` | `EXEC` | `actionName, api-version, resourceGroupName, runName, subscriptionId, workflowName` | Gets a workflow run action. |
| `WorkflowRunActions_ListExpressionTraces` | `EXEC` | `actionName, api-version, resourceGroupName, runName, subscriptionId, workflowName` | Lists a workflow run expression trace. |
