---
title: sql_pool_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_operations
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The operation description. |
| `percentComplete` | `integer` | The percentage of the operation completed. |
| `state` | `string` | The operation state. |
| `serverName` | `string` | The name of the server. |
| `operationFriendlyName` | `string` | The friendly name of operation. |
| `operation` | `string` | The name of operation. |
| `startTime` | `string` | The operation start time. |
| `errorCode` | `integer` | The operation error code. |
| `errorDescription` | `string` | The operation error description. |
| `databaseName` | `string` | The name of the Sql pool the operation is being performed on. |
| `isCancellable` | `boolean` | Whether the operation can be cancelled. |
| `errorSeverity` | `integer` | The operation error severity. |
| `estimatedCompletionTime` | `string` | The estimated completion time of the operation. |
| `isUserError` | `boolean` | Whether or not the error is a user error. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SqlPoolOperations_List` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` |
