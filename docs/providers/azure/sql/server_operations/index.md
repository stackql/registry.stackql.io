---
title: server_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - server_operations
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
<tr><td><b>Name</b></td><td><code>server_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The operation description. |
| `estimatedCompletionTime` | `string` | The estimated completion time of the operation. |
| `operation` | `string` | The name of operation. |
| `errorCode` | `integer` | The operation error code. |
| `isUserError` | `boolean` | Whether or not the error is a user error. |
| `isCancellable` | `boolean` | Whether the operation can be cancelled. |
| `serverName` | `string` | The name of the server. |
| `errorDescription` | `string` | The operation error description. |
| `startTime` | `string` | The operation start time. |
| `percentComplete` | `integer` | The percentage of the operation completed. |
| `operationFriendlyName` | `string` | The friendly name of operation. |
| `state` | `string` | The operation state. |
| `errorSeverity` | `integer` | The operation error severity. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ServerOperations_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` |
