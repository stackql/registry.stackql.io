---
title: action_plan_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - action_plan_operations
  - deployment_admin
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
<tr><td><b>Name</b></td><td><code>action_plan_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_admin.action_plan_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `description` | `string` | The operation description |
| `actionPlanOperationId` | `string` | Action plan operation identifier |
| `blobContainerName` | `string` | Blob container name storing the deployment data |
| `provisioningState` | `string` | The provisioning state |
| `outputs` | `object` | The action plan operation outputs in JToken format |
| `parameters` | `object` | The deployment parameters in JToken format |
| `startTime` | `string` | The deployment start time |
| `error` | `object` | Error response. |
| `eTag` | `string` | Entity tag of the resource |
| `location` | `string` | Location of the resource. |
| `endTime` | `string` | The deployment end time |
| `title` | `string` | The operation title |
| `actionPlanInstanceId` | `string` | Action plan instance identifier |
| `subscriptionId` | `string` | The target subscription identifier |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ActionPlanOperations_List` | `SELECT` | `planId, subscriptionId` | Lists the action plan operations |
| `ActionPlanOperations_Get` | `EXEC` | `operationId, planId, subscriptionId` | Gets the specified action plan operation |
