---
title: database_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - database_operations
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
<tr><td><b>Name</b></td><td><code>database_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The operation description. |
| `startTime` | `string` | The operation start time. |
| `isUserError` | `boolean` | Whether or not the error is a user error. |
| `errorDescription` | `string` | The operation error description. |
| `databaseName` | `string` | The name of the database the operation is being performed on. |
| `serverName` | `string` | The name of the server. |
| `errorSeverity` | `integer` | The operation error severity. |
| `estimatedCompletionTime` | `string` | The estimated completion time of the operation. |
| `state` | `string` | The operation state. |
| `percentComplete` | `integer` | The percentage of the operation completed. |
| `operationFriendlyName` | `string` | The friendly name of operation. |
| `operation` | `string` | The name of operation. |
| `isCancellable` | `boolean` | Whether the operation can be cancelled. |
| `errorCode` | `integer` | The operation error code. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseOperations_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of operations performed on the database. |
| `DatabaseOperations_Cancel` | `EXEC` | `databaseName, operationId, resourceGroupName, serverName, subscriptionId` | Cancels the asynchronous operation on the database. |
