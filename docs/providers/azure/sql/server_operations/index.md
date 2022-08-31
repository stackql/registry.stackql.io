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
| `serverName` | `string` | The name of the server. |
| `operation` | `string` | The name of operation. |
| `operationFriendlyName` | `string` | The friendly name of operation. |
| `errorDescription` | `string` | The operation error description. |
| `estimatedCompletionTime` | `string` | The estimated completion time of the operation. |
| `errorCode` | `integer` | The operation error code. |
| `errorSeverity` | `integer` | The operation error severity. |
| `state` | `string` | The operation state. |
| `percentComplete` | `integer` | The percentage of the operation completed. |
| `startTime` | `string` | The operation start time. |
| `isUserError` | `boolean` | Whether or not the error is a user error. |
| `isCancellable` | `boolean` | Whether the operation can be cancelled. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ServerOperations_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` |
