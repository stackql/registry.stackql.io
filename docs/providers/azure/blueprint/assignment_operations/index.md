---
title: assignment_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assignment_operations
  - blueprint
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
<tr><td><b>Name</b></td><td><code>assignment_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blueprint.assignment_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | String Id used to locate any resource on Azure. |
| `name` | `string` | Name of this resource. |
| `assignmentState` | `string` | State of this blueprint assignment operation. |
| `timeCreated` | `string` | Create time of this blueprint assignment operation. |
| `timeStarted` | `string` | Start time of the underlying deployment. |
| `type` | `string` | Type of this resource. |
| `blueprintVersion` | `string` | The published version of the blueprint definition used for the blueprint assignment operation. |
| `deployments` | `array` | List of jobs in this blueprint assignment operation. |
| `timeFinished` | `string` | Finish time of the overall underlying deployments. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AssignmentOperations_List` | `SELECT` | `assignmentName, resourceScope` | List operations for given blueprint assignment within a subscription or a management group. |
| `AssignmentOperations_Get` | `EXEC` | `assignmentName, assignmentOperationName, resourceScope` | Get a blueprint assignment operation. |
