---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - machine_learning_experimentation
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_experimentation.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `description` | `string` | The description of this workspace. |
| `creationDate` | `string` | The creation date of the machine learning workspace in ISO8601 format. |
| `tags` | `object` | The tags of the resource. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
| `provisioningState` | `string` | The current deployment state of team account workspace resource. The provisioningState is to indicate states for resource provisioning. |
| `friendlyName` | `string` | The friendly name for this workspace. This will be the workspace name in the arm id when the workspace object gets created |
| `type` | `string` | The type of the resource. |
| `workspaceId` | `string` | The immutable id of this workspace. |
| `accountId` | `string` | The immutable id of the team account which contains this workspace. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Workspaces_ListByAccounts` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all the available machine learning workspaces under the specified team account. |
| `Workspaces_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates a machine learning workspace with the specified parameters. |
| `Workspaces_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId, workspaceName` | Deletes a machine learning workspace. |
| `Workspaces_Get` | `EXEC` | `accountName, resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified machine learning workspace. |
| `Workspaces_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId, workspaceName` | Updates a machine learning workspace with the specified parameters. |
