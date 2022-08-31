---
title: workflow_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_triggers
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
<tr><td><b>Name</b></td><td><code>workflow_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.workflow_triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the workflow trigger name. |
| `recurrence` | `object` | The workflow trigger recurrence. |
| `changedTime` | `string` | Gets the changed time. |
| `state` | `string` | The workflow state. |
| `status` | `string` | The workflow status. |
| `createdTime` | `string` | Gets the created time. |
| `provisioningState` | `string` | The workflow trigger provisioning state. |
| `type` | `string` | Gets the workflow trigger type. |
| `workflow` | `object` | The resource reference. |
| `lastExecutionTime` | `string` | Gets the last execution time. |
| `nextExecutionTime` | `string` | Gets the next execution time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkflowTriggers_List` | `SELECT` | `name, resourceGroupName, subscriptionId, workflowName` | Gets a list of workflow triggers. |
| `WorkflowTriggers_Get` | `EXEC` | `name, resourceGroupName, subscriptionId, triggerName, workflowName` | Gets a workflow trigger. |
| `WorkflowTriggers_GetSchemaJson` | `EXEC` | `name, resourceGroupName, subscriptionId, triggerName, workflowName` | Get the trigger schema as JSON. |
| `WorkflowTriggers_ListCallbackUrl` | `EXEC` | `name, resourceGroupName, subscriptionId, triggerName, workflowName` | Get the callback URL for a workflow trigger. |
| `WorkflowTriggers_Run` | `EXEC` | `name, resourceGroupName, subscriptionId, triggerName, workflowName` | Runs a workflow trigger. |