---
title: workflow_trigger_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_trigger_histories
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
<tr><td><b>Name</b></td><td><code>workflow_trigger_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.workflow_trigger_histories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the workflow trigger history name. |
| `startTime` | `string` | Gets the start time. |
| `trackingId` | `string` | Gets the tracking id. |
| `code` | `string` | Gets the code. |
| `fired` | `boolean` | The value indicating whether trigger was fired. |
| `inputsLink` | `object` | The content link. |
| `correlation` | `object` | The correlation property. |
| `outputsLink` | `object` | The content link. |
| `status` | `string` | The workflow status. |
| `type` | `string` | Gets the workflow trigger history type. |
| `endTime` | `string` | Gets the end time. |
| `run` | `object` | The resource reference. |
| `error` | `object` |  |
| `scheduledTime` | `string` | The scheduled time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkflowTriggerHistories_List` | `SELECT` | `name, resourceGroupName, subscriptionId, triggerName, workflowName` | Gets a list of workflow trigger histories. |
| `WorkflowTriggerHistories_Get` | `EXEC` | `historyName, name, resourceGroupName, subscriptionId, triggerName, workflowName` | Gets a workflow trigger history. |
| `WorkflowTriggerHistories_Resubmit` | `EXEC` | `historyName, name, resourceGroupName, subscriptionId, triggerName, workflowName` | Resubmits a workflow run based on the trigger history. |
