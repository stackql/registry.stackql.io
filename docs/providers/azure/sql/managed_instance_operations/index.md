---
title: managed_instance_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_operations
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
<tr><td><b>Name</b></td><td><code>managed_instance_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The operation description. |
| `operationFriendlyName` | `string` | The friendly name of operation. |
| `isUserError` | `boolean` | Whether or not the error is a user error. |
| `operation` | `string` | The name of operation. |
| `managedInstanceName` | `string` | The name of the managed instance the operation is being performed on. |
| `operationSteps` | `object` | The steps of a managed instance operation. |
| `errorCode` | `integer` | The operation error code. |
| `percentComplete` | `integer` | The percentage of the operation completed. |
| `errorSeverity` | `integer` | The operation error severity. |
| `estimatedCompletionTime` | `string` | The estimated completion time of the operation. |
| `startTime` | `string` | The operation start time. |
| `operationParameters` | `object` | The parameters of a managed instance operation. |
| `isCancellable` | `boolean` | Whether the operation can be cancelled. |
| `errorDescription` | `string` | The operation error description. |
| `state` | `string` | The operation state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstanceOperations_ListByManagedInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of operations performed on the managed instance. |
| `ManagedInstanceOperations_Cancel` | `EXEC` | `managedInstanceName, operationId, resourceGroupName, subscriptionId` | Cancels the asynchronous operation on the managed instance. |
| `ManagedInstanceOperations_Get` | `EXEC` | `managedInstanceName, operationId, resourceGroupName, subscriptionId` | Gets a management operation on a managed instance. |
